from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def send_to_dojos():
    return redirect("/dojos")

@app.route('/dojos')
def index():
    dojos = Dojo.get_all()

    return render_template("index.html", dojos = dojos)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name" : request.form["name"],
    }
    Dojo.save(data)

    return redirect("/")

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    data = {
        "first_name" : request.form["first_name"],
        "last_name"  : request.form["last_name"],
        "age"        : request.form["age"],
        "dojo_id"    : request.form["dojo_id"]
    }
    Ninja.save(data)

    return redirect(f"/dojos/{data['dojo_id']}")

@app.route('/add_ninja')
def add_ninja():
    dojos = Dojo.get_all()

    return render_template("add_ninja.html", dojos = dojos)

@app.route('/dojos/<int:x>')
def edit(x):
    data = {'id' : x}
    one_dojo  = Dojo.get_dojo_with_ninjas(data)
    print(one_dojo)
    return render_template("dojo.html", dojo=one_dojo)

# @app.route('/update/<int:x>', methods=["POST"])
# def update(x):
#     data = {
#         "fname" : request.form["fname"],
#         "lname" : request.form["lname"],
#         "email" : request.form["email"],
#         "id"    : x
#     }
#     User.update(data)
#     return redirect(f'/users/{x}')

# @app.route('/users/<int:x>/destroy')
# def del_user(x):
#     data = {'id' : x}
#     User.del_one(data)
#     return redirect("/")