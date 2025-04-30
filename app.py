from flask import Flask

app = Flask(__name__)

@app.route('/')
def greet_world():
    return "<h1>Hello, World!</h1>"

@app.route('/greet/<name>')
def greet_person(name):
    return f"<h1>Hello, {name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')