
import random

num_sublists = random.randint(2, 5)  # Number of sublists
max_elements = 10
element_range = (0, 100)

total_elements = num_sublists * max_elements
unique_numbers = random.sample(range(element_range[0], element_range[1] + 1), total_elements)

nested_list = []
for _ in range(num_sublists):
    num_elements = random.randint(1, max_elements)
    sublist = unique_numbers[:num_elements]
    unique_numbers = unique_numbers[num_elements:]
    nested_list.append(sublist)

flat_list = [item for sublist in nested_list for item in sublist]

squared_list = [[item**2 for item in sublist] for sublist in nested_list]

total_sum = sum(sum(sublist) for sublist in nested_list)

min_value = min(min(sublist) for sublist in nested_list)

max_value = max(max(sublist) for sublist in nested_list)

transposed_list = list(map(list, zip(*nested_list)))

sorted_sublists = [sorted(sublist) for sublist in nested_list]

