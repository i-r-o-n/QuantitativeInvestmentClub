import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Algotrade/weightedindex/recommended_trades.csv')

#matplotlib pi chart of portfolio df recomended trades column
df['Number of Shares to Buy'].value_counts().plot.pie()
plt.show()
