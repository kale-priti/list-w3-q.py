a=[98,34,63,876,6233,65]
i=0
max=0
sec_max=0
thrid_max=0
while i<len(a):
    j=0
    while j<len(a):
        if a[j]>max:
            max=a[j]
        if a[j] >sec_max and a[j]!=max:
            sec_max=a[j]
        if a[j]>thrid_max and a[j]!=sec_max and a[j]!=max:
            thrid_max=a[j]
        j=j+1
    i=i+1
print(max)
print(sec_max)
print(thrid_max)
