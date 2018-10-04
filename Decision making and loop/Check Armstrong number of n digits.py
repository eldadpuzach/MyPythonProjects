# check if the number provided by the user is an Armstrong number or not


# take input from the user
num = int(input("Enter a number: "))

# Changed num variable to string,
# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum = 0

#find the sum of the cube for each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# display the result
if num == sum:
    print(num, " is an Armstrong number")
else:
    print(num, " isn't an Armstrong number")