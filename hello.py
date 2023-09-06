from flask import Flask, render_template

#Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

#def index():
#	return "<h1>Pozdrav Vedran!!!!</h1>"

def index():
	first_name = "Vedran"
	stuff = "This is <strong>Bold</strong> Text"
	return render_template("index.html", first_name = first_name, stuff = stuff)	

# localhost:5000/user/vedran
@app.route('/user/<name>')

def user(name):
	return render_template("user.html", user_name=name)	

# Create Custom Error Pages


# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
		return render_template("404.html"), 404	


# Internal Server Error URL
@app.errorhandler(500)
def page_not_found(e):
		return render_template("500.html"), 500			