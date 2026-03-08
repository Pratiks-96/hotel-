from flask import Flask, request, jsonify
from kubernetes import client, config

app = Flask(__name__)

config.load_incluster_config()

api = client.CustomObjectsApi()

# CREATE ENQUIRY
@app.route("/api/enquiry", methods=["POST"])
def create_enquiry():

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

    return {"status": "created"}


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
            "message": item["spec"]["message"]
        })

    return jsonify(results)


app.run(host="0.0.0.0", port=5000)
