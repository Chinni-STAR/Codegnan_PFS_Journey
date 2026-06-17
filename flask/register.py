import otp_module

username=input("enter username: ")

otp=otp_module.generate_otp()
print("Generated OTP:",otp)
user_otp=int(input("Enter OTP:"))

if otp==user_otp:
    print("Registration Successful")
else:
    print("Invalid OTP")