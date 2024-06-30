
import csv
from collections import OrderedDict
from faker import Faker

# Initialize Faker
fake = Faker()

# Define the number of records
num_records = 5

# Define the output file
output_file = "country_city_population_data.csv"

# Define the field names
fieldnames = ['country', 'city', 'population']

# Generate and write the CSV file
with open(output_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for _ in range(num_records):
        writer.writerow({
            'country': fake.country(),
            'city': fake.city(),
            'population': fake.random_int(min=1000, max=10000000)  # Population between 1,000 and 10,000,000
        })

print(f"Generated {num_records} records and saved to {output_file}")
