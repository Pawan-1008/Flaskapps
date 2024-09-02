from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():   
    return "Hello World !"

@app.route('/pawan')
def hello():   
    return "Hello Pawan how are you ?"

app.run()
