import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.applications.inception_v3 import preprocess_input as p1
from keras.models import Sequential, load_model
from werkzeug.utils import secure_filename
import numpy as np
from keras.preprocessing import image 



ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
IMAGE_SIZE = (224, 224)
UPLOAD_FOLDER = 'uploads'
model_mobile = load_model('C:/Users/Harshinee Sriram/OneDrive/Desktop/Wikimedia/keras-flask-image-classifier/model/model_MobileNet.h5')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def predict(file):
    img = load_img(file, target_size=(224, 224))
    img = image.img_to_array(img)
    img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
    img = p1(img)
    yhat = model_mobile.predict(img)
    output = yhat
    return output

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def template_test():
    return render_template('home.html', label='', imagesource='file://null')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            output = predict(file_path)
    return render_template("home.html", label=output, imagesource=file_path)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == "__main__":
    app.run(debug=False, threaded=False)
