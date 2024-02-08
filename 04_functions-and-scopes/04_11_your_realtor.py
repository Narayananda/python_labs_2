# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.


def real_estate(**kwargs):
    for k, v in kwargs.items():
        print(f"Property attribute: {k} = {v}")

real_estate(location="Denmark",view="ocean")