import pandas as pd
import matplotlib.pyplot as plt

# Import the get_adj_close() function from the my_functions.py file
from my_functions import get_adj_close

# Read in the DataFrame from the saved data
df = pd.read_csv("data.csv")

# Call the get_adj_close() function and pass in the DataFrame
adj_close_df = get_adj_close(df)

# Plot the adjusted closing prices for each stock
adj_close_df.plot()

# Add a legend and labels to the plot
plt.legend(adj_close_df.columns)
plt.xlabel("Date")
plt.ylabel("Adjusted Closing Price")
plt.title("Adjusted Closing Prices for Stocks in the Portfolio")

# Show the plot
plt.show()

# Calculate and visualize the distribution of returns
#returns = df.pct_change()
#returns.plot(x='Date', y='Stock', kind='hist', bins=50)
#plt.show()

# Calculate and visualize the correlation between the stock prices
#corr = df.corr()
#print(corr)