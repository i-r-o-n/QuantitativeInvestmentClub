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

x = np.linspace(0, 10, 200)
y = []
for i in range(200):
    y.append(Stock(capex,depreciation,CIWC,principalPayments,debtIssuance,EBIT).FCFE)
    depreciation += ((random.random() - .5)/10)

fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()