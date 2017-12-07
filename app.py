from flask import *

app = Flask(__name__)

@app.route('/')
def welcome():
	return render_template('welcome.html')

@app.route('/game')
def game():
	return render_template('index.html')

if (__name__ == '__main__'):
	app.run(port=33333)
