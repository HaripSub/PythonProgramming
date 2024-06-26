import random
from faker import Faker

# Initialize the Faker object
fake = Faker()

# Define the number of persons you want to generate
num_persons = 5

# Generate random names and ages
names = [fake.first_name() for _ in range(num_persons)]
ages = [random.randint(20, 80) for _ in range(num_persons)]

# Create the dictionary
persons = {
    'name': names,
    'age': ages
}

# Print initial dictionary
print("Initial persons:", persons)

# Access and print elements
names = persons['name']
ages = persons['age']

print("Names:", names)
print("Ages:", ages)

# Add a new person
new_name = 'Fiona'
new_age = '29'

persons['name'].append(new_name)
persons['age'].append(new_age)

print("Updated persons after adding:", persons)

# Remove a person

person_name = input("Enter the person name")


if person_name in persons['name']:
    index = persons['name'].index(person_name)
    persons['name'].pop(index)
    persons['age'].pop(index)
    print("Updated persons after removal:", persons)
else:
    print(f'The person {person_name} is not found')

paired_list = list(zip(persons['name'], persons['age']))

# Sort the list of tuples based on the second element (age)
sorted_list_by_age = sorted(paired_list, key=lambda x: int(x[1]))

# Unzip the sorted list back into names and ages
sorted_names, sorted_ages = zip(*sorted_list_by_age)

# Create a new sorted dictionary
sorted_persons_by_age = {
    'name': list(sorted_names),
    'age': list(sorted_ages)
}

# Print the sorted dictionary by age
print("Sorted dictionary by age:", sorted_persons_by_age)

# Sort the list of tuples based on the first element (name)
sorted_list_by_name = sorted(paired_list, key=lambda x: x[0])

# Unzip the sorted list back into names and ages
sorted_names_1, sorted_ages_1 = zip(*sorted_list_by_name)

# Create a new sorted dictionary
sorted_persons_by_name = {
    'name': list(sorted_names_1),
    'age': list(sorted_ages_1)
}

# Print the sorted dictionary by age
print("Sorted dictionary by name:", sorted_persons_by_name)




