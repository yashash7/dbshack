from flask import Flask, render_template, request, redirect
import db
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("login.html")
@app.route('/', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    mydb = db.database()
    user = mydb.get_user()
    if user[0][0]==username and user[0][1]==password:
        return redirect('/dashboard')
    else:
        return render_template('login.html', message="Incorrect Username or Password, please login again!")
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/hnipage')
def hnipage():
    return render_template('hnipage.html')    

@app.route('/wmrequest')
def wmrequest():
    return render_template('wmpage.html')

if __name__ == '__main__':
    app.run(debug=True)