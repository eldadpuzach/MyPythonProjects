# find all numbers divisible by 7 but NOT a multiple of 5 between 2000 and 3200
# solution should be comma separated on a single line

empty_list = []

# iterate through the range of numbers

for i in range(1, 100):
    if (i%7 == 0) and (i%5!=0):
        empty_list.append(str(i))

print(','.join(empty_list))
