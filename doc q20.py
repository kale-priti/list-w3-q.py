
# Write a function that takes one argument “n” and delete that many elements from the list.


a=["1","2","3","4","5","6","7"]
i=0
b=[]
while i<1:
    k=0
    j=1+k
    while j<len(a) and k<len(a):
        sum=a[k]+a[j]
        b.append(sum)
        k=k+2
        j=j+2
    i=i+1
print(b)