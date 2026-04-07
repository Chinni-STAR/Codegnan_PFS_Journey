
prime_num = int(input("enter the number"))
count = 0
for j in range(1, prime_num+1):
    if prime_num % j == 0:
        count += 1
        print(count)
if count == 2:
    print(f"{prime_num} is a prime number")
else :
     print(f"{prime_num} is not a prime number")
'''
for an in range(2,10):
    count = 0
    for j in range(1,an+1):
        if an % j == 0:
            count += 1
    if count == 2: 
        print(f"{an} is a prime number")
    else :
        print(f"{an} is not a prime number")         

for an in([1057,197,9,86,17673]):
    count = 0
    for j in range(1,an+1):
        if an % j == 0:
            count += 1
    if count == 2: 
        print(f"{an} is a prime number")
    else :
        print(f"{an} is not a prime number")

any = [2,356,8,3,2,8]
empty_ = []
for j in any:
    if j not in empty_:
        empty_.append(j)
        print(empty_)
        
any = [2,356,11,19,8,3,2,8,11,125,19]
empty_ = []
for j in any:
    if j not in empty_:
        empty_.append(j)
    print(any)    

so = 153
length_ = len(str(so))
amstr_ = 0
for j in str(so):
    amstr_ += int(j) ** length_
    print(amstr_)
if amstr_ == so:
    print(f"{so} is amstrong num")
else:
    print(f"{so} is not amstrong num")
'''

'''
take a list only with int in which even numbers should be separate,
odd num separated
'''
