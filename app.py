import os
from flask import Flask, request, render_template
import object_classifier

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def detect_object():
    if request.method == 'GET':
       return render_template('index.html')
    if request.method == 'POST':
        if 'file' not in request.files:
            print('file not uploaded')
            return
        file = request.files['file']
        image = file.read()
        predicted_class, confidence = object_classifier.get_predictions(image)
        filename = file.filename
        predicted = '1. %s, %.4f'%(predicted_class, confidence)
           

        return render_template('result.html', output=predicted, image=filename)

if __name__ == '__main__':
    app.run(debug=True)