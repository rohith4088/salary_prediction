import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas  as pd
app = Flask(__name__)
#load the model
model = pickle.load(open("reg_model.pkl",'rb'))
scaling = pickle.load(open("scaling.pkl",'rb'))
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/predict_api',methods = ['POST'])
def predict_api():
    data = request.json['data']  # in the form of dictionary
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    new_data = scaling.transform(np.array(list(data.values())).reshape(1, -1))
    output = model.predict(new_data)
    print(output)
    return jsonify(output.tolist())

if __name__ == "__main__":
    app.run(debug = True)
    