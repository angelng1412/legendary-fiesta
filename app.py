from flask import Flask, render_template, request, session, redirect, url_for
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
    if request.form['user'] == username and request.form['pass'] == password:
        session['user'] = request.form['user']
        return redirect( url_for('welcome') )
        #return render_template('welcome.html', user = request.form['user'])
    else:
        return redirect( url_for('error') )
    
@app.route('/welcome', methods = ['POST', 'GET'])
def welcome():
    return render_template('welcome.html', user = session['user'])

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/logout', methods = ['POST', 'GET'])
def logout():
    session.pop('user')
    return redirect( url_for('root') )

if __name__ == '__main__':
    app.debug = True
    app.run()
