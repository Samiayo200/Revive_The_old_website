from flask import Flask, request, jsonify, render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')
    


@app.route('/Cars')
def cars():
    return reder_template('products_car.html')
    
   
#@app.route('/Cars')
#def cars():
 #   return reder_template('products_jewelery.html')
    
    
#@app.route('/Cars')
#def cars():
#    return reder_template('products_watch.html')
    



if __name__ == '__main__':
    app.run(debug=True) 
