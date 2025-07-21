import pandas as pd
import matplotlib.pyplot as plt

# Part A
# Downloaded and included in the zip file

# Part B
dataFrame = pd.read_csv('diamonds.csv', index_col=0)

# Part C
print('Exercise 9.16 Part C:')
print("First seven rows of the DataFrame:")
print(dataFrame.head(7))

# Part D
print('Exercise 9.16 Part D:')
print("Last seven rows of the DataFrame:")
print(dataFrame.tail(7))

# Part E
print('Exercise 9.16 Part E:')
numerical_stats = dataFrame[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']].describe()
print("The descriptive statistics for numerical columns:")
print(numerical_stats)

# Part F
print('Exercise 9.16 Part F:')
categorical_stats = dataFrame[['cut', 'color', 'clarity']].describe()
print("The descriptive statistics for categorical columns:")
print(categorical_stats)

# Part G
print('Exercise 9.16 Part G:')
unique_cuts = dataFrame['cut'].unique()
unique_colors = dataFrame['color'].unique()
unique_clarities = dataFrame['clarity'].unique()
print("the unique values in 'cut':", unique_cuts)
print("the unique values in 'color':", unique_colors)
print("the unique values in 'clarity':", unique_clarities)

# Part H
print('Exercise 9.16 Part H:')
dataFrame[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']].hist(bins=20, figsize=(12, 8))
plt.suptitle("Histograms for Numerical Columns")
plt.show()
