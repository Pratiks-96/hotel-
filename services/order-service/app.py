from flask import Flask,request,jsonify
from prometheus_client import Counter,generate_latest

app = Flask(__name__)

orders=[]

ORDER_COUNT = Counter(
'orders_total',
'Total orders'
)

@app.route("/orders",methods=["POST"])
def create():

    data=request.json

    orders.append(data)

    ORDER_COUNT.inc()

    return {"status":"order placed"}

@app.route("/orders")
def get_orders():

    return jsonify(orders)

@app.route("/metrics")
def metrics():
    return generate_latest()

app.run(host="0.0.0.0",port=5000)
