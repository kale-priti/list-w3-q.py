a=[1,-2,-67,0,-8,7,45,8,6,-3]
i=0
count_posi=0
count_neg=0
while i<len(a):
    if a[i]<0:
        count_neg=count_neg+1
    else:
        count_posi=count_posi+1
    i=i+1
print("count negative num",count_neg)
print("count positive",count_posi)