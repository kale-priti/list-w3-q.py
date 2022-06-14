a=[100,102,1010,101]
b=[]
i=0
while i<len(a):
    k=str(a[i])
    j=0
    sum=" "
    while j<len(k):
        if k[j]!="0":
            sum=sum+k[j]
            print(sum)
        j=j+1
    b.append(int(sum))
    i=i+1
print(b)




# a=[101,100,120,1010]
# h=[]
# # b=str(a[i])
# i=0
# while i<len(a):
#     b=str(a[i])
#     j=0
#     sum=" "
#     while j<len(b):
#         if b[j]!="0":
#             sum=sum+b[j]
#             print(sum)
#         j=j+1
#     h.append(int(sum))
#     i=i+1
# print(h)