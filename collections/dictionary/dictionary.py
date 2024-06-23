from faker import Faker

fake = Faker()


# generate a random persons dictionary by giving the number of persons
def create_random_persons_dict(num_persons):
    persons_dict = {}
    for i in range(num_persons):
        persons_dict[f'person_{i + 1}'] = {'name': fake.name(), 'age': fake.random_int(min=1, max=100)}
    return persons_dict


# enter the number of persons to generate the dictionary

num_persons = int(input("Enter the number of persons"))
random_persons_dict = create_random_persons_dict(num_persons)

# modify an existing entry in the dictionary
random_persons_dict['person_1']['name'] = "Alicia"

# adding a new entry
new_person_id = f'person_{num_persons + 1}'
new_person = {'name': fake.name(), 'age': fake.random_int(min=1, max=100)}
random_persons_dict[new_person_id] = new_person

# sorting the persons dictionary based on age
sorted_persons = dict(sorted(random_persons_dict.items(), key=lambda item: item[1]['age']))

# Getting all keys
keys = sorted_persons.keys()

# Getting all values
values = sorted_persons.values()

# Getting all key-value pairs
items = sorted_persons.items()

