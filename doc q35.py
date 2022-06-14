a=[1234,122,1970,100]
i=0
b=str(a[0])[0]
c=0
while i<len(a):
    k=str(a[i])
    if k[0]==b:
        c=c+1
    i=i+1
if c==len(a):
    print("true")
else:
    print("false")


