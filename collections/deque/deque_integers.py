import random
from collections import deque

# Function to generate a deque with random integers and a maximum length
def generate_random_deque(start=0, end=100, maxlen=10):
    return deque((random.randint(start, end) for _ in range(maxlen)), maxlen=maxlen)

# Function to sort a deque
def sort_deque(d):
    return deque(sorted(d))

# Function to sort a deque in descending order
def sort_deque_descending(d):
    return deque(sorted(d, reverse=True))

# Function to add an element to the end of the deque if not already present
def add_element(d, element):
    if element not in d:
        d.append(element)
    return d

# Function to add an element to the beginning of the deque if not already present
def add_element_left(d, element):
    if element not in d:
        d.appendleft(element)
    return d

# Function to extend a deque with another sequence from the end
def extend_deque(d1, d2):
    d1.extend(d2)
    return d1

# Function to extend a deque with another sequence from the beginning
def extend_deque_left(d1, d2):
    d1.extendleft(d2)
    return d1

# Function to reverse the deque
def reverse_deque(d):
    d.reverse()
    return d

# Function to rotate the deque
def rotate_deque(d, n):
    d.rotate(n)
    return d

# Function to remove an element from the deque
def remove_element(d, element):
    try:
        d.remove(element)
    except ValueError:
        print(f"Element {element} not found in deque.")
    return d

# Function to count occurrences of an element in the deque
def count_element(d, element):
    return d.count(element)

# Function to insert an element at a specific position
def insert_element(d, index, element):
    d.insert(index, element)
    return d

# Example usage
random_deque = generate_random_deque(start=0, end=100, maxlen=10)
print("Original deque:", random_deque)

new_element_end = int(input("Enter the element to be added in the deque at the end: "))
new_deque_added_end = add_element(random_deque, new_element_end)
print("Deque after adding element at the end:", new_deque_added_end)

new_element_begin = int(input("Enter the element to be added in the deque at the beginning: "))
new_deque_added_begin = add_element_left(random_deque, new_element_begin)
print("Deque after adding element at the beginning:", new_deque_added_begin)

queue_to_extend = [45, 89]
extended_deque = extend_deque(new_deque_added_begin, queue_to_extend)
print("Deque after extending at the end:", extended_deque)

queue_to_left = [72, 23]
extended_deque_left = extend_deque_left(extended_deque, queue_to_left)
print("Deque after extending at the beginning:", extended_deque_left)

reversed_deque = reverse_deque(extended_deque_left)
print("Reversed deque:", reversed_deque)

sorted_deque = sort_deque(reversed_deque)
print("Sorted deque:", sorted_deque)

sorted_deque_desc = sort_deque_descending(reversed_deque)
print("Sorted deque (descending):", sorted_deque_desc)

rotations = int(input("Enter the number of positions to rotate the deque: "))
rotated_deque = rotate_deque(sorted_deque, rotations)
print("Rotated deque:", rotated_deque)

element_to_remove = int(input("Enter the element to be removed from the deque: "))
deque_after_removal = remove_element(rotated_deque, element_to_remove)
print("Deque after removing element:", deque_after_removal)

element_to_count = int(input("Enter the element to count in the deque: "))
count = count_element(deque_after_removal, element_to_count)
print(f"Element {element_to_count} occurs {count} times in the deque.")

index_to_insert = int(input("Enter the index to insert a new element: "))
element_to_insert = int(input("Enter the element to be inserted: "))
deque_after_insertion = insert_element(deque_after_removal, index_to_insert, element_to_insert)
print("Deque after inserting element:", deque_after_insertion)
