
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from routers.yahoofinance import yf_router
from routers.investing import invest_route

description ="""
Code Unity Forex API helps you do awesome stuff. 🚀

## Valid currency_cross for Both

['eurusd', 'usdjpy', 'gbpusd', 'audusd', 'nzdusd', 'eurjpy', 'gbpjpy', 'eurgbp', 'eurcad', 'eursek', 'eurchf', 'eurhuf', 'eurjpy', 'usdcny', 'usdhkd', 'usdsgd', 'usdinr', 'usdmxn', 'usdphp', 'usdidr', 'usdthb', 'usdmyr', 'usdzar', 'usdrub']\n

## Valid Interval for Yahoo Finance

['5m','15m','30m','60m','1h']

## Valid Timeframe For investing.com

['5mins', '15mins', '30mins','lhour']


"""

app = FastAPI(
    title="ForexApi",
    description=description,
    version="0.0.3",
    contact={
        "name": "Hasindu Sithmin",
        "email": "hasindusithmin64@gmail.com",
    },
    license_info={
        "name": "github",
        "url": "https://github.com/hasindusithmin/forex",
    },
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return RedirectResponse('/docs')


app.include_router(yf_router)
app.include_router(invest_route)
