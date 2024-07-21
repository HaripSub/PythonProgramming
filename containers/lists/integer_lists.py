import bisect
import random
import numpy as np
from collections import Counter
from typing import List

# create a integer list

# using square brackets

integer_list = [1, 2, 3, 4, 5]

# create a list from a empty list
integer_list_new = []

# Using a for loop to add elements to the list
for i in range(1, 6):
    integer_list_new.append(i)

# Using a list comprehension to create a list of even numbers from 1 to 10
even_numbers = [i for i in range(11) if i % 2 == 0]

# Creating an odd numbers from an empty list using extend function from 1 to 10
odd_numbers = []

odd_numbers.extend(range(1, 10, 2))

# creating a list of numbers divisible by 5 from en empty list in the range 1 to 20
divisible_by_5 = []

divisible_by_5 += [i for i in range(1, 21) if i % 5 == 0]

# creating a random list of 5 numbers from 1 10 100 and sorting in ascending order

random_list = random.choices(range(1, 101), k=10)
random_list.sort()

new_element = 15

# Inserting the new element while maintaining sorted order
bisect.insort(random_list, new_element)

random_list = random.choices(range(1, 101), k=5)
random_list.sort()

new_element = 15

# Inserting the new element while maintaining sorted order
bisect.insort(random_list, new_element)


# Function to generate a random list of unique numbers from 100 to 1000 divisible by 10

def generate_random_list(number):
    # Generate a pool of numbers divisible by 10 from 1 to 100
    pool = list(range(100, 1001, 10))

    # Use random.sample to select 5 unique elements from the pool
    random_list = random.sample(pool, k=5)

    if not (isinstance(number, int)):
        print(f"{number} The number should be integer")

    # Check if number is within the range
    elif not (100 <= number <= 1000):
        print(f"{number} is not within the range")

    # Check if number is already present in random_list
    elif number in random_list:
        print(f"{number} is already present in the list")

    # Check if number is divisible by 10
    elif number % 10 != 0:
        print(f"{number} is not divisible by 10")

    else:
        print(f"{number} inserted successfully")
        random_list.append(number)

    # Sort the list in descending order
    random_list.sort(reverse=True)
    return random_list


number_input = int(input("Enter the number to be inserted into the list"))

generated_random_list = generate_random_list(number_input)

# function to find if an element is present in the list using lambda based
# condition: if the number is not present in the list and if it is divisible by 3

insert_if_not_present = lambda num_list, element, position: (
    num_list.insert(position, element) if element not in num_list and element % 3 == 0 else num_list
)

# generate a list of numbers divisible by 3 using numpy from 3 to 20
integer_array_divisible_by_3 = np.arange(3, 20, 3)

integer_list_divisible_by_3 = integer_array_divisible_by_3.tolist()

new_number_input = int(input("Enter the number to be inserted into the list"))

position = int(input("Enter the position to be inserted into the list"))

insert_if_not_present(integer_list_divisible_by_3, new_number_input, position)


# generate a duplicate random list a list of odd numbers
def generate_random_list_with_duplicates(elements, length):
    return random.choices(elements, k=length)


elements = [i for i in range(1, 10, 2)]
length = 10
duplicate_random_list = generate_random_list_with_duplicates(elements, length)


# function to count the duplicate elements in the list and display the result for each element in a dictionary
def count_elements(my_list):
    counter = Counter(my_list)
    sorted_counts = sorted(counter.items(), key=lambda x: x[0])
    result_dict = dict(sorted_counts)
    return result_dict


sorted_counts = count_elements(duplicate_random_list)


# function to count the occurrence  of a particular element in the list:
def count_occurrence_element(my_list, element):
    return my_list.count(element)


def print_result_count_individual_element_occurrence():
    element_to_be_found = int(input("Enter the element to be found"))
    if element_to_be_found in duplicate_random_list:
        print(
            f"the element {element_to_be_found} occurred {count_occurrence_element(duplicate_random_list, element_to_be_found)} times")
    else:
        print(f"the element {element_to_be_found} is not found in the list")


# to remove the duplicates from the list and make the list with the unique elements
unique_list = np.unique(duplicate_random_list)

# removing the element from a list

my_first_10_natural_numbers_list = [i for i in range(1, 11)]

for x in my_first_10_natural_numbers_list:
    if x % 2 == 0:
        my_first_10_natural_numbers_list.remove(x)


# finding the average of the elements in the list

def average(values: List[float]) -> float:
    return sum(values) / len(values)


print(f"average of the elements {average([1.0, 2.0, 3.0,4.0,5.0])}")
