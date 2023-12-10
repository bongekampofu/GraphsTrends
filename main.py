import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the dataset into a Pandas DataFrame
df = pd.read_csv(r"C:\Users\Bongeka.Mpofu\Documents\csv files\HistoricalPrices.csv")

# Rename the column to remove an additional space
df = df.rename(columns = {' Open': 'Open', ' High': 'High', ' Low': 'Low', ' Close': 'Close'})

# Convert the date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort the dataset in the ascending order of date
df = df.sort_values(by = 'Date')

# Extract the date and close price columns
dates = df['Date']
closing_price = df['Close']

# Create a line plot
#plt.plot(dates, closing_price, color = 'red', linewidth = 3)
# Line plot of Open and Close prices
plt.plot(df['Date'], df['Open'])
plt.plot(df['Date'], df['Close'])
plt.title('Open and Close Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()






# Show the plot
plt.show()