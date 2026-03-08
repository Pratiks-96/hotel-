from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Prometheus counter for menu requests
MENU_REQUEST_COUNT = Counter(
    'menu_requests_total',
    'Total number of menu requests'
)

# Sample menu
menu = [
    {"name": "Paneer Butter Masala", "price": 220},
    {"name": "Veg Biryani", "price": 180},
    {"name": "Masala Dosa", "price": 120}
]

# Endpoint to get menu
@app.route("/menu")
def get_menu():
    MENU_REQUEST_COUNT.inc()  # Increment counter on each request
    return jsonify(menu)

# Metrics endpoint for Prometheus
@app.route("/menu/metrics")
def metrics():
    # Set proper MIME type for Prometheus scraping
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
