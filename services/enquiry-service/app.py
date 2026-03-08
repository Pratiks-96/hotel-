from flask import Flask, request, jsonify
from kubernetes import client, config

app = Flask(__name__)

# Load Kubernetes in-cluster config
config.load_incluster_config()

api = client.CustomObjectsApi()


# PURPOSE DETECTION FUNCTION
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


# CREATE ENQUIRY
@app.route("/api/enquiry", methods=["POST"])
def create_enquiry():

    data = request.json

    # detect purpose
    purpose = detect_purpose(data["message"])

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

    api.create_namespaced_custom_object(
        group="hotel.com",
        version="v1",
        namespace="default",
        plural="enquiries",
        body=body
    )

    return jsonify({
        "status": "created",
        "purpose": purpose
    })


# GET ALL ENQUIRIES
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


# RUN APP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
