# Kilometers to Miles convertion

kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print("%0.2f km = %0.2f mls" % (kilometers, miles))

# calculate kilometers
kilometers = miles / conv_fac
print("%0.2f mls = %0.2f mls" % (miles, kilometers))