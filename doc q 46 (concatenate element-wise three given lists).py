#  Write a Python program to concatenate element-wise three given lists. 
# Original lists:
# ['0', '1', '2', '3', '4']
# ['red', 'green', 'black', 'blue', 'white']
# ['100', '200', '300', '400', '500']
# Concatenate element-wise three said lists:
# ['0red100', '1green200', '2black300', '3blue400', '4white500']
a=['0', '1', '2', '3', '4']
b=['red', 'green', 'black', 'blue', 'white']
c=['100', '200', '300', '400', '500']
p=[]
i=0
while i<len(a):
    if len(a)==len(b)==len(c):
        s=(a[i]+b[i]+c[i])
        p.append(s)
    i=i+1
print(p)