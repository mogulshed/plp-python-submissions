import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset info:")
df.info()

print("Descriptive statistics of numerical columns:")
print(df.describe())

print("\nMean of sepal length (cm) for each species:")
species_mean_sepal_length = df.groupby('species')['sepal length (cm)'].mean()
print(species_mean_sepal_length)

sns.set_style("whitegrid")
plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
sns.histplot(data=df, x='petal length (cm)', kde=True, bins=10)
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')

plt.subplot(2, 2, 2)
species_mean_petal_length = df.groupby('species')['petal length (cm)'].mean().reset_index()
sns.barplot(x='species', y='petal length (cm)', data=species_mean_petal_length)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')

plt.subplot(2, 2, 3)
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')

plt.subplot(2, 2, 4)
plt.plot(df['sepal length (cm)'], label='Sepal Length')
plt.plot(df['petal length (cm)'], label='Petal Length')
plt.title('Sepal and Petal Length Trend')
plt.xlabel('Sample Index')
plt.ylabel('Length (cm)')
plt.legend()

plt.tight_layout()
plt.show()