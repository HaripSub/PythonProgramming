# Sample Data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'C:\\Users\\harip\\PythonProgramming\\DataScience\\DataAnalysis\\person_data.csv'

data = pd.read_csv(file_path)

age_data = data['age']

# Filter the data for Houston_data = data[data['location'] == 'Houston']

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='age', bins=10, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
