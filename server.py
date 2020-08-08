import main
import flask
from flask import Flask, request
import json
app = Flask(__name__)


@app.route("/", methods=["GET"])
def _hello_world():
	return "Hello world"

@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    req_data = request.get_json()
    img_path = req_data["image_url"]
    print("img_image",img_path)

    number_plate = main.main(img_path)
    data["number_plate"] = str(number_plate)
    data["success"] = True
    return json.dumps(data, ensure_ascii=False)

if __name__ == "__main__":
    print("App run!")
    app.run(debug=False, host="127.0.0.1", threaded=False)