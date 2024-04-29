from flask import Flask, send_file

app = Flask(__name__)

with app.app.context():
    from . import init_app
    init_app(app)

@app.route('/')
def hello():
    return 'Hello World!'
