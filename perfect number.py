#perfect number

def is_perfect(n):
    
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    if sum(l)==n:
        return 1
    else:
        return 0
n=int(input("enter the number"))

flag=is_perfect(n)
if(flag==1):
    print(n , "is a perfect number")
else:
    print(n , "is not a perfect number")
