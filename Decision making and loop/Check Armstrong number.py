#In case of an Armstrong number of 3 digits,
# the sum of cubes of each digits is equal to the number itself.
# For example:
# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.
# abcd... = an + bn + cn + dn + ...

# if the number provided by the user is an Armstrong number or not

# take input from the user
num = int(input("Enter a 3 digit number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
# display the result
if num == sum:
    print(num, " is an Armstrong number")
else:
    print(num, " isn't an Armstrong number")
