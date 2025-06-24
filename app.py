from flask import Flask, request, jsonify, render_template
import json
import os


json_cars_path = os.path.join('data', 'data_cars.json')
def loadjson():
    with open(json_cars_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
    





@app.route('/products_car')
def products_car():
    return render_template('products_car.html', cars=loadjson())
    
   
@app.route('/products_watch')
def products_watch():
    return render_template('products_watch.html')


@app.route('/products_jewelery')
def products_jewelery():
    return render_template('products_jewelery.html')






@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')




if __name__ == '__main__':
    app.run(debug=True) 
