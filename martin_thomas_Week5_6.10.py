set1 = {'red', 'green', 'blue'}
set2 = {'cyan', 'green', 'blue', 'magenta', 'red'}

print(set1)
print(set2)

# Part A

print('Exercise 6.10 Part A:')

print("equal operator ==:")
print(set1 == set2)

print("not equal operator !=:")
print(set1 != set2)

print("subset operator <=")
print(set1 <= set2)
print("proper subset operator <")
print(set1 < set2)

print("superset operator >=")
print(set1 >= set2)
print("proper subset operator >")
print(set1 > set2)

# Part B

print('Exercise 6.10 Part B:')

union_set = set1 | set2
print("union operator |")
print(union_set)

intersection_set = set1 & set2
print("intersection operator &")
print(intersection_set)

difference_set = set1 - set2
print("difference operator -")
print(difference_set)

symmetric_difference_set = set1 ^ set2
print("symmetric difference operator ^")
print(symmetric_difference_set)

print("disjoint isdisjoint()")
print(set1.isdisjoint(set2))
