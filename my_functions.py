import pandas as pd

# Define the function
def get_adj_close(df):
  # Create an empty dataframe
  adj_close_df = pd.DataFrame()

  # Loop over the stocks in the DataFrame
  for stock in df['Stock']:
    # Read the csv file for the current stock
    stock_df = pd.read_csv(f"{stock}.csv")

    # Extract the adjusted closing prices from the dataframe
    adj_close = stock_df.loc[:, "Adj Close"]

    # Save the adjusted closing prices in the dataframe
    adj_close_df.loc[:, stock] = adj_close

  # Return the dataframe
  return adj_close_df