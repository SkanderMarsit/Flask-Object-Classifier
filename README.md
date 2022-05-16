# Flask-Object-Classifier

This project aims at creating a Flask API that exposes a basic pretrained ImageNet object classifier. 

## Run using Docker
```
$ docker build . -t object_classifier
$ docker run -p 5000:5000 object_classifier 
```

Go to `http://127.0.0.1:5000/` via chrome browser and upload image from `static` folder. 
