# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

my_set = set()
counter = 0

while True:
    user_number = int(input("Enter a unique number: "))
    if user_number in my_set:
        print("That number is not unqiue")
        counter += 1
        if counter == 5:
            print("Sorry, you have had 5 attempts:")
            break
    else:
        my_set.add(user_number)
    
    if len(my_set) == 10:
        print("congratulations, you didnt have 5 missed attempts")
        break
    
    
print(my_set)
