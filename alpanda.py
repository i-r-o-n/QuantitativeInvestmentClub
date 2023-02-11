import alpaca_trade_api as api
from alpaca_trade_api.rest import TimeFrame
from alpaca_account import paper_account

ALPACA_KEY_ID = paper_account['api_key']
ALPACA_SECRET_KEY = paper_account['api_secret']
ALPACA_PAPER = True

alpaca = api.REST(ALPACA_KEY_ID, ALPACA_SECRET_KEY)

ticker = 'AAPL'

prices = alpaca.get_bars(ticker, TimeFrame.Day, start="2022-02-09T00:00:00-08:00", end=None,limit=365)

print(prices.df['close'])