

# Write a Python program to find the dimension of a given matrix.
# Original list:

# a=[[1, 2], [2, 4]]
# a=[[0, 1, 2], [2, 4, 5], [2, 3, 4]]
# a=[[0, 1, 2], [2, 4, 5]]


i=0
b=len(a)
while i<b:
    j=0
    while j<len(a[i]):
        p=len(a[i])
        j=j+1
    i=i+1
print(b,p)

