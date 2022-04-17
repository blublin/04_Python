from flask import render_template, redirect, request
from flask_app import app, Bcrypt, flash, session
from flask_app.models.user import User

## Toggle to run all debug statements to track data flow
## True = On, False = Off
debug = True

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('index.html')

# TODO REGISTER USER WITH VALIDATION
@app.route('/register/create', methods=['POST'])
def create():
    if debug:
        print(f"Request Form dict: {request.form}")
    if not User.validate_model(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    if debug:
        print(f"Password Hash: {pw_hash}")
    # Ensure data keys are correct
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    if debug:
        print(f"Registration data dict: {data}")
    user_id = User.save(data)
    # Add user to session
    session['user_id'] = user_id
    session['first_name'] = data['first_name']
    session['logged_in'] = True
    # ! Auto login after registration, go to dashboard? main page?
    return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
    data = { 'email' : request.form['email'] }
    user = User.get_by_email(data)
    if debug:
        print(f"Request Form dict: {request.form}")
        print(f"Hashed password: {user.password}")
        print(f"Entered password: {request.form['password']}")

    if not ( User.valid_email(data) and User.email_in_db(data) ):
        # De Morgans Law:
        # (not A) or (not B) == not (A and B)
        flash("Invalid credentials")
        return redirect('/')
    elif not bcrypt.check_password_hash(user.password, request.form['password']):
        # check pw (hashed, unhashed)
        flash("Invalid Email/Password")
        return redirect('/')
    else:
        session['user_id'] = user_id
        session['first_name'] = data['first_name']
        session['logged_in'] = True
        return redirect('/success')

@app.route('/success')
def success():
    data = User.get_all()
    return render_template("result.html", data = data)

@app.route('/delete/<int:id>')
def delete(id):
    data = {'id' : id}
    User.del_one(data)
    return redirect('/success')

@app.errorhandler(404)
def fourZeroFour(err):
    return "Sorry! No response. Try again, ya dingus"