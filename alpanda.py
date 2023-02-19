from alpaca_trade_api.rest import TimeFrame, REST
from alpaca_account import paper_account
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import matplotlib.ticker as mtick
import matplotlib.dates as mdates
import numpy as np
import time

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
df1 = pd.read_csv('AAPL_closing_price.csv', index_col='timestamp', parse_dates=True)

roll = 8
df1['SMA'] = df1['close'].shift(-roll//2).rolling(roll).mean()
# df1.dropna(inplace=True)

x_nums = pd.to_datetime(df1.index).astype(int) / 10**9
# print(x_nums[0], type(x_nums[0]))
x_dates = mdates.date2num(df1.index)


# Parameters for the plot
fig, ax = plt.subplots()
plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter("$%.0f"))
plt.subplots_adjust(bottom = 0.2, top = 0.9) #ensuring the dates (on the x-axis) fit in the screen
plt.ylabel('Stock Price')
plt.xlabel('Dates')

plt.style.use('default')

# Plot function to animate
def bar(i):
	# plt.plot(df1['close'][:i], c='blue')
	plt.plot(df1['SMA'][:i], c='orange')
	if i % 25 == 0 and i != 0:
		try:
			trend = np.polyfit(x_nums[i-roll:i], df1['SMA'].to_list()[i-roll:i], 1)
			p = np.poly1d(trend) 
			plt.plot(x_dates[i-2:i+10], p(x_nums[i-2:i+10]), c='red')
		except:
			pass

# Creating the graph
animator = ani.FuncAnimation(fig, bar, interval = 10)
# plt.show()

# animator.save('./videos/aapl_2022.gif')
animator.save('./videos/aapl_trendline.gif')
