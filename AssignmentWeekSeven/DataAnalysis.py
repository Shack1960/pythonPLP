# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
# Ensure the 'outputs' directory exists
import os
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

# Save the plot
plt.savefig(os.path.join(output_dir, 'sepal_length_trend.png'))

# Load the Iris dataset
# The Iris dataset is available in sklearn as a Bunch object (like a dictionary)
iris = load_iris()

# Convert the dataset to a pandas DataFrame for easier manipulation
# 'data' contains the numerical data, and 'target' represents the species
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# --- Step 1: Load and Explore the Dataset ---

# Display the first few rows of the dataset
print("\nFirst few rows of the dataset:\n", iris_df.head())

# Check the structure of the dataset
print("\nDataset information:\n")
iris_df.info()

# Check for missing values
missing_values = iris_df.isnull().sum()
print("\nMissing values per column:\n", missing_values)

# Since the Iris dataset has no missing values, no cleaning is needed

# --- Step 2: Basic Data Analysis ---

# Compute basic statistics for numerical columns
print("\nBasic statistics for numerical columns:\n", iris_df.describe())

# Group by species and compute the mean for each feature
species_means = iris_df.groupby('species').mean()
print("\nMean values for each species:\n", species_means)

# Identify patterns or interesting findings
print("\nObservations:\n")
print("- Setosa has the smallest average petal length and width.")
print("- Virginica has the largest average measurements across most features.")

# --- Step 3: Data Visualization ---

# Line chart: Trends over an index (arbitrary example since the Iris dataset is not time-series)
iris_df.reset_index().plot(x='index', y='sepal length (cm)', kind='line', title='Sepal Length Trend', legend=False)
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.grid()
plt.savefig('outputs/sepal_length_trend.png')
plt.show()

# Bar chart: Average petal length per species
species_means['petal length (cm)'].plot(kind='bar', title='Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.grid(axis='y')
plt.savefig('outputs/avg_petal_length_per_species.png')
plt.show()

# Histogram: Distribution of sepal length
sns.histplot(iris_df['sepal length (cm)'], kde=True, bins=10, color='blue')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.savefig('outputs/sepal_length_distribution.png')
plt.show()

# Scatter plot: Sepal length vs. petal length
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=iris_df)
plt.title('Sepal Length vs. Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.grid()
plt.savefig('outputs/sepal_vs_petal_length.png')
plt.show()

# --- Error Handling (for file operations and data integrity) ---
try:
    # Attempt to save the dataset to a CSV file
    iris_df.to_csv('outputs/iris_dataset.csv', index=False)
    print("Dataset saved successfully as 'iris_dataset.csv'.")
except Exception as e:
    print(f"Error saving dataset: {e}")

# --- Conclusion ---
print("\nScript executed successfully. Visualizations and dataset have been saved in the 'outputs' directory.")
