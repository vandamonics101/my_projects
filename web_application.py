from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello Everyone. This is my first Web Application'

if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1')
