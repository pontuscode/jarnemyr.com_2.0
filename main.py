from flask import Flask, render_template, url_for

app = Flask(__name__)
MEDIA_FOLDER = "/home/pontus/flask_webserver_2.0/static/tutorial_stuff/img"


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')
	
@app.route('/projects', methods=['GET'])
def projects():
	return render_template('projects.html')
	
@app.route('/contact', methods=['GET'])
def about():
	return render_template('contact.html')
#@app.route('/sayhello', methods=["POST"])
#def sayhello():
#	return "hey man xD";


if __name__ == '__main__':
	app.run(debug=True)
