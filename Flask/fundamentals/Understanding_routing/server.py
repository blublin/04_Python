from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def hiName(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return f"{word * num}!"

@app.errorhandler(404)
def fourZeroFour(err):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.