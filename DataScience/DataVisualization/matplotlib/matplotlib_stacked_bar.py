import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:\\Users\\harip\\PythonProgramming\\DataScience\\person_data.csv'

data = pd.read_csv(file_path)

senior_citizens_data = data[data['age'] > 60]

# Group data by location and gender, and count the number of doctors
grouped_data = senior_citizens_data.groupby(['location', 'gender']).size().unstack()

# Drop any rows containing NaN values
grouped_data = grouped_data.dropna()

# Plot bar chart
plt.figure(figsize=(10, 6))
locations = grouped_data.index
female_counts = grouped_data['Female']
male_counts = grouped_data['Male']

print("Locations:", locations)
print("Female Counts:", female_counts)
print("Male Counts:", male_counts)

plt.barh(locations, female_counts, color='pink', label='Female')
plt.barh(locations, male_counts, left=female_counts, color='green', label='Male')
for loc, female, male in zip(locations, female_counts, male_counts):
    plt.text(female, loc, str(female), ha='right', va='center', color='black', fontweight='bold')
    plt.text(female + male, loc, str(male), ha='left', va='center', color='black', fontweight='bold')

plt.title('Counts of Female and Male Senior Citizens in Each Location')
plt.xlabel('Count')
plt.ylabel('Location')
plt.xticks(rotation=45)
plt.legend(title='Gender')
plt.tight_layout()
plt.show()

