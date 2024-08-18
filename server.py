from flask import Flask

app = Flask(__name__)

@app.route('/')
def greet_user():
    return "Hello, Welcome to the Flask Application!"

if __name__ == '__main__':
    app.run(debug=True)
