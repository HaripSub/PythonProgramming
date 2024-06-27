from collections import namedtuple
from math import radians, sin, cos, sqrt, atan2

# Define a named tuple type called 'Coordinate'
Coordinate = namedtuple('Coordinate', ['latitude', 'longitude', 'location'])
# Create instances of Coordinate
coordinate1 = Coordinate(latitude=37.7749, longitude=-122.4194, location="San Francisco, CA")  # San Francisco, CA
coordinate2 = Coordinate(latitude=34.0522, longitude=-118.2437, location="Los Angeles, CA")  # Los Angeles, CA

# Access fields by name
print(
    f"Coordinate 1: Latitude = {coordinate1.latitude}, Longitude = {coordinate1.longitude}, "
    f"Location={coordinate1.location}")

print(
    f"Coordinate 2: Latitude = {coordinate2.latitude}, Longitude = {coordinate2.longitude},'"
    f"Location={coordinate2.location}")


# Define a function that calculates the distance between two coordinates


def calculate_distance(coord1, coord2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = radians(coord1.latitude), radians(coord1.longitude)
    lat2, lon2 = radians(coord2.latitude), radians(coord2.longitude)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371.0 * c  # Radius of Earth in kilometers
    return distance


# Calculate the distance between the two coordinates
distance = calculate_distance(coordinate1, coordinate2)
print(f"Distance between locations:  {coordinate1.location} and {coordinate2.location} : {distance:.2f} km")
# Outputs: Distance between coordinates: 559.20 km

# Convert the named tuple to a dictionary
coordinate_dict = coordinate1._asdict()
print(coordinate_dict)  # Outputs: {'latitude': 37.7749, 'longitude': -122.4194}

# Update a field using the _replace method
updated_coordinate = coordinate1._replace(latitude=40.7128)  # New York City, NY
print(updated_coordinate)  # Outputs: Coordinate(latitude=40.7128, longitude=-122.4194)

# Define a list of coordinates
coordinates = [
    Coordinate(latitude=37.7749, longitude=-122.4194, location='San Francisco, CA'),  # San Francisco, CA
    Coordinate(latitude=34.0522, longitude=-118.2437, location="Los Angeles, CA"),  # Los Angeles, CA
    Coordinate(latitude=40.7128, longitude=-74.0060, location="New York City, NY")  # New York City, NY
]

coordinates.sort(key=lambda coord: coord.latitude)

# Iterate through the list and print each coordinate
for coord in coordinates:
    print(f"Latitude = {coord.latitude}, Longitude = {coord.longitude}, Location = {coord.location}")

