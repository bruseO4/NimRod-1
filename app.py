import request 
from flask import Flask, request, render_template
app = Flask(__name__)
  

@app.route('/')
def my_form():
    return render_template('output.html')

@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    #processed_text = variable.upper()
    return variable
    

