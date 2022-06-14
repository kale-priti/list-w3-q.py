a=[-2,4,3,-5,-8,-1,8,9,-9]
i=0
p_count=0
n_count=0
while i<len(a):
    if a[i]<0:
        n_count=n_count+1
    else:
        p_count=p_count+1
    i=i+1
print(p_count)
print(n_count)

        