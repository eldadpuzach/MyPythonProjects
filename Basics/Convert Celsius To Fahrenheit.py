# Python Program to convert temperature in celsius to fahrenheit
# They are related by the formula:
# celsius * 1.8 = fahrenheit - 32
# change this value for a different result
celsius = int(input("Enter the value of temperature in Celcius: "))

# calculate fahrenheit
farenheit = (celsius * 1.8) + 32
celsius = (farenheit - 32) / 1.8
print("%0.0f C = %0.0f F" % (celsius, farenheit))
print("%0.0f F = %0.0f C" % (farenheit, celsius))
