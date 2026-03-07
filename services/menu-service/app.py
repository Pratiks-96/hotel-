from flask import Flask,jsonify
from prometheus_client import Counter,generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'menu_requests_total',
    'Menu Requests'
)

menu = [
 {"name":"Paneer Butter Masala","price":220},
 {"name":"Veg Biryani","price":180},
 {"name":"Masala Dosa","price":120}
]

@app.route("/menu")
def get_menu():

    REQUEST_COUNT.inc()

    return jsonify(menu)


@app.route("/metrics")
def metrics():
    return generate_latest()

app.run(host="0.0.0.0",port=5000)
