num = input("Enter a number: ")


# initialize sum
sum = 0


# a = int(num[0])
# a = a**3

# b = int(num[1])
# b = b**3


# c = int(num[2])
# c = c**3

for a in num:
    sum = sum + int(a) ** int(len(num))


# sum = a+b+c
print(sum)
sum = str(sum)

# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
