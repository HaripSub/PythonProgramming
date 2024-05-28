# Sample Data
import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset('tips')

# Violin Plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=data, x='day', y='total_bill', palette='muted')
plt.title('Total Bill Distribution by Day')
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.tight_layout()
plt.show()