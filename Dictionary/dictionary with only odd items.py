even_squares = {x: x*x for x in range(11) if x%2 == 0}
odd_squares = {x: x*x for x in range(11) if x%2 == 1}
squares = {x: x*x for x in range(11)}

# Output: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(odd_squares)
print(even_squares)
print(squares)