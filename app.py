import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas  as pd
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
    print(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(data)
    print(output[0])
    return jsonify(output[0])
if __name__ == __main__:
    app.run(debug = True)
    