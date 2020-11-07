# odd=[]
# for x in range(3,60):
#     if(x%3==0):
#        x+=8
#        odd.append(x)
# print(odd)

a=[x+8 for x in range(3,60) if x%3==0]
print(a)
