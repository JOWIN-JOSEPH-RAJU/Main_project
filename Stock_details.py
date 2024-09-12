
# this code downloads the bookvalue ,face vale pe ratio etc
import yfinance as yf

def get_stock_data(ticker):
    """
    Retrieves financial data for a given stock using yfinance.

    Args:
        ticker (str): The stock ticker symbol.

    Returns:
        dict: A dictionary containing the requested financial metrics.
    """

    try:
        yf_data = yf.Ticker(ticker)
        info = yf_data.info

        # Handle potential errors in fetching data
        if not info:
            raise ValueError(f"Unable to fetch data for ticker: {ticker}")

        roe = info.get('returnOnEquity', None)  # Handle missing values gracefully
        book_value = info.get('bookValue', None)
        face_value = info.get('enterpriseValue', None)
        pe_ratio = info.get('trailingPE', None)

        return {
            'ROE': roe,
            'Book Value': book_value,
            'Face Value': face_value,
            'P/E Ratio': pe_ratio,
            
        }

    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

# Example usage
ticker = "ONGC.NS"
data = get_stock_data(ticker)

if data:
    print("ROE:", data['ROE'])
    print("Book Value:", data['Book Value'])
    print("Face Value:", data['Face Value'])
    print("P/E Ratio:", data['P/E Ratio'])
else:
    print(f"Unable to retrieve data for {ticker}")