# Creating Sets
set1 = {1, 2, 3, 4, 5, 6, 8, 12}
set2 = {"a", "b", "c", "d", "e", "f"}
set3 = {4, 8, 12, 16, 20}

# Using The Union Function
print(set1.union(set2))
print(set1)
print(set2)
print(set1 | set2)

# Using The Intersection Function
result = set1.intersection(set3)
print(result)

# Using The Difference Function
print(set1.difference(set3))
print(set1-set3)

# Using The Symmetric Difference Function
print(set1.symmetric_difference(set3))
print(set1^set3)

# Checking Type Of Lists
list1 = [11, 22, 33, 44]
print(type(list1))

# Converting List To A Set
set4 = set(list1)
print(set4)
print(type(set4))