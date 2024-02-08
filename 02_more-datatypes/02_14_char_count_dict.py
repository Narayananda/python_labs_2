# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}
user_input = str(input("Write a string: "))
dic = {}

for i in range(len(user_input)):
    if user_input[i] not in dic:
        dic[user_input[i]] = 1
    else:
        dic[user_input[i]]+= 1

print(dic)