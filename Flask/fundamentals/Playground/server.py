from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html", level=3, color="blue")

@app.route('/play/<int:level>')
def playLevel(level):
    return render_template("index.html", level=level, color="blue")

@app.route('/play/<int:level>/<string:color>')
def playLevelColor(level, color):
    return render_template("index.html", level=level, color=color)

@app.errorhandler(404)
def fourZeroFour(err):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)