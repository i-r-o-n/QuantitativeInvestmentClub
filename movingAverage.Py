#calculate Moving average from a given Pandas DF

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')

df = pd.read_csv('/Users/aadityarao/Documents/Python/QuantitativeInvestmentClub/relianceStock.csv', index_col='Date', parse_dates=True)

#set start and end date
start_date , end_date = '2020-01-01', '2020-12-31'

#import data

def dfProcess(df):
    dfp = df['Close'].to_frame()
    dfp['SMA30'] = dfp['Close'].rolling(10).mean()
    dfp.dropna(inplace=True)
    dfDate = dfp.loc[start_date:end_date]
    return dfDate

def dfPlot(dfDate):
    #apply a trendline to moving average that goes beyon the given interval
    z = np.polyfit(dfDate.index.to_julian_date(), dfDate['SMA30'], 3)
    p = np.poly1d(z)
    dfDate['Trendline'] = p(dfDate.index.to_julian_date())
    dfDate[['Close', 'SMA30', 'Trendline']].plot(label='RELIANCE', figsize=(16, 8))
    plt.show()

def main():
    dfPlot(dfProcess(df))

if __name__ == '__main__':
    main()