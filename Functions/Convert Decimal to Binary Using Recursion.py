# Decimal number is converted into binary by dividing the number successively by 2 and printing the remainder in reverse order.

def convertToBinary(n):
    # Function to print binary number for the input decimal using recursion
    if n > 1:
        convertToBinary(n//2)
    print(n % 2, end='')

# decimal number
dec = 34

convertToBinary(dec)