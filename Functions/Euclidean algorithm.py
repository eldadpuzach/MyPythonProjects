def computeHCF (x, y):

    # this function implements the Euclidian algorithm to find H.C.F. of two numbers
    while (y):
        x, y = y, x % y
    return x

print(computeHCF(24, 54))

# Here we loop until y becomes zero. The statement x, y = y, x % y does swapping of values in Python.
# In each iteration, we place the value of y in x and the remainder (x % y) in y, simultaneously.
# When y becomes zero, we have H.C.F. in x.