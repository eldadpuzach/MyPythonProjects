#create a cool calculator
c = 50
h = 30
#use this formula Q = square root of [(2*c*d)/h]
#find d

import math
x = []
y = [i for i in input('Give me a csv numbers: ').split(',')]
for d in y:
    x.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(x))

#this join method for srt to convert integer answ into a str
#this takes an input number and calculates the above formula with upper round