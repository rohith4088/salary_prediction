import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy
import pandas 
app = Flask(__name__)
#load the model
model = pickle.load(open("regressor_model.pkl",'rb'))
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/predict_api',methods = ['POST'])
def predict_api():
    data = request.json['data'] #in the form of dictornary
    print(data)
    
    
 