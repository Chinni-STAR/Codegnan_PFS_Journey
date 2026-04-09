'''
Recursion functions--

Recursion is a programming technnique where a function calls itself either directly or indirectly to
solve a problem by breaking it into smaller,simpler subproblems.
recursion especially useful for problems that can be divided into identical smaller tasks, such as
mathematical calculations,tree traversals orr divide and conquer algorithms.
'''
'''
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
fibonacci(num)
'''
'''
def validatepin(self):
    while self.remaining_attempts>0:
        userpin=input("enter 4 digit pin:")
        if len(userpin) ==4 and userpin == self.user_in["ATM Pin"]:
            print("welcome to the ATM")
            return True
        else:
            self.remaining_attempts -=1
            if self.remaining_attempts>0:
                print(f"invalid pin.attempts left:{self.remaining_attempts}")
            else:
                print("card blocked.please contact customer service")
                return False
'''
'''
a="python is a programming language"
vowel=[]
const=[]
space=''
def Vowe_con(a,vowel,const,space):
    for i in a:
        if i in "aeiouAEIOU":
            vowel.append(i)
        elif space == i:
            space.remove(i)
        else:
            const.append(i)
    print(vowel)
    print(const)
Vowe_con(a,vowel,const,space)

'''
n=2
count=0
def primecheck(n,count):
    for i in range(1,n+1):
        if n%i == 0:
            count=count+1
if count==2:
    print("prime")
else:
    print("not prime")
primecheck(n,count)



