# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here

randlist.sort()
new_list = []

tuple_list = []

for n in randlist:
    tuple_list.append(n)
    if len(tuple_list) == 2:
        new_list.append(tuple(tuple_list))
        tuple_list = []
if len(randlist)%2==1:
    new_list.append((randlist[-1],0))
    

print(new_list)
