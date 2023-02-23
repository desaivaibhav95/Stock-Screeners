import datetime as dt
import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr
yf.pdr_override()
from dateutil.relativedelta import *
from nsepy.history import get_price_list

start_1mo=dt.datetime.now() + relativedelta(days=-30)
end=dt.datetime.now()

gainers_losers_1mo = pd.DataFrame(columns=['Company','Last Close','%Change(1-month)'])

for s in nse_stocks.index:
    stock = str(nse_stocks['SYMBOL'][s])

    try:
        df_1mo=pdr.get_data_yahoo(stock,start_1day,end)
        last_close = df_1mo['Adj Close'][-1]
        pct_chg = round(((df_1mo['Close'][-1]-df_1mo['Close'][0])/df_1mo['Close'][0])*100,2)

        gainers_losers_1mo = gainers_losers_1mo.append({'Company':stock, 'Last Close':last_close, '%Change(1-month)':pct_chg},ignore_index=True)

    except:
        print("Ticker not available or delisted")

top_gainers_1month_list = gainers_losers_1mo.sort_values('%Change(1-month)',ascending=False)
top_gainers_1month_list_top_50 = top_gainers_1month_list.head(50)
top_gainers_1month_list_top_100 = top_gainers_1month_list.head(100)
top_gainers_1month_list_top_500 = top_gainers_1month_list.head(500)

top_losers_1month_list = gainers_losers_1mo.sort_values('%Change(1-month)')
top_losers_1month_list_50 = top_losers_1month_list.head(50)
top_losers_1month_list_100 = top_losers_1month_list.head(100)
top_losers_1month_list_500 = top_losers_1month_list.head(500)
