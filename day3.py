#let work on simple case study simple interest Calculator


customer_name = input("Enter customer name: ")
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest
#calculate S.I
print("----------------")
print("Customer Name:", customer_name)
print("Principal Amount:", principal)
print("Simple Interest:", simple_interest)
print("Total Amount:", total_amount)
print("----------------")
