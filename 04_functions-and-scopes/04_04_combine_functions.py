# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.


def greet(*args):
    for name in args:
        return f"Hello {name}, how are you doing."

def write_letter(name, text):
    return f"{greet(name)} {text} Goodbye {name}."


text1 = "Its been so long since i saw you last. Hope all is well. Cant wait to see you again."

print(write_letter("John",text1))