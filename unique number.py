"""
unique number
 the digits in that number are unique
 """
n=int(input("enter the number"))
flag=0
for ele in str(n):
    if (str(n)).count(ele)>1:
        flag=1
        break
if flag==1:
    print( n , "is not a unique number")
else:
    print( n , "is a unique number")

