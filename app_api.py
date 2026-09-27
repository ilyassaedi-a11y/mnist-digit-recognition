from flask import Flask, request, jsonify
import numpy as np
from tensorflow import keras
from PIL import Image

app = Flask(__name__)
model = keras.models.load_model('mnist_ann_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    img = Image.open(file).convert('L').resize((28, 28))
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 28, 28)

    prediction = model.predict(img_array)
    predicted_digit = int(np.argmax(prediction))
    confidence = float(np.max(prediction))

    return jsonify({
        'predicted_digit': predicted_digit,
        'confidence': confidence
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)