import yfinance as yf
import os
import matplotlib.pyplot as plt
import datetime

# --- 1. GET DATA ---
# The only change is here: we're now analyzing 'TSLA'
ticker = "TSLA"
start_date = "2015-01-01"
end_date = datetime.date.today().strftime("%Y-%m-%d")  # Get today's date
data = yf.download(ticker, start=start_date, end=end_date)
print(f"Data downloaded for {ticker} from {start_date} to {end_date}")

# --- SAVE DATA ---
# Create data folder if it doesn't exist
data_folder = "data"
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Save the dataframe to a CSV file
csv_file_path = os.path.join(data_folder, f"{ticker}_data.csv")
data.to_csv(csv_file_path)
print(f"Data saved to {csv_file_path}")

# --- 2. PLOT DATA ---

# Plot the closing price
plt.figure(figsize=(14, 7))
plt.plot(data["Close"], label="Close Price", color="blue")
plt.title(f"{ticker} Closing Price")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid()
