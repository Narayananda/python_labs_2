# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

string = "codingnomads"
a = tuple(string)
print(a)

for i in string:
    print(i)

for i in a:
    print(i)