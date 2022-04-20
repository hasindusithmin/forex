
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routers.yahoofinance import yf_router
from routers.investing import invest_route

description ="""
Valid currency_cross for Both\n
['eurusd', 'usdjpy', 'gbpusd', 'audusd', 'nzdusd', 'eurjpy', 'gbpjpy', 'eurgbp', 'eurcad', 'eursek', 'eurchf', 'eurhuf', 'eurjpy', 'usdcny', 'usdhkd', 'usdsgd', 'usdinr', 'usdmxn', 'usdphp', 'usdidr', 'usdthb', 'usdmyr', 'usdzar', 'usdrub']\n
Valid Interval for Yahoo Finance\n
['5m','15m','30m','60m','1h']\n
Valid Timeframe For investing.com\n
['5mins', '15mins', '30mins','lhour']\n
#github : https://github.com/hasindusithmin/forex.git
"""

app = FastAPI(
    title="forexapi",
    description=description,
    version="0.0.1",
    contact={
        "name": "Hasindu Sithmin",
        "email": "hasindusithmin64@gmail.com",
    }
)

@app.get('/')
def root():
    return RedirectResponse('/docs')


app.include_router(yf_router)
app.include_router(invest_route)
