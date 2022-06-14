#   Write a Python program to insert a specified element in a given list after every nth element.
# Original list:

# a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# k=2
# i=0
# p=[]
# while i<len(a):
#     # k=int(input("enter the number"))
#     if i==k:
#         p.append(20)
#         k+=2
#     p.append(a[i])  
#     i+=1
# print(p)      



  

    
#  Write a Python program to insert a specified element in a given list after every
#  nth element.
# Original list:

# a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# x=int(input("enter the num"))
# n=int(input("enter the number"))
# s=n
# i=n
# while i<len(a):
#     if i==n:
#         a.insert(i,x)
#         n=n+n
#     i=i+1
# print(a)
    
# a=[1,3,5,6]
# b=[8,9,4,3,1,5]
# i=0
# k=[]
# while i<len(a):
#     j=0
#     while j<len(b):
#         if a[i] not in b and a[i] not in k:
#             k.append(a[i])
#         if b[j] not in a and b[j] not in k:
#             k.append(b[j])
#         j=j+1
#     i=i+1
# print(k)

def hello(a):
    i=0
    n=[]
    r=0
    while i<len(a):
        if type(a[i])==list:
            j=0
            h=0
            while j<len(a[i]):
                if type(a[i][j])==list:
                    k=0
                    b=0
                    while k<len(a[i][j]):
                        if type(a[i][j][k])==int:
                            b=b+a[i][j][k]
                        k=k+1

                    n.append(b)
                else:
                    h+=a[i][j]
                j=j+1
            n.append(h)
        else:
            r=r+a[i]
        i=i+1
    n.append(r)
    print(n)
hello([2,[3,[6,1],5],3])


