# Dependencies
import numpy as np
import pandas as pd
from flask import Flask, render_template, request,redirect

# Create an instance of Flask
app = Flask(__name__)

 
app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    
    # Return template and data
    return render_template("index.html")

@app.route("/happy")
def happy():
    return "I am happy"    

    
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)