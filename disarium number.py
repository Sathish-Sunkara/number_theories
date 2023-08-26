"""
sum of its digits raised to the powers of their respective positions equals to that number
"""

n=int(input("enter the number?"))
m=n
sum1=0
for i in range(len(str(n))):
    sum1+=(int(str(n)[i])**(i+1))
if sum1==m:
    print("the "+str(m)+" is a disarium number")
else:
    print("the "+str(m)+" is not a disarium number")

    
