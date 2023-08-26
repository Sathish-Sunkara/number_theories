#armstrong number
""" sum of the digits powers raised to the length of the number is called armstrong number"""

def is_armstrong(n):
    m=n
    s=0
    l=len(str(n))
    while(n>0):
        r=n%10
        s+=pow(r,l)
        n//=10
    if s==m:
        return 1
    else:
        return 0

    
n=int(input("enter the number"))

flag=is_armstrong(n)

if(flag==1):
    print(n , "is a armstrong number")
else:
    print(n , "is not a armstrong number")
