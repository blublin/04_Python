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

    users = User.get_all()
    you = User.get_one(session['user_id'])
    return render_template("wall.html", messages = messages, mLen = mLen, users=users, you=you)

@app.route('/msg/create',methods=['POST'])
def create_msg():
    if debug:
        print(f"Request Form dict: {request.form}")

    msg_data = {
        'user_sent_id' : session['user_id'],
        'user_recv_id' : request.form['id'],
        'message' : request.form['message']
    }
    Message.save(msg_data)

    msg_count = User.get_one(session['user_id']).msg_sent_count
    msg_count += 1
    user_data = {
        'id' : session['user_id'],
        'msg_sent_count' : msg_count 
    }
    
    User.update(user_data)
    return redirect('/wall')

# ! ///// DELETE //////
@app.route('/msg/destroy/<int:id>')
def destroy(id):
    data ={ 'id': id }
    Message.destroy(data)
    # Redirect show all or index?
    return redirect('/models')