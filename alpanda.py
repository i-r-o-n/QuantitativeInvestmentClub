from alpaca_trade_api.rest import TimeFrame, REST
from alpaca_account import paper_account
import datetime as dt
import pandas as pd

ALPACA_KEY_ID = paper_account['api_key']
ALPACA_SECRET_KEY = paper_account['api_secret']
ALPACA_PAPER = True

alpaca = REST(ALPACA_KEY_ID, ALPACA_SECRET_KEY)

ticker = 'AAPL'

def price_from_start_date(start: str) -> pd.DataFrame:

	end = dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=15)
	prices = alpaca.get_bars(ticker, TimeFrame.Day, start=start.isoformat(), end=end.isoformat()).df

	return prices

PST = dt.timezone(dt.timedelta(hours=-8))
last_year = dt.datetime(2022, 2, 11, tzinfo=PST)

# price_from_start_date(last_year)['close'].to_csv('AAPL_closing_price.csv')
print(pd.read_csv('AAPL_closing_price.csv').head())