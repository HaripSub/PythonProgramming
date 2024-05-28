
import pandas as pd
import matplotlib.pyplot as plt


file_path = 'C:\\Users\\harip\\PythonProgramming\\DataScience\\person_data.csv'

data = pd.read_csv(file_path)


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