from flask import Flask, render_template
import os
from predictor import check

app = Flask(__name__, static_folder="images")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print("Upload directory:", target)

    if not os.path.isdir(target):
        os.mkdir(target)

    file = request.files['file']
    filename = file.filename
    dest = os.path.join(target, filename)
    print("Saving file to:", dest)

    file.save(dest)  # Save the uploaded file

    #  Predict the tumor type
    predicted_class = check(filename)

    return render_template('complete.html', image_name=filename, predvalue=predicted_class)


if __name__ == "__main__":
    app.run(debug=True)