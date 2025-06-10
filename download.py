import yfinance as yf


# --- 1. GET DATA ---
# The only change is here: we're now analyzing 'TSLA'
ticker = "TSLA"
start_date = "2015-01-01"
end_date = "2023-12-31"
data = yf.download(ticker, start=start_date, end=end_date)
print(f"Data downloaded for {ticker}")
