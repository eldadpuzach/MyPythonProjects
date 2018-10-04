# import fractions
#
# # # Output: 3/2
# # print(fractions.Fraction(1.5))
# #
# # # Output: 5
# # print(fractions.Fraction(5))
# #
# # # Output: 1/3
# # print(fractions.Fraction(1,3))
#
# # As float
# # Output: 2476979795053773/2251799813685248
# print(fractions.Fraction(1.1))
#
# # As string
# # Output: 11/10
# print(fractions.Fraction('1.1'))

from fractions import Fraction as F

# Output: 2/3
print(F(1,3) + F(1,3))

# Output: 6/5
print(1 / F(5,6))

# Output: False
print(F(-3,10) > 0)

# Output: True
print(F(-3,10) < 0)