import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:\\Users\\harip\\PythonProgramming\\DataScience\\person_data.csv'

data = pd.read_csv(file_path)

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