str=input("enter the word : ")
if str[::]==str[::-1]:
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")