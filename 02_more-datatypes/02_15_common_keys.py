# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

new_dic = {}

for i in dict_1:
    if i in dict_2:
        new_dic[i] = dict_1[i] + dict_2[i]
    elif i not in dict_2:
        new_dic[i] = dict_1[i]

for i in dict_2:
    if i not in new_dic:
        new_dic[i]=dict_2[i]
    else:
        continue

print(new_dic)

# # if dict_1.keys() in dict_2.keys():
# #     print("yes")

# print(dict_1.keys())