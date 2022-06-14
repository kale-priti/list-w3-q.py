

# Write a Python program to add a number to each element in a given list of numbers.
# Original lists:


a=[3,8,9,4,5,0,5,0,3]
add=int(input("enter the num"))
s=[]
i=0
while i<len(a):
    sum=add+a[i]
    s.append(sum)
    i=i+1
print(s)

