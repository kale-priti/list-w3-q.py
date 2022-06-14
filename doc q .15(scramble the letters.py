
# Write a Python program to scramble the letters of string in a given list. 
# Original list:
list=['Python', 'list', 'exercises', 'practice', 'solution']
# After scrambling the letters of the strings of the said list:
# ['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']
i=1
p=[]
while i<len(list)+1:
    a=list[-i]
    p.append((a))
    i+=1
print((p))