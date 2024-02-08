# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

dic = {}

for i in range(10):
    i = i+1
    dic[i] = i*i

print(dic)
