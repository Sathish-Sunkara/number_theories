"""
fascinating number
"""

n=int(input("enter the number"))
if len(str(n))==3:
    str1=str(n)+str(2*n)+str(3*n)
    print("indication is : "+str1)
    for num in str1:
        if len(str1)!=9 or str1.count(num) or str1.count(num)==0:
            flag=1
        else:
            flag=0

    if flag==1:
        print(n ,  "is not a fascinating number")
    else:
        print(n ,  "is a fascinating number")
else:
    print("othr than 4 digits not a fascinating number")
