from flask import Flask,url_for,render_template,request
import pickle
import math
import sys

f1 = open("month.pkl",'rb')
f2 = open("product.pkl",'rb')
f3 = open("rfr.pkl",'rb')

month = pickle.load(f1)
product = pickle.load(f2)
model = pickle.load(f3)


app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def home():
    value = 0
    if request.method=='POST':
        year = request.form.get("year")
        month_1 = request.form.get("month")
        product_1 = request.form.get("product")
        
        value = math.floor(model.predict([[month.transform([month_1])[0],year,product.transform([product_1])[0]]])[0])
    
    return render_template("form.html",value=value)

app.run(port=5000)