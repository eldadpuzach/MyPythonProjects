# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# To take coefficient input from the users
# a = float(input('Enter a: '))
# b = float(input('Enter b: '))
# c = float(input('Enter c: '))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
x1 = (-b - cmath.sqrt(d)/ 2*a)
x2 = (-b + cmath.sqrt(d)/ 2*a)

print("The solutions are {0} and {1}".format(x1, x2))