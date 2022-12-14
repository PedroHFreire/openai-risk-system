import pandas as pd

# Create a DataFrame with the sample data
data = {
    'Stock': ['Apple', 'Google', 'Microsoft', 'Amazon'],
    'Weight': [0.15, 0.20, 0.25, 0.40]
}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)