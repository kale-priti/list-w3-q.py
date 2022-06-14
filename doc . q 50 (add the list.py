
# # Write a Python program to join two given list of lists of same length, element wise. 
# # Original lists:


# a=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# b=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# i=0
# d=[]
# while i<len(a):
#     j=0
#     while j<len(b):
#         if len(a)==len(b):
#             s=a[i]+b[i]
#             d.append(s)
#         j=j+1
#         i=i+1
# print(d)

a="my name is priti"
b=a.split()
print(b)
i=0
l=""
while i<len(b):
    j=0
    s=""
    while j<len(b[i]):
        if j==0:
            k=b[i][j].upper()
            s+=k
        else:
            s+=b[i][j]
        j=j+1
    l=l+s
    i=i+1
print(l)

