ICICI_chinni_AC_Details = {"Name" : "Chinni",
                           "ATM PIN" : "4466",
                           "Balance" : 8000}
user_pin = input("Pls enter your 4 digits ATM Pin:")
if len(user_pin) == 4:
    if user_pin in ICICI_chinni_AC_Details['ATM PIN']:
        user_choice=int(input("enter \n1.WithDraw: \n2.Deposite \n3.Pin Change "))
        if user_choice==1:
            money_w=int(input("enter money you want to withdraw:"))
            if money_w<= ICICI_chinni_AC_Details['Balance']:
                ICICI_chinni_AC_Details['Balance']-=money_w
                print(ICICI_chinni_AC_Details['Balance'])
            else:
                print("insufficient")
        elif user_choice==2:
             Deposite_m = int(input("plz enter the money you want to deposite: "))
             if Deposite_m % 100 == 0 and Deposite_m >=5000:
                 ICICI_chinni_AC_Details["Balance"]+=Deposite_m
                 print(f"you have depostied {Deposite_m} and the total ammount is {ICIC_chinni_AC_Details["Balance"]}")
             else:
                 print(f"{Deposite_m} you have entered is change or less than given amount {5000}")
        elif user_choice ==3:
             old_pin=input("pls enter your old pin")
             if old_pin in ICICI_chinni_AC_Details["ATM PIN"]:
                 new_pin=input("Enter new ATM PIN: ")
                 if new_pin !=old_pin:
                     ICICI_chinni_AC_Details ["ATM PIN"] = new_pin
                     print("Your ATM pin updated succesfully")
                     attempts_remaining==3
                     while attempts_remaining > 0:
                         old_pin = input("Enter your old ATM PIN: ")
                         if len(old_pin)==4:
                             if old_pin in user_choice["ATM PIN"]:
                                 pin_change = input("Enter a new 4 digits ATM PIN: ")
                                 user_choice["ATM PIN"]=pin_change
                                 print("new pin is updated")
                             else:
                                 print("you entered pin is incorrect")
                         else:
                            print("Enter correct number")
    else:
        print("You have entered invalid pin")
else:
    print("You entered invalid pin")
