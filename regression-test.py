import random
from Archive.FCFE import Stock
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.ticker as mtick

# capex = 10
# depreciation = .1
# CIWC = 3
# principalPayments = 4
# debtIssuance = 1
# EBIT = 10

#Read from csv + 
df1 = pd.read_csv('AAPL_closing_price.csv')
df1['timestamp'] = pd.to_datetime(df1['timestamp'], format="%Y-%m-%d %H:%M:%S%z")
y = df1['close']

#make fake data
x = np.linspace(0, 1, len(df1['timestamp']))
# y = []
# for i in range(200):
#     y.append(Stock(capex,depreciation,CIWC,principalPayments,debtIssuance,EBIT).FCFE)
#     depreciation += ((random.random() - .5))

def smooth(n, y):
    #n = distance to blur/smooth, y is an array of the original points
    new = []
    for i in range(len(y)):
        total = 0
        added = 0
        for j in range(n, -n, -1):
            try:
                total += y[i + j]
                added += 1
            except:
                pass
        total /= (added)
        new.append(total)
    return new


fig, ax = plt.subplots()

ax.plot(df1['timestamp'],y)
ax.plot(df1['timestamp'],smooth(10, y))

plt.style.use('ggplot') #use pretty colors
plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter("$%.0f")) #add dollar sign
plt.subplots_adjust(bottom = 0.2, top = 0.9) #ensure dates fit on the screen

plt.ylabel('Stock Price')
plt.xlabel('Dates')

plt.show()