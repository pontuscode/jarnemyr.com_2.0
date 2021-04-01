from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')
	
	
@app.route('/projects', methods=['GET'])
def projects():
	return render_template('projects.html')
	
	
@app.route('/contact', methods=['GET'])
def about():
	return render_template('contact.html')


@app.route('/projects/arbitrage', methods=['GET'])
def arbitrage():
	return render_template('/projects/arbitrage.html')


@app.route('/projects/lending-tracker', methods=['GET'])
def lending_tracker():
	return render_template('/projects/lending-tracker.html')
	

@app.route('/projects/portfolio-tracker', methods=['GET'])
def portfolio_tracker():
	return render_template('/projects/portfolio-tracker.html')

if __name__ == '__main__':
	app.run(debug=True)
