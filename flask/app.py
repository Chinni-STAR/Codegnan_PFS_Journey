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


