# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

# flattened_list = []

# for i in starter_list:
#     flattened_list += i

# print(flattened_list)



deep_list = [1,"fifi",[2,3,[8,9,(4,4,4,),8,7,7,8],[3,[4,[5]]],9090],[[],[[44]]],8989]

def into_the_void_again(inside_list):
    new_list = []
    for i in inside_list:
        if isinstance(i,(list,tuple)):
            new_list.extend(into_the_void_again(i))
        else:
            new_list.append(i)
    return new_list

print(into_the_void_again(deep_list))


hard_nested_list = deep_list

final_list = []
while True:
    for element in hard_nested_list:
        if isinstance(element, (list, tuple)):
            final_list.extend(element)
        elif isinstance(element, (int, float, str)):
            final_list.append(element)  # string,

    for elem in final_list:
        if isinstance(elem, (tuple, list)):
            hard_nested_list = final_list
            final_list = []
            break  # the else below will not execute, we repeat the while loop
    else:  # no break!!! only executes if for loop finishes
        break


print("\nBefore")
print(hard_nested_list)
print("-----------------")
print("After operation")
print(final_list)