from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from database_setup import User, Base
import hashlib

app = Flask(__name__, static_url_path='/static')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"


engine = create_engine('sqlite:///flasky.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSessionMaker = sessionmaker(bind=engine)
dbSession = DBSessionMaker()


# db = SQLAlchemy(app)

# class user(db.Model):
# 	id = db.Column('user_id', db.Integer, primary_key = True)
# 	name = db.Column(db.String(100))
# 	email = db.Column(db.String(50))  
# 	password = db.Column(db.String(200))

# db.create_all()

# def __init__(self, name, email, password):
# 	self.name = name
# 	self.email = email
# 	self.password = password


def hash_password(password):
	return hashlib.md5(password.encode()).hexdigest()

def validate(email, password):
	print('email: ', email)
	print('password: ', password)
	query = dbSession.query(User).filter(User.email.in_([email]),User.password.in_([hash_password(password)]))
	print('is valid ', None != query.first())
	return query.first() != None




@app.route('/')
def home():
		return render_template('index.html')

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

@app.route('/subjects2', methods=['GET', 'POST'])
def subjects2():
	error = None
	if request.method == 'POST':
		email = str(request.form['email'])
		password = str(request.form['password'])
		is_valid = validate(email, password)
		print (is_valid)
		if False == is_valid:
			error = 'Invalid credentials. Please try again.'
			session['email'] = None
			return render_template('index.html', error = error)
		else:
			session['email'] = email
			session['password'] = password
			return render_template('subjectspage.html')


@app.route('/subjects', methods=['GET', 'POST'])
def subjects():
	print("entered subjects")
	if request.method == 'GET':
		print("In the get method")
		return render_template('subjectspage.html')
	else:
		print("in the else")
		new_name = request.form['name']
		new_email = request.form['email']
		print("New name:" + str(new_name))
		new_password = hash_password(request.form['password'])
		new_password2 = hash_password(request.form['password2'])
		if (new_password == new_password2):
			print("creating new user")
			new_user= User(name=new_name,email=new_email,password=new_password)
			print('new user')
			dbSession.add(new_user)
			dbSession.commit()
			session['email'] = new_email
        
			flash('Record was successfully added')
			return render_template('subjectspage.html')

		else:
			print('fail')
			return render_template('index.html')


@app.route('/trigolevels')
def trigolevels():
  return render_template('trigolev.html')

@app.route('/profile')
def profile():
  return render_template('profile.html')


@app.route('/subjectspage')
def subjectspage():
  return render_template('subjects.html')


@app.route('/explaination')
def explaination():
  return render_template('explaination.html')


@app.route('/questionone')
def questionone():
  return render_template('questionone.html')


@app.route('/congrats')
def congrats():
  return render_template('congrats.html')


@app.route('/questone')
def questone():
  return render_template('questone.html')

@app.route('/sing_out')
def sing_out():
  return render_template('index.html')

@app.route('/show_all')
def show_all():
   return render_template('show_all.html', users = dbSession.query(User).all() )

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html')

if __name__ == '__main__':
  app.run(host= '0.0.0.0', debug=True)
