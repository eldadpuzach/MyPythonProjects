# Output = [64, 128, 256, 512]
pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)

# Output = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
odd = [x for x in range(20) if x % 2 == 1]
print(odd)

# Output = ['Python Language', 'Python Programming', 'C Language', 'C Programming']
[x+y for x in ['Python ','C '] for y in ['Language','Programming']]
