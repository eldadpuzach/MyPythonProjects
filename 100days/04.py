#creates list & tuple for csv input
values = input('Give me some cs numbers:')
list = values.split(',')
tuple = tuple(list)
print(list,tuple)