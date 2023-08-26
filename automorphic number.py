# auto morphic number the square of the number end with the same number

n=int(input("enter the number"))
x=n
m=n**2
t=10
flag=0
r=0
while(r<x):
    r=m%t
    if r==x:
        flag=1
        break
    t=t*10
if flag==0:
    print(x," is not a automorphic number")
else:
     print(x," is a automorphic number")

    
