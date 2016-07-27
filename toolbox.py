from flask import Flask, render_template
app = Flask(__name__)

#users =
#[
#    {
#	}
#]

@app.route('/')
def index():
  return render_template('index.html')

 #, users=users)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html')

if __name__ == '__main__':
  app.run(debug=True)