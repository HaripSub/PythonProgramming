import tkinter as tk
from tkinter import ttk, messagebox
import random
from bs4 import BeautifulSoup
import requests
import logging
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


def display_weather_data(weather_data):
    result_text.delete(1.0, tk.END)
    if weather_data:
        result_text.insert(tk.END, f"Weather in {weather_data.city.replace('-', ' ').title()}:\n")
        result_text.insert(tk.END, f"Temperature: {weather_data.temperature}\n")
        result_text.insert(tk.END, f"Description: {weather_data.description}\n")
    else:
        result_text.insert(tk.END, "No weather data available.\n")


def update_city_combobox(event):
    selected_country = country_var.get()
    if selected_country:
        city_combobox['values'] = country_city_mapping[selected_country]


def get_weather_data():
    country = country_var.get()
    city = city_var.get()
    if country and city:
        weather_data = fetch_weather_from_website(country, city)
        display_weather_data(weather_data)
    else:
        messagebox.showwarning("Input Error", "Please select both country and city.")


country_city_mapping = {
    'germany': ['frankfurt', 'munich', 'nuremberg', 'berlin', 'cologne'],
    'italy': ['rome', 'milan', 'pisa', 'naples', 'venice'],
    'france': ['nice', 'paris', 'bordeaux', 'lyon', 'strasbourg'],
    'india': ['chennai', 'hyderabad', 'kochi', 'mumbai', 'kolkata'],
    'switzerland': ['bern', 'zurich', 'lausanne', 'geneva', 'basel']
}

# Create the main window
root = tk.Tk()
root.title("Weather Data Fetcher")

# Create and set the country selection dropdown
country_var = tk.StringVar()
city_var = tk.StringVar()

country_label = tk.Label(root, text="Select a Country:")
country_label.pack(pady=5)
country_combobox = ttk.Combobox(root, textvariable=country_var, values=list(country_city_mapping.keys()))
country_combobox.pack(pady=5)
country_combobox.bind("<<ComboboxSelected>>", update_city_combobox)

# Create and set the city selection dropdown
city_label = tk.Label(root, text="Select a City:")
city_label.pack(pady=5)
city_combobox = ttk.Combobox(root, textvariable=city_var)
city_combobox.pack(pady=5)

# Create and set the fetch button
fetch_button = tk.Button(root, text="Fetch Weather Data", command=get_weather_data)
fetch_button.pack(pady=20)

# Create and set the result text box
result_text = tk.Text(root, wrap='word', width=50, height=20)
result_text.pack(pady=10)

# Run the application
root.mainloop()
