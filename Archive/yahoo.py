import yahooquery
import pprint

ticker = yahooquery.Ticker('AAPL')
# ticker.all_financial_data(frequency="q").to_csv('quarterly.csv') 
pprint.pprint(ticker.all_financial_data(frequency="q"))
pprint.pprint(ticker.esg_scores)
