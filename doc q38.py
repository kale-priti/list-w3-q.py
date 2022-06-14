m="https://www.w3resource.com/python-execrices/list"
a=[".com","edu","tv","https"]
i=0
c=0
while i<len(a):
    if a[i] in m:
        c+=1
    i=i+1
if c>=1:
    print("true")
else:
    print("flase")