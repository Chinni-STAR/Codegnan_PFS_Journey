def add(a,b):
    return a+b

def mul(r,m):
    return r*m

def sub(a,b):
    return a-b

name="python is a programming"

n=40

def prime(n,c):
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return "prime"          #print("prime")
    else:
        return "not prime"      #print("not prime")




