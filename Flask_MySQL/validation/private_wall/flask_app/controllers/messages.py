from flask import render_template, redirect, request
from flask_app import app, Bcrypt, flash, session
from flask_app.models.message import Message
from flask_app.models.user import User

## Toggle to run all debug statements to track data flow
## True = On, False = Off
debug = True

bcrypt = Bcrypt(app)

# # Landing Page / Dashboard / Logged In
@app.route('/wall')
def wall():
    if debug:
        print(f"Session while attempting to access success: {session}")
    if not 'logged_in' in session:
        flash("Please login before continuining.", "login")
        return redirect ('/')
    data = {'id' : session['user_id']}
    messages = User.get_user_with_messages(data)
    if debug:
        print(f"Messages: {messages}")
    mLen = len(messages)
    return render_template("wall.html", messages = messages, mLen = mLen)

@app.route('/msg/create',methods=['POST'])
def create_msg():
    if debug:
        print(f"Request Form dict: {request.form}")
    Message.save(request.form)
    return redirect('/success')

# ! ///// DELETE //////
@app.route('/msg/destroy/<int:id>')
def destroy(id):
    data ={ 'id': id }
    Message.destroy(data)
    # Redirect show all or index?
    return redirect('/models')