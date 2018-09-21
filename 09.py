# create an array of 5 integers and display array items, access them via index
from array import *
array_num = array('i', [1,3,5,7,9])
for i in array_num:
    print(i)
print('Access first three items individuals')
i = 0
while i < 3:
    print(array_num[i])
    i += 1
#append a new item to end of an array
print('starting array:', array_num)
array_num.append(11)
print('new array:', array_num)

#reverse the order
print('reversed array:', array_num[::-1])

#insert a new value before the number 3
print(array_num)
array_num.insert(1,4) # I want the number 4 at index of 2
print('CORRECTION', array_num)

#remove an item via index
array_num.pop(6) #deafault is last item, otherwise add index
print(array_num)

#remove the first occurance of an element
new_array = array('i', [1,3,5,7,3,9,3,11])
print('new array: ', new_array)
new_array.remove(1)
print(new_array)

#convert an array into a list
print(type(new_array))
x = new_array.tolist()
print(type(x))
print(x)