import alpaca_backtrader_api as alpaca
import backtrader as bt
import pytz
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

class RSIStack(bt.Strategy):

    def next(self):
        for i in range(0,len(self.datas)):
            print(f'{self.datas[i].datetime.datetime(ago=0)} \
            {self.datas[i].p.dataname}: OHLC: \
                  o:{self.datas[i].open[0]} \
                  h:{self.datas[i].high[0]} \
                  l:{self.datas[i].low[0]} \
                  c:{self.datas[i].close[0]} \
                  v:{self.datas[i].volume[0]}')

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
