a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# Iterate the said list cyclically on specific index position 3 :
# ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
# Iterate the said list cyclically on specific index position 5 :
# ['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']
print(a)
i=0
index=int(input("enter the specific index position:"))
p=[]
while i<1:
    b=a[index: ]+a[0:index]
    p.extend(b)
    i=i+1
print(p)

