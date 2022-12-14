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

# Calculate the daily returns for each stock
returns_df = adj_close_df.pct_change()

# Create a 2 by 2 grid of subplots
fig, axs = plt.subplots(2, 2)

# Loop over the stocks in the DataFrame
for i, stock in enumerate(returns_df.columns):
  # Create a histogram of the daily returns for the current stock
  axs[i//2][i%2].hist(returns_df[stock], bins=50, alpha=0.5)

  # Add a legend and labels to the subplot
  axs[i//2][i%2].legend([stock])
  axs[i//2][i%2].set_xlabel("Daily Return")
  axs[i//2][i%2].set_ylabel("Frequency")
  axs[i//2][i%2].set_title(f"Distribution of Daily Returns for {stock}")

# Show the plots
plt.show()

# Calculate the correlation between the stock prices
corr_matrix = adj_close_df.corr()

# Visualize the correlation matrix
plt.imshow(corr_matrix, cmap="RdYlGn", interpolation="none")

# Add labels and a colorbar to the plot
plt.colorbar()
tick_marks = list(range(len(corr_matrix.columns)))
plt.xticks(tick_marks, corr_matrix.columns, rotation=45)
plt.yticks(tick_marks, corr_matrix.columns)

# Show the plot
plt.show()