# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
list_ = [1, 2, 3, 4, 3, 4, 5]



# 1. Convert to a different data type


set1 = set(list_)
set2 = set(list_)

print(set1.union(set2))


# 2. Use a loop and a second list to solve it more manually
list2_ = []
for n in list_:
    if n not in list2_:
        list2_.append(n)

print(list2_)

