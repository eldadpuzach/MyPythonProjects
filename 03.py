#given integer number n, create a dictionary with the function that creates square
#of the dictionary index
print('Enter in an int. number:')
n = int(input())
d = dict()
for i in range(1, n+1):
    d[i] = i*i
print(d)
#recall that the range will go up to and not include