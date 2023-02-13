#calculate Moving average from a given Pandas DF

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')

df = pd.read_csv('AAPL_closing_price.csv', index_col='timestamp', parse_dates=True)

#set start and end timestamp

#import data

def dfProcess(df):
    dfp = df['close'].to_frame()
    dfp['SMA30'] = dfp['close'].rolling(10).mean()
    dfp.dropna(inplace=True)
    return dfp

def dfPlot(dfDate):
    #apply a trendline to moving average that goes beyon the given interval
    z = np.polyfit(dfDate.index.to_julian_date(), dfDate['SMA30'], 3)
    p = np.poly1d(z)
    dfDate['Trendline'] = p(dfDate.index.to_julian_date())
    dfDate[['close', 'SMA30', 'Trendline']].plot(label='RELIANCE', figsize=(16, 8))
    plt.show()

def main():
    dfPlot(dfProcess(df))

if __name__ == '__main__':
    main()