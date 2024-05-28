import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


file_path = 'C:\\Users\\harip\\PythonProgramming\\DataScience\\person_data.csv'

data = pd.read_csv(file_path)

# Filter the data for Houston
houston_data = data[data['location'] == 'Houston']

gender_counts = houston_data['gender'].value_counts()

print(gender_counts)


# Plot gender distribution using Seaborn
plt.figure(figsize=(8, 6))
ax = sns.countplot(data=houston_data, x='gender', palette=['skyblue', 'orange'])

# Display count values on top of the bars
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=12, color='black', xytext=(0, 5),
                textcoords='offset points')
legend_elements = [Patch(facecolor='skyblue', edgecolor='black', label='Male'),
                   Patch(facecolor='orange', edgecolor='black', label='Female')]
plt.legend(handles=legend_elements)

plt.title('Gender Distribution in Houston')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()
