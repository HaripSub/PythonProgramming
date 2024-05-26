import csv
import random

from faker import Faker

# Initialize Faker
fake = Faker()

# Define the number of records
num_records = 1000

# Define the output file
output_file = "person_data.csv"

# Define the field names
fieldnames = ['id', 'name', 'age', 'location']

cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "San Francisco", "Seattle", "Denver", "Washington", "Boston"
]

# Open the CSV file for writing
with open(output_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    # Generate the data
    for i in range(1, num_records + 1):
        writer.writerow({
            'id': i,
            'name': fake.name(),
            'age': fake.random_int(min=1, max=100),
            'location':  random.choice(cities)
        })

print(f"Generated {num_records} records and saved to {output_file}")
