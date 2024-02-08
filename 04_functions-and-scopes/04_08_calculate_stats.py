# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list):
# define the function here
  print(f"The biggest number is: {max(list)}")
  print(f"The smallest number is: {min(list)}")
  print(f"The sum of the numers is: {sum(list)}")
  print(f"The average of the numbers is: {sum(list)/len(list)}")

# call the function below here
stats(example_list)
