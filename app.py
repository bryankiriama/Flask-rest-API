from flask import Flask, jsonify
from models import db, User, Post

app = Flask(__name__)

@app.route('/')
def index():
    return f"<h1>Welcome to the Flask App!</h1>"

if __name__ == '__main__':
    app.run(port=5500, debug=True)