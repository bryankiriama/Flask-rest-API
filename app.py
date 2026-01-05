from flask import Flask, jsonify
from models import *
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rest-api.db'

Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return f"<h1>Welcome to the Flask App!</h1>"

if __name__ == '__main__':
    app.run(port=5500, debug=True)