from flask import Flask, render_template
from threading import Thread
import os

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/login')
def login():
	return render_template('login.html', title='Login')


@app.route('/signup')
def signup():
	return render_template('signup.html', title='Sign-up')


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	run = app.run(debug=True, host='0.0.0.0', port=port)
	Thread(target=run).start()
