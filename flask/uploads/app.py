'''
WEB:
---
-->(www)is used url to show the web application(to generate url that is called as web app)
-->(WWW)the world wide web is a collection of websites and webpages connected through the network where user can access these websites
using web browsers.

Web Browser
-----------
-->A web browser is a software used to access and display webpages


Web Server
----------
-->A web server stores websites files and sends webpages to users when they request through a browser...

Web application
---------------
-->A web application is a software that runs and sends inside a browser and allows user to interact with data and server online.
'''
'''
from flask import Flask

app=Flask(__name__)
@app.route('/')
def home():
    return "Welcome to Flask Application"

if __name__=='__main__':
    app.run(debug=True)
'''
'''
Flask
------
-->flask is lightweight web frame used to build web applications using python
-->is also a micro web framework
'''
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask App</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(to right, #1e3c72, #2a5298);
                font-family: Arial, sans-serif;
            }

            .container {
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                text-align: center;
            }

            h1 {
                color: #1e3c72;
                margin-bottom: 10px;
            }

            p {
                color: #555;
                font-size: 18px;
            }

            button {
                margin-top: 20px;
                padding: 10px 20px;
                border: none;
                background-color: #1e3c72;
                color: white;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
            }

            button:hover {
                background-color: #16325c;
            }
        </style>
    </head>
    <body>

        <div class="container">
            <h1>Welcome to Flask Application</h1>
            <p>Your Flask app is running successfully 🚀</p>
            <button>Get Started</button>
        </div>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
'''
'''
Routing,url_for(),Redirects and URL converters


url_for()
---------
-->This flask function used to dynamically generate URLs  for routes in the Flask
-->this avoids hardcoding for URLs
-->Automatically updates URLs if route changes

syntax--> url_for('function_name')

from flask import Flask,url_for
app=Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/about')
def about():
    return url_for('home')
if __name__=='__main__':
    app.run(debug=True)

#Dynamic Routing
----------------
URL--> http://127.0.0.1:5000
-->the dynamic routing means passing values through the URL, Flask allows URLs to accept variables...

from flask import Flask,url_for
app=Flask(__name__)
name='Chinni'

@app.route('/')
def home():
    return f"Welcome {name}"

@app.route('/student/<name>')
def student(name):
    return f"Welcome {name}"
if __name__=='__main__':
    app.run(debug=True)


Static Route
------------
--> Fixed URL
-->No parameters
--> same output

Dynamic route
-------------
-->Variable URL
-->Accept parameters

'''
'''
redirect()
----------
// it move one page to another page is called as redirect
// 

from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return "Login Page"

if __name__=='__main__':
    app.run(debug=True)
'''

'''
URL converters
---------------
1. Int converter
'''
'''
from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/marks/<int:score>')
def marks(score):
    return f"marks={score}"

@app.route('/')
def home():
    return redirect(url_for('marks',score=67))

if __name__=='__main__':
    app.run(debug=True)
'''
'''
2.float Converter

from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/price/<float:Bill>')
def price(Bill):
    return f"price={Bill}"

@app.route('/')
def home():
    return redirect(url_for('price', Bill=67))

if __name__=='__main__':
    app.run(debug=True)
'''

'''
3.UUID Converter

from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/user/<uuid:user_id>')
def user(user_id):
    return f"user ID={user_id}"

@app.route('/')
def home():
    return redirect(url_for('user',user_id="123e4567-e89b-12d3-a456-426614174000"))

if __name__=='__main__':
    app.run(debug=True)
'''

'''
HTTP Request Methods
--------------------

This HTTP request methods are used for communication between a client(browser/app) and a server in web development and
APIs

1.GET request
-------------
-->A Get request  is used to retrive data from the server

from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "This is GET Request"

if __name__ == '__main__':
    app.run(debug=True)


2.POST Request
--------------

from flask import Flask, request, url_for
app = Flask(__name__)

@app.route('/')
def submit():
    return 
    <form action='/submit', methods=['POST'>
    <input type='text' name='name' placeholder='chinni'>
    <input type 
    
if __name__ == '__main__':
    app.run(debug=True)
'''  

'''
get - this get request is used to retrieve the data from the server
        data is visible 
        
post - post request is used to send data to the server
put - used to update the existing data on the server in the server
delete - used to delete required data from the server


control structures:

In control structures,what we write to use these symblos "{% %}"

1.condition

example
-------
{% if marks >= 35 %}
    <h2>Pass</h2>
{%else%}
    <h2>fail</h2>
{% end if%}
2.loops

example
-------
{% for item in subjects %}
    <p>{{item}}</p>
{% end for%}

Template Inheritance
--------------------
-->This allows one HTML file to reuse another HTML file

GET--->request.args.get
-----------------------
-->values throught URL

POST--->requests.form
---------------------
-->data submitted from HTML

JSON data--> request.get_json()
------------------------------
The structure data sent in API request

Authenticating user Registration
--------------------------------
-->Authenticating in user Registration that means verifying that a user is genuine before allowing to an application

SMTP(Simple mail transfer protocol)
-->It is used to send mail over the network
-->to used this have to import(smtplib)

EmailMessage
------------
-->This is a class from python's email message

Tokenization
------------

Constructor  parameters
-----------------------
-->secret_key which is used for encrypting tokens
-->salt where this is additional layer for security

Database
-----------

-->Notes
-->Uploading files
-->Authentication files

Using mysql.connector
---------------------
-->This is used to

import mysql.connector


Login Validation
-----------------
-->This login validation is the process of verifying whether the username or email and password entered by a user are correct or not

-->Authenicates users
-->prevent unauthorized users

Session
-------
-->A session is a serverside storage mechanism used to store user-specific information across multiple requests

Why it is needed?
----------------
Eg: session['username]='admin'
-->The normal HTTP is a stateless protocol,which means it does not remember previous request,but the sessions help maintain user information 
while they navigate through the application

types
-----
-- Client-side sessions
   --------------------
   -->The data stored in user's browser
   
-- Server-side sessions
   --------------------
   -->The data stored in the server
   
Jinja Template inheritance
--------------------------
-->The templates inheritance allows multiple HTML pages to share a common layout

session cookies
---------------
-->Deleted when the browser is closed
-->Client side sessions
'''











