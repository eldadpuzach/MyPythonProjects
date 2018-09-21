# Check if the input number is prime or not

# take input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
# they divides by the number itself or by 1

if num > 1:
    #check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "isn't a prime number")
            print(i, "*", num//i, "=", num)
            break
    else:
        print(num, "is prime number")
