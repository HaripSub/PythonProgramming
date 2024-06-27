import random
from collections import namedtuple
from faker import Faker

# Initialize Faker to generate fake data
fake = Faker()

genders = ['Male', 'Female']

# Define the named tuple 'Person' to store name, age, and gender
Person = namedtuple('Person', ['name', 'age', 'gender'])


def create_random_persons_tuple(num_persons):
    persons = []
    for _ in range(num_persons):
        name = fake.name()
        age = fake.random_int(min=1, max=100)
        gender = random.choice(genders)
        person = Person(name=name, age=age, gender=gender)
        persons.append(person)
    return persons


persons_tuple = create_random_persons_tuple(5)

# Print the list of persons
print("Generated persons:")
for person in persons_tuple:
    print(f"Name = {person.name}, Age = {person.age}, Gender = {person.gender}")

# Sort the list of persons by age
persons_tuple.sort(key=lambda person: person.age)

# Print the sorted list of persons
print("\nSorted persons by age:")
for person in persons_tuple:
    print(f"Name = {person.name}, Age = {person.age}, Gender = {person.gender}")


def find_person(persons, name):
    for person in persons:
        if person.name == name:
            return person
    return None


# Check if a person with the input name exists and get their details
name_to_check = input("\nEnter the name to modify the age of the person: ")
person_found = find_person(persons_tuple, name_to_check)

if person_found:
    modified_person = person_found._replace(age=person_found.age + 1)
    # Replace the old tuple with the modified one in the list

persons_tuple = [modified_person if person == person_found else person for person in persons_tuple]

print("\nUpdated list of persons:")

print("\nSorted persons by age:")
for person in persons_tuple:
    print(f"Name = {person.name}, Age = {person.age}, Gender = {person.gender}")
