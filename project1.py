import re
def validate_name(name):
    pattern=r'^[A-Za-z]{3,}$'
    return re.fullmatch(pattern,name)
def validate_email(email):
    pattern=r'[\w\.-]+@[\w\.-]*\-\*+$'
    return re.fullmatch(pattern,email)
def validate_phone(phone):
    pattern=r'^[0-9]{10}$'
    return re.fullmatch(pattern,phone)
def validate_password(password):
    pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.fullmatch(pattern,password)

def main():
    name=input("Enter Name:")
    email=input("Enter Email:")
    phone=input("Enter Phone Number:")
    password=input("Enter Password:")

    if not validate_name(name):
        print("Invalid name")
    elif not validate_email(email):
        print("Invalid email")
    elif not validate_phone(phone):
        print("Invalid phone number")
    elif not validate_password(password):
        print("Invalid Password")
    else:
        print("All inputs are valid! for submitted successfully")

if __name__=="__main__":
    main()
    
