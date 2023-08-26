"""
magical number
recursively the sum of digits is 1
its like a happy number
"""

def sum_digits(num):
    sum1=0
    while(num>0):
        rem=num%10
        sum1=sum1+rem
        num=num//10
    print(sum1)
    return sum1


n=int(input("enter the number"))
m=n

while(True):
    a=sum_digits(n)
    if a==1:
        print(m , "is a magical number")
        break
    elif len(str(a))==1:
        print(m , "is not a magical number")
        break
    else:
        n=a
        
