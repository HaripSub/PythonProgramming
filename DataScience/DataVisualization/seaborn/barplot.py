import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'C:\\Users\\harip\\PythonProgramming\\DataScience\\DataAnalysis\\person_data.csv'

data = pd.read_csv(file_path)

# Filter the data for New York
ny_data = data[data['location'] == 'New York']

# Calculate the occupation counts
occupation_counts = ny_data['occupation'].value_counts().reset_index()
occupation_counts.columns = ['occupation', 'count']

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
    'School Student': 'blue',
    'Retired': 'gray'
}

# Assign colors to occupations, using a default color for any not listed
occupation_counts['color'] = occupation_counts['occupation'].map(occupation_colors)

# Set the Seaborn theme
sns.set_theme(style="whitegrid")

# Create the bar plot with hue
plt.figure(figsize=(10, 6))
bar_plot = sns.barplot(data=occupation_counts, x='occupation', y='count', hue='occupation', dodge=False,
                       palette=occupation_colors, legend=False)

# Add values on top of each bar
for index, row in occupation_counts.iterrows():
    bar_plot.text(index, row['count'], str(int(row['count'])), color='black', ha="center", va='bottom', fontsize=10)

# Create custom legend
legend_labels = list(occupation_colors.keys())
legend_handles = [plt.Rectangle((0, 0), 1, 1, color=occupation_colors[label]) for label in legend_labels]
plt.legend(legend_handles, legend_labels, title='Occupations', fontsize=10, title_fontsize='11')

# Set plot labels and title
plt.title('Occupation Distribution in New York', fontsize=16)
plt.xlabel('Occupation', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=25, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()
