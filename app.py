from flask import Flask, render_template , request, jsonify
import json
import pandas as pd
import pickle
import math


car_brands_data = pd.read_json('car_brands.json')
loaded_model = pickle.load(open('./pr.sav',"rb"))


app = Flask(__name__)



@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/rate', methods=["POST", "GET"])
def rate(): 
    if request.method == "POST":
        brand = request.form.get("brand")
        model_name = request.form.get("car_model")
        car_model = request.form.get('year')
        gear = request.form.get("gear")
        fule = request.form.get("fule")
        car_id = request.form.get("car_id")
        kiloage = request.form.get("kiloage")
        NOP = request.form.get("NOP")
        engine = request.form.get("engine_power")
        pay = request.form.get("pay_method")
        sunrof = request.form.get("sunrof")
        df = pd.read_csv('header.csv')
        df.loc[0] = 0
        df['car_model']= car_model
        df['قوة الماتور'] = engine
        df['عداد السيارة']= kiloage
        df['عدد الركاب']= NOP
        df['فتحة سقف']=sunrof   
        df[fule]=1
        df[pay]=1
        df[gear]=1
        df[car_id]=1
        df[ brand + '_' + model_name ]= 1
        df=df.drop(columns=["Unnamed: 0"])
        
        X=df.drop(columns=["car_price"])
        result = loaded_model.predict(X)
        predict =math.floor(result[0])
        
        
        return render_template('rate.html',car_brand=car_brands_data, predict = predict)
    else:
        return render_template('rate.html',car_brand=car_brands_data)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/get_models/<company_name>')
def get_models(company_name):
    company_models = car_brands_data[car_brands_data["company_name"] == company_name]["models"]
    return jsonify(company_models.tolist())

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
