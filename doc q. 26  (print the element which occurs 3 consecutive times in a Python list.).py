


a=[4,5,5,5,3,8]
count=0
i=0
while i<len(a):
    if  i>0:
        count=count+1
        print("count:",i)
        if count==3:
            print(a[i])
    i=i+1
