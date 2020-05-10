from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print('test message')
    return '<h1>Hello, YoYoYo!</h1>'