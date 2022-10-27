from fileinput import filename
#from DeepImageSearch import Index, LoadData, SearchImage
import numpy as np
from flask import request, redirect, render_template, Flask
import os
import pickle
from flask_cors import CORS
from werkzeug.utils import secure_filename
from PIL import Image
import io
import base64

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "C:/Users/tejas/OneDrive/Desktop/Intership/webpage/static/Images"
CORS(app)

#model = pickle.load(open('models/model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/Star')
def Star():
    return render_template('Star.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':

        image = request.files['myFile']
        if image.filename == '':
            print("file name is invalid")
            return redirect(request.url)
        global filename
        filename = secure_filename(image.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(
            basedir, app.config["IMAGE_UPLOADS"], filename))
        img = Image.open(app.config["IMAGE_UPLOADS"]+"/" + filename)
        data = io.BytesIO()
        img.save(data, "JPEG")

        encode_img_data = base64.b64encode(data.getvalue())

        return render_template("index.html", filename=encode_img_data.decode("UTF-8"))

    return render_template('index.html')


""" @app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        image_list = LoadData().from_folder(['Data'])
        Index(image_list).Start()
        results = SearchImage().get_similar_images(
            image_path=["IMAGE_UPLOADS"]+"/" + filename, number_of_images=5)
        print(results) """


if __name__ == '__main__':
    app.run()
