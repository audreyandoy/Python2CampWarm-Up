# 1) create a variable called x and assign its value to 10.
# x = 10
# 2) Print out that variable to the compile
# print(x)
# 3) Create a variable that asks for user's name via input
# name = input("What is your  name?")
# print(name)
# 4) Have a user enter a number, if the number is greater than 10, print "the number is greater than 10" if the number is less print "the number is less than 10", else "the number is equal to 10"
num = int(input("Enter a number: "))
print(num)

if num > 10:
    print("The number is greater than 10!")
elif num < 10:
    print("The number is less than 10")
else: 
    print("number is equal to 10.")