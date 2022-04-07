from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

@app.route('/')
def index(users=users):
    return render_template("index.html", users=users)

# @app.route("/")
# @app.route("/index")
def index():
	return render_template("index2.html")

@app.errorhandler(404)
def fourZeroFour(err):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)