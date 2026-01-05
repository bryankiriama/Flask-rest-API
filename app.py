from flask import Flask, jsonify , make_response
from models import *
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rest-api.db'

Migrate(app, db)
db.init_app(app)

api = Api(app)

class Userresource(Resource):
    def get(self, user_id):
        return ([user for user in User.query.all()], 200) # compresing to list

    def post(self):
        data = request.get_json()
        new_user = User(
            username=data['username'],
            email=data['email']
        )
        db.session.add(new_user)
        db.session.commit()
        return make_response((new_user), 201)



@app.route('/')
def index():
    return f"<h1>Welcome to the Flask App!</h1>"

if __name__ == '__main__':
    app.run(port=5500, debug=True)