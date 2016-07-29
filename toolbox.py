from flask import Flask, render_template, redirect, url_for, request, session
from sqlalchemy import create_engine
from database_setup import Base, User
from sqlalchemy.orm import scoped_session, sessionmaker
import hashlib

engine = create_engine('sqlite:///flasky.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSessionMaker = sessionmaker(bind=engine)
dbSession = DBSessionMaker()

#DBSession = scoped_session(sessionmaker())
app = Flask(__name__)
app.secret_key = 'super secret string'

def hash_password(password):
	return hashlib.md5(password.encode()).hexdigest()

def validate(email, password):
	query = DBSession.query(User).filter(User.email.in_([email]),User.password.in_([hash_password(password)]))
	return query.first() != None




@app.route('/')
def home():
	print('home')
	email = session.get('email')
	if not email:
		return render_template('index.html')
	else:
		user=DBSession.query(User).filter_by(email = email).first()
		return render_template('blank.html',user = user)

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def validate(email, password):
    query = dbSession.query(Person).filter(
        Person.email.in_([email]),
        Person.hashed_password.in_([hash_password(password)])
    )



@app.route('/signin', methods=['GET', 'POST'])
def signin():
	error = None
	if request.method == 'POST':
		email = str(request.form['email'])
		password = str(request.form['pwd'])
		is_valid = validate(email, password)
		if is_valid == False:
			error = 'Invalid credentials. Please try again.'
		else:
			session['email'] = email
			return redirect(url_for('home'))
	session['email'] = None
	return render_template('subjectspage.html', error = error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		new_username = request.form['name']
		new_email = request.form['email']
		new_password = hash_password(request.form['pwd'])
		new_password2 = hash_password(request.form['pwd2'])
		if (new_password == new_password2):
			new_user= User(name=new_name,email=new_email,password=new_password)
			DBSession.add(new_user)
			DBSession.commit()
			print('after commit')
			session['email'] = new_email
			return redirect(url_for('home'))
		else:
			print('fail')
			return render_template('index.html')


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/subjects')
def subjects():
  return render_template('subjectspage.html')

@app.route('/trigolevelsmenu')
def trigolevelsmenu():
  return render_template('trigolev.html')

 #, users=users)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html')

if __name__ == '__main__':
  app.run(debug=True)
