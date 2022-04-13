from flask import Flask, render_template, request, redirect, session
# import the class from friend.py
from users import User
app = Flask(__name__)

@app.route('/')
@app.route('/users')
def index():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route('/add')
def add():
    return render_template("create.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the User class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

@app.route('/users/<int:x>')
def see_user(x):
    data = {'id' : x}
    one_user  = User.get_one(data)
    print(one_user)
    return render_template("user.html", user=one_user)

@app.route('/users/<int:x>/edit')
def edit(x):
    data = {'id' : x}
    one_user  = User.get_one(data)
    print(one_user)
    return render_template("edit.html", user=one_user)

@app.route('/users/<int:x>/destroy')
def del_user(x):
    data = {'id' : x}
    User.del_one(data)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)