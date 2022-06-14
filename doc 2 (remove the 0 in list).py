# a=[0,5,0,3,0,0,1,0,2,8,]
# i=0
# b=[]
# while i<len(a):
#     if a[i]==0:
#         pass
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)



a=[-2,5,-8,6,-3,-1,-9,7,5,3,]
i=1
n=[]
while i<len(a):
    j=0
    while j<len(a):
        if a[i]>0:
            n.append(a[i])
        else:
            n.append(0)
        j=j+1
    i=i+1
    

        
