from flask import Flask, render_template

app = Flask(__name__)

app.route('/', method=['GET'])
def index():
    return render_template('index.html')
