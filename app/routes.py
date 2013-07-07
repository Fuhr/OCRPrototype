import os, sys

from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename

sys.path.append('./pytesser/')
from pytesser import *


UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'tif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/')
# def home():
#     return render_template('home.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            image_string = image_file_to_string(UPLOAD_FOLDER + filename)

            return render_template('result.html', result = image_string)

    return render_template('home.html')




if __name__ == '__main__':
    app.run(debug=True)
