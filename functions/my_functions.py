import pandas as pd

## Get adjusted closing prices
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


## Portfolio VaR
import numpy as np

def portfolio_var(returns, weights, confidence_level):
    # Calculate the portfolio expected return
    portfolio_return = np.sum(returns * weights)

    # Calculate the portfolio variance
    portfolio_variance = np.dot(weights.T, np.dot(returns.cov() * 252, weights))

    # Calculate the portfolio VaR
    portfolio_var = portfolio_return - (confidence_level * np.sqrt(portfolio_variance))

    return portfolio_var


## Portfolio ES
import numpy as np
from scipy.stats import norm

def portfolio_es(returns, weights, confidence_level):
    # Calculate the portfolio VaR
    portfolio_var = portfolio_var(returns, weights, confidence_level)

    # Calculate the portfolio expected return
    portfolio_return = np.sum(returns * weights)

    # Calculate the portfolio variance
    portfolio_variance = np.dot(weights.T, np.dot(returns.cov() * 252, weights))

    # Calculate the portfolio expected shortfall (ES)
    portfolio_es = portfolio_return - (np.sqrt(portfolio_variance) * (1 - norm.cdf(-confidence_level)))

    return portfolio_es