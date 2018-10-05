# This datatype supports methods like
# copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), symmetric_difference() and union().
# Being immutable it does not have method that add or remove elements.

# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

print(A.isdisjoint(B))

print(A.difference(B))
print(A | B)
print(A.add(3))