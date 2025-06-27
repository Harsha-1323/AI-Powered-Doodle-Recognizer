from flask import Flask, render_template, request, jsonify
import re, base64, io
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from utils import preprocess

app = Flask(__name__)
model = load_model("model/doodle_model.h5")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    img_data = re.sub('^data:image/.+;base64,', '', data['image'])
    image = Image.open(io.BytesIO(base64.b64decode(img_data)))
    
    processed = preprocess(image)  # preprocess returns a model-ready array
    prediction = model.predict(processed)
    label = np.argmax(prediction)

    return jsonify({"prediction": str(label)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
