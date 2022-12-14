import pandas as pd
import pandas_datareader as pdr

# Set the start and end dates for the data
start_date = '2020-01-01'
end_date = '2022-12-31'

# Create a DataFrame with the sample data
data = {
    'Stock': ['AAPL', 'GOOGL', 'MSFT', 'AMZN'],
    'Weight': [0.15, 0.20, 0.25, 0.40]
}
df = pd.DataFrame(data)

# Save the DataFrame to a csv file
df.to_csv("data/data.csv")

# Loop over the stocks in the DataFrame
for stock in df['Stock']:
  # Get the stock prices data for the current stock
  stock_prices = pdr.get_data_yahoo(stock, start_date, end_date)
  
  # Create a new dataframe for the current stock
  stock_df = pd.DataFrame(stock_prices)
  
  # Save the dataframe to a csv file
  stock_df.to_csv(f"data/{stock}.csv")
