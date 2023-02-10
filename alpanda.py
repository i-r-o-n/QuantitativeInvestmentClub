import alpaca_backtrader_api as alpaca
import backtrader as bt
from datetime import datetime
from alpaca_account import paper_account

ALPACA_KEY_ID = paper_account['api_key']
ALPACA_SECRET_KEY = paper_account['api_secret']
ALPACA_PAPER = True

fromdate = datetime(2020,8,5)
todate = datetime(2020,8,10)

tickers = ['AAPL', 'MSFT']
timeframes = {
    '2H':120,
    '5H':300
}

prices = dict()

class RSIStack(bt.Strategy):

    def next(self):
        for i in range(0,len(self.datas)):
            date = self.datas[i].datetime.datetime(ago=0)
            price = self.datas[i].close[0]
            prices[date] = price
            

cerebro = bt.Cerebro()
cerebro.addstrategy(RSIStack)
# cerebro.broker.setcash(100000)
# cerebro.broker.setcommission(commission=0.0)

store = alpaca.AlpacaStore(
    key_id=ALPACA_KEY_ID,
    secret_key=ALPACA_SECRET_KEY,
    paper=ALPACA_PAPER
)

DataFactory = store.getdata

for ticker in tickers:
    for timeframe, minutes in timeframes.items():
        print(f'Adding ticker {ticker} using {timeframe} timeframe at {minutes} minutes.')

        d = DataFactory(
            dataname=ticker,
            timeframe=bt.TimeFrame.Minutes,
            compression=minutes,
            fromdate=fromdate,
            todate=todate,
            historical=True)

        cerebro.adddata(d)

cerebro.run()
print("Final Portfolio Value: %.2f" % cerebro.broker.getvalue())
# cerebro.plot(style='candlestick', barup='green', bardown='red')
