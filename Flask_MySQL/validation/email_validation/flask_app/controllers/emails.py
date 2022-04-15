from flask import render_template, redirect, request, flash
from flask_app import app
from flask_app.models.email import Email

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_email', methods=['POST'])
def create_comment():
    # print(request.form)
    if not Email.valid_email(request.form):
        # print("redirecting")
        return redirect('/')
    # print("not redirecting")

    if request.form['email'] in [d.email for d in Email.get_all()]:
        flash(f"{request.form['email']} already in database!")
        return redirect('/')
    flash("I consider this an absolute win")
    cID = Email.save(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    data = Email.get_all()
    return render_template("result.html", data = data)

@app.route('/delete/<int:id>')
def delete(id):
    data = {'id' : id}
    Email.del_one(data)
    return redirect('/success')

@app.errorhandler(404)
def fourZeroFour(err):
    return "Sorry! No response. Try again, ya dingus"