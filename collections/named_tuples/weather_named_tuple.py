import random
from bs4 import BeautifulSoup
import requests
import logging
import argparse
from collections import namedtuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a named tuple for weather data
WeatherData = namedtuple('WeatherData', ['city', 'temperature', 'description'])


def fetch_weather_from_website(country, city):
    base_url = 'https://www.timeanddate.com/weather'
    url = f'{base_url}/{country}/{city}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract temperature
        temperature_elem = soup.find('div', class_='h2')
        temperature = temperature_elem.text.strip() if temperature_elem else 'N/A'

        # Extract description
        description_elem = soup.find('img', id='cur-weather')
        description = description_elem['title'] if description_elem and \
                                                   'title' in description_elem.attrs else 'N/A'

        return WeatherData(city, temperature.replace('\xa0', ' '), description)

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred for {city}: {http_err}")
    except Exception as err:
        logging.error(f"Other error occurred for {city}: {err}")
    return None


def fetch_weather_data_for_country(country, cities):
    weather_data_list = []
    for city in cities:
        weather_data = fetch_weather_from_website(country, city)
        if weather_data:
            weather_data_list.append(weather_data)
    return weather_data_list


def print_weather_data(country, weather_data_list):
    print(f'{country.title()} is chosen')
    for weather_data in weather_data_list:
        print(f"Weather in {weather_data.city.replace('-', ' ').title()}:")
        print(f"Temperature: {weather_data.temperature}")
        print(f"Description: {weather_data.description}")
        print()  # Print a blank line for better readability


if __name__ == "__main__":
    country_city_mapping = {
        'germany': ['frankfurt', 'munich', 'nuremberg', 'berlin', 'cologne'],
        'italy': ['rome', 'milan', 'pisa', 'naples', 'venice'],
        'france': ['nice', 'paris', 'bordeaux', 'lyon', 'strasbourg'],
        'india': ['chennai', 'hyderabad', 'kochi', 'mumbai', 'kolkata'],
        'switzerland': ['bern', 'zurich', 'lausanne', 'geneva', 'basel']
    }

    parser = argparse.ArgumentParser(description='Fetch weather data for cities in a country.')
    parser.add_argument('--country', type=str, choices=country_city_mapping.keys(),
                        help='Specify the country to fetch weather data for.')
    args = parser.parse_args()

    if args.country:
        # Fetch weather data for the specified country
        country = args.country
        cities = country_city_mapping[country]
        weather_data_list = fetch_weather_data_for_country(country, cities)
    else:
        # Fetch weather data for a random country
        country = random.choice(list(country_city_mapping.keys()))
        cities = country_city_mapping[country]
        weather_data_list = fetch_weather_data_for_country(country, cities)
        weather_data_list.sort(key=lambda weather_data: weather_data.temperature)

    print_weather_data(country, weather_data_list)
