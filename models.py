from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#models
class User(db.Model):
    __tablwename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)  # Post title
    content = db.Column(db.Text, nullable=False)       # Post content
    post_image = db.Column(db.String(200), nullable=True)  # Optional image


        # Foreign key to link to User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)