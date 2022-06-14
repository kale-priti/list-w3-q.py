# remove=int(input("enter the remove num"))
# a=[1,2,3,4,5,6,7,8,9]
# i=0
# while i<remove:
#     a.pop()
#     i=i+1
# print(a)

a=[101,100,120,1010]
h=[]
# b=str(a[i])
i=0
while i<len(a):
    b=str(a[i])
    j=0
    sum=" "
    while j<len(b):
        if b[j]!="0":
            sum=sum+b[j]
        j=j+1
    h.append(int(sum))
    i=i+1
print(h)
            
    


            
