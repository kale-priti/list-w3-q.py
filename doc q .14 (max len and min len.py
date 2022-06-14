a=[[1,3],[5,7,1],[0],[9,11,11,1,56],[13,15,17,34]]
i=0
max_len=[]
min_len=a[0]
while i<len(a):
    j=0
    while j<len(a[i]):
        if len(a[i])>len(max_len):
            max_len=a[i]
        if len(a[i])<len(a[0]):
            min_len=a[i]
        j=j+1
    i=i+1
print(max_len)
print(min_len)


