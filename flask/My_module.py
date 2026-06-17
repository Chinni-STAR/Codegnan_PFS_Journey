from flask import Flask, render_template
import random
app = Flask(__name__)

#Home page
@app.route("/")
def home():
    return '''
<h1>Welcome to Home Page
<h3>Available URL's:</h3>
<url>
    <li> <a href = '/about'> About Page </a> </li>
    <li> <a href = '/Contact'> Contact Page </a> </li>
    <li> <a href = '/generated_otp'> OTP generation page </a> </li>
    <li> <a href = '/student/teja'>Dynamic URL</a> </li>
    <li> <a href = '/dashboard'> Dashboard </a> </li>
'''

@app.route("/about")
def about():
    generated_otp = random.randint(1000, 9999)
    return render_template("about.html", otp_number=generated_otp)

@app.route("/contact")
def contact():
    return '''
<p> contact </p>
'''

@app.route("/student/{name}")
def name():
    return f"Welcome {name}"

@app.route("/generated_otp")
def otp():
    generated_otp = random.randint(1000, 9999)
    return f"Your OTP is {generated_otp}"
app.run(debug = True)