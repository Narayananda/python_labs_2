# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

from resources import randlist

if len(randlist) == len(set(randlist)):
    print("This list is unique: \n", randlist)
else:
    print("This list is not unique: \n", randlist)