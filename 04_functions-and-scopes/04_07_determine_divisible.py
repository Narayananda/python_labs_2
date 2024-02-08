# Write a script where you complete the following tasks:

# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean

# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean

# - take in a number from the user between 1 and 1,000,000,000

# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 

# - print your the result variables with descriptive messages


def div4_or_7(number):
    if number%4==0 or number%7==0:
        return True
    else:
        return False
    

def div4_and_7(number):
    if number%4==0 and number%7==0:
        return True
    else:
        return False
    


user_input = int(input("Enter a number between 1 and 1,000,000,000: "))

four_or_seven = div4_or_7(user_input)
four_and_seven = div4_and_7(user_input)

print(f"Can {user_input} be divided by 4 or 7. The answer is: {four_or_seven}\nCan {user_input} be divided by 4 and 7. The answer is: {four_and_seven}")


