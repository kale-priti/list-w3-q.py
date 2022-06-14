

# You will be given a number and you need to return it as a string in Expanded Form#


a=input("enter the num")
b=[]
i=0
while i<len(a):
    k=len(a)-(i+1)
    if a[i]=="0":
        print(end=" ")
    else:
        s=int(a[i]*(10**k))
        b.append(s)
        print(b)
    i=i+1
print(b)






