# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import my_functions

# Read the CSV file with portfolio data into a Pandas DataFrame
df = pd.read_csv('data.csv')

# Read the CSV files with stock data
adj_close = my_functions.get_adj_close(df)

print(adj_close)

# Calculate the summary statistics for the stock prices
print(df.describe())

# Visualize the stock prices over time
df.plot(x='Date', y='Stock', kind='line')
plt.show()

# Calculate and visualize the distribution of returns
returns = df.pct_change()
returns.plot(x='Date', y='Stock', kind='hist', bins=50)
plt.show()

# Calculate and visualize the correlation between the stock prices
corr = df.corr()
print(corr)