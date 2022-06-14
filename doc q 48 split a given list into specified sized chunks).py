#  program to split a given list into specified sized chunks. 
# Original list:
a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
i=0
b=[]
size=int(input("enter the specified sized chunks:"))
while i<=len(a)-size:
    b.append(a[i:i+size])
    i=i+size
print(b)