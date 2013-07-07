import os, sys
import datetime
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


            name_split = str(file.filename).split('.')



            temp_file = name_split[0] + str(datetime.datetime.now()) + '.' + name_split[1]
            filename = secure_filename(temp_file.decode('utf-8'))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            image_string = image_file_to_string(UPLOAD_FOLDER + filename)
            print image_string
            return render_template('result.html', result = image_string.decode('utf-8'))

    return render_template('home.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)