import random
from collections import deque

# List of fruit names
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry',
          'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango',
          'nectarine', 'orange', 'pear', 'quince', 'raspberry',
          'strawberry', 'tangerine', 'watermelon', 'peaches', 'blueberry', 'blackberry', 'mandarin']


# Function to generate a deque with random fruits
def generate_random_fruit_deque(num_elements=10):
    random_fruits = deque(random.sample(fruits, num_elements))
    return random_fruits


def sort_fruit_deque(fruit_deque):
    # Convert deque to list and sort it
    sorted_list = sorted(fruit_deque)
    # Convert the sorted list back to a deque
    return deque(sorted_list)


# Example usage
random_fruit_deque = generate_random_fruit_deque(num_elements=5)
print(random_fruit_deque)

sorted_fruit_deque = sort_fruit_deque(random_fruit_deque)
print("Sorted fruit deque:", sorted_fruit_deque)
