# Write a script that takes in a string from the user.
user_sentance = input("Write a sentance: ")

# Using the `split()` method, create a list of all the words in the string
user_list = user_sentance.split()

# and print back the most common word in the text.
common_count = 1
common_word = None

for i in range(len(user_list)):
    if user_list.count(user_list[i]) > common_count:
        common_word = user_list[i]

print(common_word)
