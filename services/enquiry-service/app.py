from flask import Flask,request
from prometheus_client import Counter,generate_latest

app = Flask(__name__)

ENQUIRY_COUNT = Counter(
'enquiry_total',
'Total enquiries'
)

data=[]

@app.route("/enquiry",methods=["POST"])
def enquiry():

    body=request.json

    data.append(body)

    ENQUIRY_COUNT.inc()

    return {"status":"saved"}

@app.route("/metrics")
def metrics():
    return generate_latest()

app.run(host="0.0.0.0",port=5000)
