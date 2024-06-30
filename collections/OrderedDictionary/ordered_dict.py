import csv
from collections import OrderedDict, namedtuple
import random



# Define the output file
output_file = "country_city_population_data.csv"
Coordinate = namedtuple('Coordinate', ['latitude', 'longitude'])


def generate_random_coordinates():
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    return Coordinate(latitude, longitude)


# Read data from the CSV file and store in a list of OrderedDict
def read_csv_to_ordereddict(filename):
    ordered_csv_data = []
    with open(filename, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ordered_row = OrderedDict()
            for fieldname in reader.fieldnames:
                ordered_row[fieldname] = row[fieldname]
            ordered_csv_data.append(ordered_row)
    return ordered_csv_data


# Read the generated CSV file
ordered_csv_data = read_csv_to_ordereddict(output_file)

# Print the original ordered CSV data with the new element
print("\nOriginal Data:")
for ordered_row in ordered_csv_data:
    print(ordered_row)

new_row = OrderedDict([('country', 'Usa'), ('city', 'NewYork'), ('population', '7034678')])
ordered_csv_data.append(new_row)

# Print the original ordered CSV data with the new element
print("\nOrdered dictionary with new row:")
for ordered_row in ordered_csv_data:
    print(ordered_row)

for ordered_row in ordered_csv_data:
    ordered_row['coordinates'] = generate_random_coordinates()  # Adding a new element 'continent'

print("\nOrdered dictionary with new field coordinates:")
for ordered_row in ordered_csv_data:
    print(ordered_row)

# Sort by Country
sorted_by_country = sorted(ordered_csv_data, key=lambda x: x['country'])
print("\nSorted by Country:")
for row in sorted_by_country:
    print(row)

# Sort by City
sorted_by_city = sorted(ordered_csv_data, key=lambda x: x['city'])
print("\nSorted by City:")
for row in sorted_by_city:
    print(row)

# Sort by Population
sorted_by_population = sorted(ordered_csv_data, key=lambda x: int(x['population']))
print("\nSorted by Population:")
for row in sorted_by_population:
    print(row)
