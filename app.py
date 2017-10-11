from flask import Flask, render_template, request, session, redirect, url_for, flash
import os 

app = Flask(__name__)
app.secret_key = os.urandom(32)

username = 'username'
password = 'password'

@app.route('/')
def root():
    if session.has_key('user'):
        return redirect( url_for('welcome') )
    else: 
        return render_template('form.html')

@app.route('/verify', methods = ['POST','GET'])
def verify():
    userIn = request.form['user']
    passIn = request.form['pass']
    if userIn == username:
        if passIn == password:
            session['user'] = request.form['user']
            flash('Login Successful')
            return redirect( url_for('welcome') )
        else:
            flash('Incorrect password. Please try again.')
            return redirect( url_for('root') )
    else:
        flash('Incorrect username. Please try again')
        return redirect( url_for('root') )
    
@app.route('/welcome', methods = ['POST', 'GET'])
def welcome():
    return render_template('welcome.html', user = session['user'])

@app.route('/logout', methods = ['POST', 'GET'])
def logout():
    session.pop('user')
    flash('Logged Out')
    return redirect( url_for('root') )

if __name__ == '__main__':
    app.debug = True
    app.run()
