# Sample Data
import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset('iris')

# Pair Plot
sns.pairplot(data, hue='species', palette='Set1')
plt.suptitle('Pair Plot of Iris Dataset', y=1.02)
plt.tight_layout()
plt.show()
