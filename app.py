from flask import Flask,render_template
# Flask-It is our framework which we are going to use to run/serve our application.
#request-for accessing file which was uploaded by the user on our application.

# import numpy as np #used for numerical analysis
# from tensorflow.keras.models import load_model#to load our trained model
# from tensorflow.keras.preprocessing import image

import requests


app = Flask(__name__,template_folder="templates") # initializing a flask app
# Loading the model
# model=load_model('nutrition.h5')
print("Loaded model from disk")


@app.route('/')# route to display the home page
def home():
    return render_template('home.html')#rendering the home page

@app.route('/image1',methods=['GET','POST'])# routes to the index html
def image1():
    return render_template("image.html")


if __name__ == "__main__":
    app.run('0.0.0.0',port=8080,debug=True)
