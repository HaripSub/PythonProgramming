import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:\\Users\\harip\\PythonProgramming\\DataScience\\DataAnalysis\\person_data.csv'

data = pd.read_csv(file_path)

# Scatter plot of age vs. gender
plt.figure(figsize=(10, 6))

# Mapping genders to markers
markers = {'Male': 'o', 'Female': 's'}

for gender, marker in markers.items():
    gender_data = data[data['gender'] == gender]
    plt.scatter(gender_data['age'], gender_data.index, marker=marker, label=gender)

plt.title('Age vs. Gender')
plt.xlabel('Age')
plt.ylabel('Index')
plt.legend()
plt.show()

