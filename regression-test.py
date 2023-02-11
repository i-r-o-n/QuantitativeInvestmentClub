import random
from Archive.FCFE import Stock
import matplotlib.pyplot as plt
import numpy as np

capex = 10
depreciation = .1
CIWC = 3
principalPayments = 4
debtIssuance = 1
EBIT = 10

#make fake data
x = np.linspace(0, 10, 200)
y = []
for i in range(200):
    y.append(Stock(capex,depreciation,CIWC,principalPayments,debtIssuance,EBIT).FCFE)
    depreciation += ((random.random() - .5))

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
ax.plot(x,y, c="#151515")
ax.plot(x,smooth(3, y), c="r")
ax.plot(x,smooth(10, y), c="g")
plt.show()