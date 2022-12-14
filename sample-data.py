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

# Get the stock prices data for the stocks in the DataFrame
prices = pdr.get_data_yahoo(df['Stock'], start_date, end_date)

# Print the prices data
print(prices)

# Set the path for the CSV file
csv_file_path = 'prices.csv'

# Save the DataFrame to a CSV file
prices.to_csv(csv_file_path)