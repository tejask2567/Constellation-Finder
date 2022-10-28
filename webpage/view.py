from fileinput import filename
from importlib.resources import path
from DeepImageSearch import Index, LoadData, SearchImage
import numpy as np
from flask import request, redirect, render_template, Flask
import os
from flask_cors import CORS
from werkzeug.utils import secure_filename
from PIL import Image
import io
import base64
from werkzeug.utils import secure_filename
import logging
from pathlib import Path
import cv2 as cv

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


var_List = []


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':

        image = request.files['myFile']
        if image.filename == '':
            print("file name is invalid")
            return redirect(request.url)
        filename = secure_filename(image.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
        print(basedir)
        image.save(os.path.join(
            basedir, app.config["IMAGE_UPLOADS"], filename))
        path = os.path.join(
            basedir, app.config["IMAGE_UPLOADS"], filename)
        print(path)
        global img
        img = Image.open(app.config["IMAGE_UPLOADS"]+"/" + filename)
        data = io.BytesIO()
        img.save(data, "JPEG")
        # data.seek(0)
        #plot_url = base64.b64encode(img.getvalue()).decode()
        #im_source = "data:Images/jpeg;base64,{}".format(plot_url)
        #image_list = LoadData().from_folder(['Data'])
        # Index(image_list).Start()
        results = SearchImage().get_similar_images(
            image_path=path, number_of_images=1)
        global res
        res = list(results.values())[0]
        var_List.append(res)
        #encode_img_data = base64.b64encode(data.getvalue())

        return render_template("index.html", filename=filename)

    return render_template('index.html')


""" image_list = LoadData().from_folder(['Data'])
Index(image_list).Start()
results = SearchImage().get_similar_images(
    image_path=(os.path.abspath(img)), number_of_images=1)
res = list(results.values())[0] """


@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        res2 = var_List.pop()
        processed_text = res2.split('\\')[1].split('_')[0]
        return render_template('index.html', processed_text=processed_text)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
