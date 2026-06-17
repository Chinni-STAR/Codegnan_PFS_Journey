from flask import Flask, render_template, request

app = Flask(__name__)

# Store user data temporarily
users = {}

# ==============================
# HOME ROUTE
# ==============================
@app.route('/')
def home():
    return "Welcome to Simple Notes Manager"

# ==============================
# USER REGISTRATION ROUTE
# ==============================
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        # Store user data
        users[username] = password

        return f"User {username} Registered Successfully"

    return render_template('register.html')

# ==============================
# RUN APPLICATION
# ==============================
if __name__ == '__main__':
    app.run(debug=True,port=8000)