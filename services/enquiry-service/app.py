from flask import Flask, request
from kubernetes import client, config

app = Flask(__name__)

config.load_incluster_config()

api = client.CustomObjectsApi()

@app.route("/api/enquiry", methods=["POST"])
def enquiry():

    data = request.json

    body = {
        "apiVersion": "hotel.com/v1",
        "kind": "Enquiry",
        "metadata": {
            "name": data["name"].lower().replace(" ","-")
        },
        "spec": {
            "name": data["name"],
            "phone": data["phone"],
            "message": data["message"]
        }
    }

    api.create_namespaced_custom_object(
        group="hotel.com",
        version="v1",
        namespace="default",
        plural="enquiries",
        body=body
    )

    return {"status":"created"}

app.run(host="0.0.0.0",port=5000)
