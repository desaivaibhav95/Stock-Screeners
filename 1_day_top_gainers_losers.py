import datetime as dt
import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr
yf.pdr_override()
from dateutil.relativedelta import *
from nsepy.history import get_price_list

start_1day=dt.datetime.now() + relativedelta(days=-2)
end=dt.datetime.now()

gainers_losers_1day = pd.DataFrame(columns=['Company','Last Close','%Change(1-day)'])

for s in nse_stocks.index:
    stock = str(nse_stocks['SYMBOL'][s])

    try:
        df_1day=pdr.get_data_yahoo(stock,start_1day,end)
        last_close = df_1day['Adj Close'][-1]
        pct_chg = round(((df_1day['Close'][-1]-df_1day['Close'].shift(1)[-1])/df_1day['Close'].shift(1)[-1])*100,2)

        gainers_losers_1day = gainers_losers_1day.append({'Company':stock, 'Last Close':last_close, '%Change(1-day)':pct_chg},ignore_index=True)

    except:
        print("Ticker not available or delisted")

top_gainers_1day_list = gainers_losers_1day.sort_values('%Change(1-day)',ascending=False)
top_gainers_1day_list_top_50 = top_gainers_1day_list.head(50)
top_gainers_1day_list_top_100 = top_gainers_1day_list.head(100)
top_gainers_1day_list_top_500 = top_gainers_1day_list.head(500)

top_losers_1day_list = gainers_losers_1day.sort_values('%Change(1-day)')
top_losers_1day_list_50 = top_losers_1day_list.head(50)
top_losers_1day_list_100 = top_losers_1day_list.head(100)
top_losers_1day_list_500 = top_losers_1day_list.head(500)
