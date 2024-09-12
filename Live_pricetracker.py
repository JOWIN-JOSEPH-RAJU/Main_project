import yfinance as yf
import time
import keyboard

def get_stock_price(company):
  """Retrieves the current stock price for the given company using yfinance.

  Args:
      company: The ticker symbol of the company (e.g., "INFY.NS").

  Returns:
      str: The current stock price as a string, or None if unable to retrieve it.
  """
  company=company +".NS"
  try:
    # Download live stock data
    data = yf.download(tickers=company, period="1d", interval="1m")

    # Extract current price from the most recent data point
    if data.shape[0] > 0:  # Check if data is available
      current_price = data["Close"].iloc[-1]
      return current_price.astype(str)  # Convert to string
    else:
      print(f"No data available for {company}")
      return None

  except Exception as e:
    print(f"Error retrieving stock price: {e}")
    return None

if __name__ == "__main__":
  company = input("Enter The Company Name (e.g., INFY.NS): ")

  # Handle potential keyboard input errors
  try:
    delay = int(input("Enter the refresh interval (seconds) (Press Esc to exit): "))
  except ValueError:
    print("Invalid input. Using default refresh interval (0 seconds).")
    delay = 0

  while True:
    if keyboard.is_pressed('esc'):
      break

    price = get_stock_price(company)
    if price:
      print(f"Stock Price for {company}: {price}")
    else:
      print("Unable to retrieve stock price.")

    time.sleep(delay)