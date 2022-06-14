
# Write a Python program to sum two or more lists, the lengths of the lists may be different. 
# Original list:
# [[1, 2, 4], [2, 4, 4], [1, 2]]
# Sum said lists with different lengths:
# [4, 8, 8]

a=[[1,2,4],[2,4,4],[1,2]]
i=0
b=[]
while i<len(a):
    sum=0
    j=0
    while j<len(a[i]):
        sum=sum+a[j][i]
        j=j+1
    b.append(sum)
    i=i+1
print(b)