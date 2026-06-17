""" from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        if username=="chinnimusirana" and password=="1234567":
            return "Login successful"
        else:
            return "Invalid credentials"
    return render_template("login.html")
app.run(debug=True)
"""
""" from flask import Flask,session
app=Flask(__name__)
app.secret_key="mysecretkey"
@app.route("/")
def login():
    session["username"]='chinni'
    session["password"]='12344'
    return "session created"
app.run(debug=True) """
""" from flask import Flask,session
from datetime import datetime,timedelta
app=Flask(__name__)
app.secret_key="mysecretkey"
app.permanent_session_lifetime=timedelta(minutes=1)
@app.route("/")
def login():
    session.permanent=True
    session["username"]='chinni'
    session["password"]='12344'
    return "session created"
app.run(debug=True)  """


