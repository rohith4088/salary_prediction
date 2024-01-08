import pickle
from Flask import flask,request,app,jsonify,url_for,render_template
import numpy
import pandas 
app = Flask(__name__)
#load the model
model = pickle.load(open("regressor_model.pkl",'rb'))
@app.route('/')
def home():
    return render_template("home.html")
