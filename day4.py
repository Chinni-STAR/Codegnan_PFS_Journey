'''
statements --> these are 3 types
-Control statements
-Conditional staements/Decision making
-loop statements
'''

'''
conditional statements:
#if statement--> this(if stmt)is used to check any condition, if the condition becomes true then it will enter
in side the (if stmt)

age= int(input("enter the age:"))
if age >= 18:
    print("your age is 18 or above")

Student_att= int(input("enter the sem attendance:"))
if Student_att >= 75:
    print("you can directly enter the sem exam hall")

fee_details= int(input("enter the fees:"))
if fee_details < 50000:
    print("you need to pay the fees first")

price=int(input("enter the price:"))
if price < 900:
    print("i need to buy these dress")'''

#if-else statement -->this also called as fall back statement which only execute when the (if stmt)
#become false
'''
age=int(input("enter the age:"))
if age>=18:
    print('you can vote')
else:
    print(f'you cannot and have to wait {18-age} years')

total_amount= int(input("enter the total shopping money:"))
if total_amount >= 149:
    print("no deliver cost")
else:
    print(f"add {149-total_amount} to your cart")

hotel_rooms=int(input("enter how many rooms want:"))
if hotel_rooms <= 5:
    print("you're go to room")
else:
    print("you need to wait")'''

#if elif else statement -->(if+else)--in the elif part, i can check one more condition
'''
student_marks=int(input("enter your marks:"))
if student_marks >= 90:
    print("you got A+ grade")
elif student_marks >=75 and student_marks <90:
    print("You got A grade")
elif student_marks >=60 and student_marks < 75:
    print("you got B+ grade")
else:
    #print("you fail the exam")
    print(f"you need to score {60-student_marks} marks for pass the exam")'''

#Calculator-1
'''
n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
operator=input("enter the operation to perform:")
if operator == '+':
    print(n1+n2)
    print(f"addition of {n1} and {n2} is {n1+n2}")
elif operator == '-':
    print(n1-n2)
elif operator == '*':
    print(n1*n2)
else:
    print(n1/n2)

#using options for calculator -2
num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
user_choice=int(input("enter your choice:\n 1.ADD\n 2.SUB\n 3.MUL\n 4.DIV : "))
if user_choice == 1:
    print(num1+num2)
elif user_choice == 2:
    print(num1-num2)
elif user_choice == 3:
    print(num1*num2)
else:
    print(num1/num2)


#program
num=int(input("enter any number:"))
if num % 2==0:
    print("{num} is a even number")
else:
    print(f"{num} is odd number")'''

#program for finding positive,negative no
num=int(input("enter the number:"))
if num >=1:
    print(f"{num} is postive number")
elif num < 0:
    print(f"{num} is negative number")
else:
    print("the number is zero")






















    
