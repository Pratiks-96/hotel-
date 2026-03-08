from flask import Flask, request, jsonify
from kubernetes import client, config
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Kubernetes config
config.load_incluster_config()
api = client.CustomObjectsApi()

# -----------------------
# Prometheus metrics
# -----------------------
# Total number of orders received
ORDERS_COUNTER = Counter('orders_received_total', 'Total number of orders received')

# Total orders by purpose
ORDERS_BY_PURPOSE = Counter('orders_by_purpose_total', 'Orders grouped by purpose', ['purpose'])

# -----------------------
# Purpose detection
# -----------------------
def detect_purpose(message):
    msg = message.lower()
    if "wedding" in msg or "function" in msg or "party" in msg:
        return "event-booking"
    if "catering" in msg:
        return "catering"
    if "order" in msg or "biryani" in msg or "pizza" in msg:
        return "food-order"
    if "table" in msg or "reservation" in msg:
        return "table-booking"
    return "general-enquiry"

# -----------------------
# Create order/enquiry
# -----------------------
@app.route("/api/enquiry", methods=["POST"])
def create_enquiry():
    data = request.json
    purpose = detect_purpose(data["message"])

    # Increment Prometheus counters
    ORDERS_COUNTER.inc()
    ORDERS_BY_PURPOSE.labels(purpose=purpose).inc()

    body = {
        "apiVersion": "hotel.com/v1",
        "kind": "Enquiry",
        "metadata": {
            "name": data["name"].lower().replace(" ", "-")
        },
        "spec": {
            "name": data["name"],
            "phone": data["phone"],
            "message": data["message"],
            "purpose": purpose
        }
    }

    try:
        api.create_namespaced_custom_object(
            group="hotel.com",
            version="v1",
            namespace="default",
            plural="enquiries",
            body=body
        )
    except client.exceptions.ApiException as e:
        # If resource already exists, ignore
        if e.status != 409:
            raise

    return jsonify({"status": "created", "purpose": purpose})

# -----------------------
# Get all enquiries
# -----------------------
@app.route("/api/enquiries", methods=["GET"])
def get_enquiries():
    enquiries = api.list_namespaced_custom_object(
        group="hotel.com",
        version="v1",
        namespace="default",
        plural="enquiries"
    )

    results = []
    for item in enquiries["items"]:
        results.append({
            "name": item["spec"]["name"],
            "phone": item["spec"]["phone"],
            "message": item["spec"]["message"],
            "purpose": item["spec"].get("purpose", "unknown")
        })

    return jsonify(results)

# -----------------------
# Prometheus metrics endpoint
# -----------------------
@app.route("/order/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

# -----------------------
# Run Flask app
# -----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8083)
