import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


file_path = 'C:\\Users\\harip\\PythonProgramming\\DataScience\\person_data.csv'

data = pd.read_csv(file_path)


# Get unique locations

locations = data['location'].unique()

# Calculate male and female counts for each location
male_counts = []
female_counts = []
for location in locations:
    male_counts.append(data[(data['location'] == location) & (data['gender'] == 'Male')].shape[0])
    female_counts.append(data[(data['location'] == location) & (data['gender'] == 'Female')].shape[0])

# Plot vertical bar chart for location distribution by gender
plt.figure(figsize=(12, 8))
bar_width = 0.35
index = np.arange(len(locations))

bars_male = plt.barh(index, male_counts, bar_width, label='Male', color='skyblue')
bars_female = plt.barh(index + bar_width, female_counts, bar_width, label='Female', color='pink')

for bar in bars_male:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{int(bar.get_width())}',
             ha='left', va='center')

# Add value annotations to female bars
for bar in bars_female:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{int(bar.get_width())}',
             ha='left', va='center')

plt.title('Location Distribution by Gender')
plt.ylabel('Location')
plt.xlabel('Count')
plt.yticks(index + bar_width / 2, locations, rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()