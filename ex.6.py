n= int(input("enter the number : "))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i

 
if n<0 :
    print("the factorial is not feasible for negative number")
elif n==0:
    print("0")
else :
    print(factorial)
