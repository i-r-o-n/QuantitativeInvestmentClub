import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

stocks = pd.read_csv('/Users/aadityarao/Documents/Python/QuantitativeInvestmentClub/Algotrade/weightedindex/sp_500_stocks.csv')
stocks

dfn = pd.read_csv('Algotrade/weightedindex/recommended_trades.csv')

from keySecret import IEX_CLOUD_API_TOKEN as token

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def dataingest():
    symbol_groups = list(chunks(stocks['Ticker'], 100))
    symbol_strings = []
    for i in range(0, len(symbol_groups)):
        symbol_strings.append(','.join(symbol_groups[i]))

    final_dataframe = pd.DataFrame(columns = column_names)

    for symbol_string in symbol_strings:
    #     print(symbol_strings)
        batch_api_call_url = f'https://cloud.iexapis.com/stable/stock/market/batch/?types=quote&symbols={symbol_string}&token={token}'
        data = requests.get(batch_api_call_url).json()
        for symbol in symbol_string.split(','):
            final_dataframe = final_dataframe.append(
                                            pd.Series([symbol, 
                                                    data[symbol]['quote']['latestPrice'], 
                                                    data[symbol]['quote']['marketCap'], 
                                                    'N/A'], 
                                                    index = column_names), 
                                            ignore_index = True)

# def calculate_portfolio_size():
    global portfolio_size
    portfolio_size = input('Enter the value of your portfolio: ')
    try:
        portfolio_size = float (portfolio_size)
    except ValueError:
        print('That is not a number!')
        portfolio_size = input('Enter the value of your portfolio: ')
        calculate_portfolio_size()


def calculate_weighted_index(dfn):
    portfolio_size = float(input('Enter the value of your portfolio: '))
    position = float(portfolio_size)/len(dfn.index)
    print(position)
    for i in range(0, len(dfn['Ticker']) - 1):
        dfn.loc[i, 'Number of Shares to Buy'] = position/dfn.loc[i, 'Stock Price']
    return dfn

def pushToExcel(df):
    writer = pd.ExcelWriter('recommended_trades.xlsx', engine = 'xlsxwriter')
    df.to_excel(writer, 'recomendedTrades', index = False)
    column_formats = {
    'A': ['Ticker'],
    'B': ['Stock Price'],
    'C': ['Market Capitalization'],
    'D': ['Number of Shares to Buy']
    }
    for column in column_formats.keys():
        writer.sheets['recomendedTrades'].set_column(f'{column}:{column}', 18)
        writer.sheets['recomendedTrades'].write(f'{column}1', column_formats[column][0])
    writer.save()

def main():
    df = calculate_weighted_index(dfn)
    pushToExcel(df)

if __name__ == '__main__':
    main()

