# Create a function called my_enumerate() that mirrors the functionality of Python's built-in enumerate().

def my_enumerator(list:list,start=0):
    """Mirrors the functionality of Python's built-in enumerate()

    Args:
        list:list - takes a list

    Return:
        dict - returns a dictionary
        
    """
    dict1 = {}
    for item in list:
        dict1[start]=item
        start+=1
    return dict1.items()

courses = ["English", "Maths", "Chemistry", "Arts"]

for index, course in my_enumerator(courses,start=5):
    print(f"{index}: {course}")

