from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "@_xxV9deAbYzhHU7DT_C" #generated by password gen

debug = False

@app.route('/')
def index():
    if 'leaderboard' not in session:
        session['leaderboard'] = {}
    if 'rand' not in session:
        num = random.randint(1,100)
        session['rand'] = num
        session['color'] = 'red'
        session['guesses'] = 0
        session['guess'] = 0 # below all possible values
        if debug:
            print(session['rand'], type(session['rand']))
    if debug:
        print(session)
    return render_template("index.html",
    num=session['rand'], guess=session['guess'], guesses=session['guesses'], color=session['color'])

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess']) if request.form['guess'] else 0
    if debug:
        print(guess, type(guess))
    session['guesses'] += 1
    session['guess'] = guess
    if guess == session['rand']:
        return redirect('/correct')
    return redirect('/')

@app.route('/correct')
def correct():
    session['color'] = 'green'

    return redirect('/')

@app.route('/winner', methods=['POST'])
def winner():
    session['leaderboard'][request.form['username']] = session['guesses']
    return redirect('/reset')

@app.route('/reset')
def reset():
    sKeys = list(session.keys())
    for k in sKeys:
        if k != 'leaderboard':
            session.pop(k)
    return redirect('/')

@app.route('/leaderboard')
def leaderboard():
    sorted_LB = sorted(session['leaderboard'].items(), key=lambda x:x[1])
    return render_template("leaderboard.html", lb=sorted_LB)

@app.errorhandler(404)
def fourZeroFour(err):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)