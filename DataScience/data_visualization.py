import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
file_path = 'person_data.csv'
data = pd.read_csv(file_path)

# Filter the data for Houston
houston_data = data[data['location'] == 'Houston']

# Calculate the gender distribution
gender_counts = houston_data['gender'].value_counts()

# Plot pie chart for gender distribution
plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'orange'])
plt.title('Gender Distribution in Houston')
plt.legend()
plt.show()

# Filter the data for New York
ny_data = data[data['location'] == 'New York']

# Calculate the occupation counts
occupation_counts = ny_data['occupation'].value_counts()

# Define custom colors for each occupation
occupation_colors = {
    'Engineer': 'skyblue',
    'Doctor': 'orange',
    'Lawyer': 'green',
    'Shop Owner': 'brown',
    'Pharmacist': 'purple',
    'Accountant': 'yellow',
    'Bank Manager': 'cyan',
    'Baby': 'pink',
    'College Student': 'gold',
    'School Student': 'blue'
}

# Plot bar chart for occupation counts in New York with custom colors and legend
plt.figure(figsize=(10, 6))

bars = plt.bar(occupation_counts.index, occupation_counts, color=[occupation_colors.get(occupation, 'gray') for
                                                                  occupation in occupation_counts.index])

# Add values on top of each bar
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(int(bar.get_height())),
             ha='center', va='bottom')

# Create legend with custom colors
legend_labels = list(occupation_colors.keys())
legend_handles = [plt.Rectangle((0, 0), 1, 1, color=occupation_colors[label]) for label in legend_labels]
plt.legend(legend_handles, legend_labels)

plt.title('Occupation Distribution in New York')
plt.xlabel('Occupation')
plt.ylabel('Count')
plt.xticks(rotation=25, ha='right')
plt.tight_layout()
plt.show()

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

grouped_data = [data[data['location'] == location]['age'].values for location in data['location'].unique()]

# Plot box plot
plt.figure(figsize=(10, 6))
plt.boxplot(grouped_data, labels=data['location'].unique())
plt.title('Age Distribution by Location')
plt.xlabel('Location')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

senior_citizens_data = data[data['age'] > 60]

# Group data by location and gender, and count the number of doctors
grouped_data = senior_citizens_data.groupby(['location', 'gender']).size().unstack()

# Plot bar chart
plt.figure(figsize=(12, 8))
grouped_data.plot(kind='bar', stacked=False)
plt.title('Counts of Female and Male Senior citizens in Each Location')
plt.xlabel('Location')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(title='Gender')
plt.tight_layout()
plt.show()
