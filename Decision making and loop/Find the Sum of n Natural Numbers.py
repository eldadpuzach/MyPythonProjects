# find the sum of natural numbers up to n where n is provided by user

# uncomment to take input from the user
num = int(input("Enter a number: "))

sum = num * (num + 1) / 2
print("The sum is", sum)

# if num < 0:
#     print("Enter positive number")
# else:
#     sum = 0
#     # use while loop to iterate un till zero
#     while num > 0:
#         sum += num
#         num -= 1
#     print("The sum is", sum)
