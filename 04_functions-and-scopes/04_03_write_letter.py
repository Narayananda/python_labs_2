# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.


def write_letter(name, text):
    return f"Hello {name}, {text}. Take care {name}"

name1 = "julius"
text1 = "its been so long since i saw you last. how are you doing. Cant wait to see you again"

print(write_letter(name1,text1))