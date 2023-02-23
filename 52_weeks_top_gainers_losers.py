import datetime as dt
import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr
yf.pdr_override()
from dateutil.relativedelta import *
from nsepy.history import get_price_list

start_52w=dt.datetime.now() + relativedelta(weeks=-52)
end=dt.datetime.now()

weeks_52 = pd.DataFrame(columns=['Company','Last Close','52-week-high','52-week-low'])

for s in nse_stocks.index:
    stock = str(nse_stocks['SYMBOL'][s])

    try:
        df_52w=pdr.get_data_yahoo(stock,start_52w,end)
        last_close = df_52w['Adj Close'][-1]
        pct_chg_max = df_52w['Adj Close'].max()
        pct_chg_min = df_52w['Adj Close'].min()

        weeks_52 = weeks_52.append({'Company':stock, 'Last Close':last_close, '52-week-high':pct_chg_max, '52-week-low':pct_chg_min},ignore_index=True)

    except:
        print("Ticker not available or delisted")

weeks_52_high = weeks_52.loc[weeks_52['Last Close']>=weeks_52['52-week-high']]
weeks_52_low = weeks_52.loc[weeks_52['Last Close']<=weeks_52['52-week-low']]

weeks_52_high.to_csv('52_week_high.csv')
weeks_52_low.to_csv('52_week_low.csv')        
