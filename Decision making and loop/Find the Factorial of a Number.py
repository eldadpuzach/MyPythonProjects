# find the factorial of a number provided by the user.

# uncomment to take input from the user
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial doesn't exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 = 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of {0} = {1}".format(num, factorial))
