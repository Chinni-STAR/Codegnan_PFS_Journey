""" 
Forgot password
---------------
-->A Forgot password feature allows users to reset their password if they have forgotten it and cannot remember it. 
#This typically involves sending a password reset link or OTP (One-Time Password) to the user's registered email address or phone number. 
#The user can then use this link or OTP to create a new password and regain access to their account.

-->Instead of showing the old password,the application sends a secure passeword reset link or OTP to the user's registered email address or phone number.
"""
""" from flask import Flask, request, render_template,flash
app = Flask(__name__)
app.secret_key = "secret_key"
@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():  
    if request.method == 'POST':
        email = request.form['email']
        # Here you would typically check if the email exists in your database
        # and send a password reset link or OTP to the user's email address.
        flash('Password reset link has been sent to your email address.')
    return render_template('forgot_password.html')
if __name__ == '__main__':
    app.run(debug=True) """
    
""" 
Token Generation
----------------
-->The flask application commmonly use the itsdangerous library to generate secure tokens for password reset links or OTPs.

from itsdangerous import URLSafeTimedSerializer
token = serializer.dumps(email, salt='password-reset-salt')

#salt is additional layer of security that helps protect against certain types of attacks, such as token forgery.

Token Validation
----------------
-->When a user clicks on the password reset link or enters the OTP, the application validates the token to ensure it is valid and has not expired.

email = serializer.loads(token, salt='password-reset-salt', max_age=600) #600 seconds = 10 minutes
#NOTE: max_age is the time limit for the token to be valid, typically set to a few minutes for security reasons.
"""
