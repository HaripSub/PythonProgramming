import math
import random
import string
from faker import Faker

fake = Faker()


# Random integer
def random_int():
    return random.randint(1, 100)


# Random float
def random_float():
    return round(random.uniform(1.0, 100.0), 2)


# Random string
def random_string(length=5):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


# Random boolean
def random_bool():
    return random.choice([True, False])


# Random list
def random_list(length=3):
    return [random_int() for _ in range(length)]


# Random dictionary
def random_dict(length=3):
    result = {}
    for _ in range(length):
        word = fake.word()
        result[word] = len(word)
    return result


def random_tuple(length=5):
    return tuple(random_int() for _ in range(length))


# Creating a tuple with random data types
mixed_tuple = (
    random_int(),
    random_float(),
    random_string(),
    random_bool(),
    random_list(),
    random_dict(),
    random_tuple()
)

print(list(mixed_tuple))

# Inserting a new element (e.g., a new random number) into the tuple
new_element = random.randint(101, 200)  # Example of a new element
index = 4  # Insert at index 4 (before the random list)

# Create a new tuple with the new element inserted
new_tuple = mixed_tuple[:index] + (new_element,) + mixed_tuple[index:]
print("New tuple:", new_tuple)


def remove_element_by_value(tpl, value):
    # Convert tuple to list
    lst = list(tpl)
    # Remove the first occurrence of the value
    if value in lst:
        lst.remove(value)
    # Convert list back to tuple
    else:
        print(f"Element {value} is not found")
    return tuple(lst)


element = input("Enter the element to be removed")
try:
    # Attempt to convert to integer
    if element.isdigit():
        element = int(element)
    elif element == 'True':
        element = True
    elif element == 'False':
        element = False
    else:
        # Attempt to convert to float
        element = float(element)
except ValueError:
    # Keep as string if conversion to integer or float fails
    pass

updated_tuple_after_removal = remove_element_by_value(new_tuple, element)

print(updated_tuple_after_removal)
