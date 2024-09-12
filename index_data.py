import yfinance as yf
import matplotlib.pyplot as plt

def get_index_data(selected_index):
  """
  Fetches historical index data from Yahoo Finance.

  Args:
      selected_index (str): The index ticker symbol (e.g., "^NSEI", "^GSPC").

  Returns:
      pandas.DataFrame: The historical index data.
  """
  selected_index="^"+selected_index
  return yf.Ticker(selected_index).history(period="1d", interval="1m")

def plot_index_data(index_data):
  """
  Plots the closing price of the index data.

  Args:
      index_data (pandas.DataFrame): The historical index data.
  """
  plt.plot(index_data['Close'])
  plt.xlabel('Time')
  plt.ylabel('Closing Price')
  plt.title(f"{selected_index} Closing Price (1 Day, 1 Minute Interval)")
  plt.show()

if __name__ == "__main__":
  selected_index = "NSEI"  # Replace with your desired index
  index_data = get_index_data(selected_index)

  # Choose execution path: plot or return data
  # Option 1: Plot the graph directly
  plot_index_data(index_data)

  # Option 2: Return data for external plotting (uncomment)
  # return index_data