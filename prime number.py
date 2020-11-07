inp = int(input("enter the number"))

a= int(inp+1/2)
  
if inp > 1:  
   for i in range(2, a): 
       if (inp % i) == 0: 
           print(inp, "is not a prime number") 
           break
   else: 
       print(inp, "is a prime number") 
  
else: 
   print(inp, "is not a prime number") 