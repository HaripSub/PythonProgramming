import pandas as pd
import matplotlib.pyplot as plt


file_path = 'C:\\Users\\harip\\PythonProgramming\\DataScience\\DataAnalysis\\person_data.csv'

data = pd.read_csv(file_path)

# Filter the data for Houston
houston_data = data[data['location'] == 'Houston']

# Calculate the gender distribution
gender_counts = houston_data['gender'].value_counts()

print(gender_counts)


# Function to format the pie chart labels with the actual counts
def func(pct, all_values):
    absolute = pct / 100. * sum(all_values)
    rounded_value = round(absolute)
    return f"{rounded_value}"


# Plot pie chart for gender distribution
plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct=lambda pct: func(pct, gender_counts),
        startangle=140, colors=['skyblue', 'orange'])
plt.title('Gender Distribution in Houston')
plt.legend()
plt.show()


