# display all the prime numbers within an interval

# change the values of lower and upper for a different result
# lower = 900
# upper = 1000

# uncomment the following lines to take input from the user
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between {0} and {1} are:".format(lower, upper))

for num in range(lower, upper + 1):
    #prime numbers are greater than 1
    if num >1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
