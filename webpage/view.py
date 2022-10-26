from fileinput import filename
#from DeepImageSearch import Index, LoadData, SearchImage
import numpy as np
from flask import request, redirect, render_template, Flask
import os
import pickle
from flask_cors import CORS
from werkzeug.utils import secure_filename
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


""" @app.route("/upload-image", methods=['GET', 'POST'])
def img_upload():

    if request.method == "POST":
        if request.files:
            image = request.files["myFile"]
            image.save(os.path.join(
                app.config["IMAGE_UPLOADS"], image.filename))
            print("Image Saved")
            return redirect(request.url)
    return render_template("/index.html")
 """


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':

        image = request.files['myFile']
        if image.filename == '':
            print("file name is invalid")
            return redirect(request.url)

        filename = secure_filename(image.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(
            basedir, app.config["IMAGE_UPLOADS"], filename))

        return render_template("index.html", filename=filename)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()

""" 
image_list = LoadData().from_folder(['Data'])

# For Faster Serching we need to index Data first, After Indexing all the meta data stored on the local path
Index(image_list).Start()

# for searching, you need to give the image path and the number of the similar image you want
results = SearchImage().get_similar_images(
    image_path=image_list[0], number_of_images=5)

# If you want to plot similar images you can use this method, It will plot 16 most similar images from the data index
print(results)
 """
