from alpaca_trade_api.rest import TimeFrame, REST
from alpaca_account import paper_account
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import matplotlib.ticker as mtick
import numpy as np

# API Stuff
ALPACA_KEY_ID = paper_account['api_key']
ALPACA_SECRET_KEY = paper_account['api_secret']
ALPACA_PAPER = True

alpaca = REST(ALPACA_KEY_ID, ALPACA_SECRET_KEY)

ticker = 'AAPL'

def price_from_start_date(start: str) -> pd.DataFrame:

	end = dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=15)
	prices = alpaca.get_bars(ticker, TimeFrame.Day, start=start.isoformat(), end=end.isoformat()).df

	return prices

# Timezone things
PST = dt.timezone(dt.timedelta(hours=-8))
last_year = dt.datetime(2022, 2, 11, tzinfo=PST)

# Fetching data from API and writing to CSV
# price_from_start_date(last_year)['close'].to_csv('AAPL_closing_price.csv')

# Reading from CSV
df1 = pd.read_csv('AAPL_closing_price.csv')

# Converting the timestamp format and setting the index
df1.timestamp = pd.to_datetime(df1.timestamp, format="%Y-%m-%d %H:%M:%S%z")
df1.set_index(['timestamp'],inplace=True)

# Parameters for the plot
color = 'red'
fig, ax = plt.subplots()
plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter("$%.0f"))
plt.subplots_adjust(bottom = 0.2, top = 0.9) #ensuring the dates (on the x-axis) fit in the screen
plt.ylabel('Stock Price')
plt.xlabel('Dates')

# Plot function to animate
def bar(i):
	plt.legend(df1.columns)
	p = plt.plot(df1.index[:i], df1['close'][:i])
	p[0].set_color('blue')

# Creating the graph
animator = ani.FuncAnimation(fig, bar, interval = 10)

plt.show()

# animator.save('aapl_2022.gif')
