a=[34.67,12,-94.89,0,"c#"]
i=0
k=[]
while i<len(a):
    if type(a[i])==int:
        k.append(a[i])
    i=i+1
print(k)