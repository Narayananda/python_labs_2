# Write a script that takes a string from the user
user_input = list(map(str, input("write a sentence: ").split()))

# and creates a list that contains a tuple for each word.
tuple_list = []
for word in user_input:
    tuple_list.append(tuple(word))

print(tuple_list)
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]
