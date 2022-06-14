a=[1,2,3,3,3,2,4,5,6,7,4,4]
i=0
count=0
while i<len(a):
    j=i
    while j<len(a):
        if a[i]==a[j]:
            count=count+1
        j=j+1
i=i+1
if count==3:
    print(a[i])
    