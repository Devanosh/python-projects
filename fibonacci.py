# n=int(input("enter the number: "))
# a=0
# b=1
# i=0
# f=[a,b]
# if n<=0:
#     print("not possible")
# elif n==1:
#     print(b)
# else:
#     while i<n+1:
#         i+=1
#         c=a+b
#         a=b
#         b=c
#         f.append(c)
#     print(f)
n=int(input("enter the number : "))
a=0
b=1
f=[a,b]
for i in range(0,n+1):
    c=a+b
    a=b
    b=c
    f.append(c)
print(f)