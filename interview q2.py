# a=[1,2,[],1,[]]
# i=0
# b=[]
# while i<len(a):
#     if a[i]!=[]:
#         b.append(a[i])
#     i=i+1
# print(b)

# a=[101,1001,1010,1110]
# b=[]
# i=0
# while i<len(a):
#     s=str(a[i])
#     sum=" "
#     j=0
#     while j<len(s):
#         if s[j]!="0":
#             sum=sum+s[j]
#         j=j+1
#     k=int(sum)
#     b.append(k)
#     i=i+1
# print(b)
# a="my name is sreekanya"
# print(a[12:])

# a=[1,2,3,4,5]
# b=[1,7,8,9,]


# l=[2,4,7,[8,9,7],4,3,9]
# i=0
# a=[]
# b=[]
# sumE=0
# sumO=0
# while i<len(l):
#     if type(l[i])==int:
#         if l[i]%2==0:
#             a.append(l[i])
#             sumE+=l[i]
#         else:    
#             b.append(l[i])
#             sumO+=l[i]
#     else:
#         j=0
#         while j<len(l[i]):
#             if l[i][j]%2==0:
#                 a.append(l[i][j])
#                 sumE+=l[i][j]
#             else:
#                 b.append(l[i][j]) 
#                 sumO+=l[i][j] 
#             j+=1              
#     i+=1
# print("even num sum",a,sumE)
# print("odd num sum",b,sumO)
            




a=[1,0,0,0]
i=0
sum=""
while i<len(a):
    sum=sum+str(a[i])
    i=i+1
n=int(sum)
print(n)
i=0
sum=0
while n>0:
    sum+=(n%10)*(2**i)
    n=n//10
    i=i+1
print(sum)

        

