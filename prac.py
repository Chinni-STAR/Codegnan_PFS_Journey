ICICI_chinni_AC_Details = {"Name" : "Chinni",
                           "ATM PIN" : "4466",
                           "Balance" : 8000}
user_pin = input("Pls enter your 4 digits ATM Pin:")
if len(user_pin) == 4:
    if user_pin in ICICI_chinni_AC_Details['ATM PIN']:
        user_choice=int(input("enter \n1.WithDraw: "))
        if user_choice==1:
            money_w=int(input("enter money you want to withdraw:"))
            if money_w<= ICICI_chinni_AC_Details['Balance']:
                ICICI_chinni_AC_Details['Balance']-=money_w
                print(ICICI_chinni_AC_Details['Balance'])
            else:
                print("insufficient")
else:
    print("You entered invalid pin")
