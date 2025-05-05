#QUESTION 1
import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Convert to a DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Display the first few rows
print("🔍 First 5 rows:")
print(df.head())

# Check data types and structure
print("\n📋 Data types:")
print(df.dtypes)


# Check for missing values
print("\n❓ Missing values:")
print(df.isnull().sum())

print("\n✅ Dataset cleaned (no missing values found).")


#QUESTION 2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load and convert dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

print("📊 Basic Statistics:")
print(df.describe())

print("\n📁 Grouped Means by Species:")
print(df.groupby('species').mean())

# Plot: Boxplot of petal length by species
plt.figure(figsize=(8, 6))
sns.boxplot(x='species', y='petal length (cm)', data=df, palette='Set2')
plt.title('Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.grid(True)
plt.show()

# Plot: Pairplot to visualize feature relationships by species
sns.pairplot(df, hue='species', palette='Set1', diag_kind='kde')
plt.suptitle("Pairwise Feature Relationships in Iris Dataset", y=1.02)
plt.show()

#QUESTION 3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
try:
    from sklearn.datasets import load_iris
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)

    # Add a new column for species names
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    print("✅ Dataset loaded successfully.\n")

except FileNotFoundError:
    print("❌ File not found.")
except Exception as e:
    print("❌ Something went wrong:", e)

# Check for missing values if any
if df.isnull().values.any():
    print("⚠️ Found missing values. Filling them with the mean...")
    df.fillna(df.mean(numeric_only=True), inplace=True)

# 1.Line Chart to show trend over time
df['date'] = pd.date_range(start='2025-01-01', periods=len(df))

#line plot
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['sepal length (cm)'], color='blue', label='Sepal Length')
plt.title('Sepal Length Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 2.Bar Chart  showing the comparison of a numerical value across categories 
plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal length (cm)', data=df, palette='pastel')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()

# 3. Histogram to show  numerical column to understand its distribution.

plt.figure(figsize=(8, 6))
plt.hist(df['sepal width (cm)'], bins=10, color='lightgreen', edgecolor='black')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# 4. Scatter Plot visualize the relationship between two numerical columns

plt.figure(figsize=(8, 6))
sns.scatterplot(
    x='sepal length (cm)',
    y='petal length (cm)',
    hue='species',
    data=df,
    palette='Set2'
)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.grid(True)
plt.tight_layout()
plt.show()
