######## Convert Character Matrix to single String;
    #The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
#The String after join: gfgisbest ########



# a=[['g','f','g'],['i','s'],['b','e','s','t']]
# i=0
# sum=""
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum+=a[i][j]
#         j+=1
#     i+=1
# print(sum)        



while i<=3:
    b=1
    while b<=3-i:
        print(" ",end="")
        b=b+1
    s=1
    while s<=i:
        print("*",end=" ")
        s=s+1
    print()
    i=i+1

a=1
while a<=3:
    j=1
    while j<=a:
        print(" ",end="")
        j=j+1
    p=1
    while p<=3-a:
        print("*",end=" ")
        p=p+1
    print()
    a=a+1
            
   


