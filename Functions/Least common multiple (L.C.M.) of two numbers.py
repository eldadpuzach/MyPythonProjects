# The least common multiple (L.C.M.) of two numbers
# is the smallest positive integer that
# is perfectly divisible by the two given numbers.
# For example, the L.C.M. of 12 and 14 is 84.

# Python Program to find the L.C.M. of two input number

# define a function
def lcm(x, y):
    """This function takes two
    & returns the L.C.M."""

    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

# change the values of num1 and num2 for a different result
num1 = 54
num2 = 24

# uncomment the following lines to take input from the user
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))