import main
import flask
from flask import Flask, request
import json
import numpy as np
import cv2
app = Flask(__name__)


@app.route("/", methods=["GET"])
def _hello_world():
	return "Hello world"

@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    # req_data = request.get_json()
    # img_path = req_data["image_url"]
    # print("img_image",img_path)
    # number_plate = main.main(img_path)
    if request.files:
        image = request.files["image"].read()
        npimg = np.fromstring(image, np.uint8)
        # convert numpy array to image
        img = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)
        number_plate = main.main(img)

        data["number_plate"] = str(number_plate)
        data["success"] = True

    return json.dumps(data, ensure_ascii=False)

if __name__ == "__main__":
    print("App run!")
    app.run(debug=False, host="127.0.0.1", threaded=False)