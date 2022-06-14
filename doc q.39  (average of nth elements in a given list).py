
#  Write a Python program to compute the average of nth elements in a given list of lists with different lengths.
# Original list:
a=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# Average of n-th elements in the said list of lists with different lengths:
# [4.8, 5.8, 6.8, 8.0, 11.0]
i=0
s=0
s1=0
s2=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if j==0:
            s+=a[i][j]
        if j==1:
            s1+=a[i][j]
        if j==2:
            s2=s+a[i][j]
        j+=1
    i+=1
# print(s)  
# print(s)          

