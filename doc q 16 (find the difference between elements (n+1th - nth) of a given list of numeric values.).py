a=[1,2,3,4,5,6]
i=0
b=[]
while i<len(a):
    if i!=1:
        b.append(1)
    i=i+1
print(b)

# def inset_element_list(lst, x, n):
#     i= n
#     while i < len(lst):
#         lst.insert(i, x)
#         i+= n+1
#         return lst