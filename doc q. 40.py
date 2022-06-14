# Write a Python program to sum two or more lists, the lengths of the lists may be different. 
# Original list:
a=[[1, 2, 4], [2, 4, 4], [1, 2]]
i=0
l=[]
sum=0
while i<len(a):
    j=0
    while i<len(a[i]):
        s=a[i][j]
        l.append(s)
        j=j+1
    i=i+1
print(l)
