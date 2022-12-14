# Define the function
def get_adj_close(df):
  # Loop over the stocks in the DataFrame
  for stock in df['Stock']:
    # Read the csv file for the current stock
    stock_df = pd.read_csv(f"{stock}.csv")

    # Extract the adjusted closing prices from the dataframe
    adj_close = stock_df.loc[:, "Adj Close"]

    # Print the adjusted closing prices for the current stock
    print(f"Adjusted closing prices for {stock}:")
    print(adj_close)