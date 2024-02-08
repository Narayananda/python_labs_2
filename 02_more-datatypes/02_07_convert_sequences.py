# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"
tuple_str = tuple(string)
my_list = list(tuple_str)
my_list[my_list.index("c")] = "k"
tuple_str_2 = tuple(my_list)

print(tuple_str_2)