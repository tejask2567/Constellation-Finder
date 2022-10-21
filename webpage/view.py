from flask import request, redirect
import os
from app import app

app.config["IMAGE_UPLOADS"] = "webpage/uploads"


@app.route("/upload-image", methods=['GET', 'POST'])
def img_upload():

    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(
                app.config["IMAGE_UPLOADS"], image.filename))
            print("Image Saved")
            return redirect(request.url)
    return render_template("/index.html")
