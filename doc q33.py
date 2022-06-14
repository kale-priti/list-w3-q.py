a=[12,67,98,34]
i=0
c=[]
while i<len(a):
    b=a[i]%10
    a[i]=a[i]//10
    c.append(b+a[i])
    i=i+1
print(c)