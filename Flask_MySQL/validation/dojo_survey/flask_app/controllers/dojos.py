from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_comment', methods=['POST'])
def create_comment():
    print(request.form)
    if not Dojo.validate_comment(request.form):
        print("redirecting")
        return redirect('/')
    print("not redirecting")

    cID = Dojo.save(request.form)
    data = {'id' : cID}
    comment = Dojo.get_one(data)
    print(comment)
    return render_template('result.html', comment = comment)

@app.route('/register', methods=['POST'])
def register():
    if not Dojo.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    return redirect('/dashboard')

@app.errorhandler(404)
def fourZeroFour(err):
    return "Sorry! No response. Try again, ya dingus"