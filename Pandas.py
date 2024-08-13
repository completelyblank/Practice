import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Salary': [50000, 60000, 55000, 65000, 70000]
}
df = pd.DataFrame(data)

# 1. Display the first few rows of the DataFrame
print("1. Display the first few rows of the DataFrame:")
print(df.head())  # Shows the first 5 rows by default

# 2. Display the last few rows of the DataFrame
print("\n2. Display the last few rows of the DataFrame:")
print(df.tail())  # Shows the last 5 rows by default

# 3. Get a concise summary of the DataFrame
print("\n3. Get a concise summary of the DataFrame:")
df.info()

# 4. Get descriptive statistics of the DataFrame
print("\n4. Get descriptive statistics of the DataFrame:")
print(df.describe())

# 5. Get the shape (dimensions) of the DataFrame
print("\n5. Get the shape (dimensions) of the DataFrame:")
print(df.shape)  # (rows, columns)

# 6. Get the column labels of the DataFrame
print("\n6. Get the column labels of the DataFrame:")
print(df.columns)

# 7. Select a single column
print("\n7. Select a single column:")
print(df['Name'])

# 8. Select multiple columns
print("\n8. Select multiple columns:")
print(df[['Name', 'Salary']])

# 9. Select data by row label
print("\n9. Select data by row label:")
print(df.loc[1])  # Selects the second row (index = 1)

# 10. Select data by row position
print("\n10. Select data by row position:")
print(df.iloc[2])  # Selects the third row (index = 2)

# 11. Filter rows based on a condition
print("\n11. Filter rows based on a condition:")
print(df[df['Age'] > 25])

# 12. Sort the DataFrame by a specific column
print("\n12. Sort the DataFrame by a specific column:")
print(df.sort_values(by='Salary', ascending=False))

# 13. Drop a column from the DataFrame
print("\n13. Drop a column from the DataFrame:")
print(df.drop(columns=['Salary']))

# 14. Rename columns in the DataFrame
print("\n14. Rename columns in the DataFrame:")
df_renamed = df.rename(columns={'Name': 'Employee Name', 'Salary': 'Income'})
print(df_renamed)

# 15. Reset the index of the DataFrame
print("\n15. Reset the index of the DataFrame:")
print(df.reset_index(drop=True))

# 16. Set a column as the index
print("\n16. Set a column as the index:")
print(df.set_index('Name'))

# 17. Append rows from another DataFrame
print("\n17. Append rows from another DataFrame:")
new_data = {'Name': 'Frank', 'Age': 31, 'Salary': 62000}
new_df = pd.DataFrame([new_data])
df_appended = pd.concat([df, new_df], ignore_index=True)
print(df_appended)

# 18. Handle missing values by filling them with a specific value
df_missing = df.copy()
df_missing.loc[1, 'Age'] = None  # Introduce a missing value
print("\n18. Handle missing values by filling them with a specific value:")
print(df_missing.fillna(value=0))  # Fill missing values with 0

# 19. Drop rows with missing values
print("\n19. Drop rows with missing values:")
print(df_missing.dropna())  # Drop rows where any element is NaN

# 20. Concatenate two DataFrames
df2 = pd.DataFrame({'Name': ['George'], 'Age': [34], 'Salary': [52000]})
print("\n20. Concatenate two DataFrames:")
df_concatenated = pd.concat([df, df2], ignore_index=True)
print(df_concatenated)
