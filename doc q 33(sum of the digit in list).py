
a=[12, 67, 98, 34]
i=0
sum=0
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j=j+1
    i=i+1
print(sum)

