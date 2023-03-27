from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))

    def create_db():

@app.before_first_request
def create_db():
    db.create_all()

    user1 = User(name='John', email='john@example.com')
    db.session.add(user1)

    post1 = Post(title='My first post', content='This is my first post', user=user1)
    post2 = Post(title='My second post', content='This is my second post', user=user1)
    db.session.add(post1)
    db.session.add(post2)

    db.session.commit()


@app.route('/')
def index():
  posts = Post.query.all()
  return render_template('index.html', posts=posts )


@app.route('/about')
def about():
  return render_template('about.html' )



@app.route('/contact')
def contact():
  return render_template('contact.html' )








