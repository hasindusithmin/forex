
from fastapi import APIRouter,HTTPException
import yfinance as yf
import json

yf_router = APIRouter(
    prefix="/yahoo",
    tags=["yahoo finance"]
)
currency_cross_list = ['eurusd', 'usdjpy', 'gbpusd', 'audusd', 'nzdusd', 'eurjpy', 'gbpjpy', 'eurgbp', 'eurcad', 'eursek', 'eurchf', 'eurhuf', 'eurjpy', 'usdcny', 'usdhkd', 'usdsgd', 'usdinr', 'usdmxn', 'usdphp', 'usdidr', 'usdthb', 'usdmyr', 'usdzar', 'usdrub']
currency_cross_dict = {'usdjpy': 'JPY=X', 'usdcny': 'CNY=X', 'usdhkd': 'HKD=X', 'usdsgd': 'SGD=X', 'usdinr': 'INR=X', 'usdmxn': 'MXN=X', 'usdphp': 'PHP=X', 'usdidr': 'IDR=X', 'usdthb': 'THB=X', 'usdmyr': 'MYR=X', 'usdzar': 'ZAR=X', 'usdrub': 'RUB=X', 'eurusd': 'EURUSD=X', 'gbpusd': 'GBPUSD=X', 'audusd': 'AUDUSD=X', 'nzdusd': 'NZDUSD=X', 'eurjpy': 'EURJPY=X', 'gbpjpy': 'GBPJPY=X', 'eurgbp': 'EURGBP=X', 'eurcad': 'EURCAD=X', 'eursek': 'EURSEK=X', 'eurchf': 'EURCHF=X', 'eurhuf': 'EURHUF=X'}
interval_list = ['5m','15m','30m','60m','1h']
@yf_router.get('/info/{currency_cross}')
async def get_info(currency_cross:str):
    currency_cross = currency_cross.strip()
    valid_cross = True if currency_cross in currency_cross_list else False
    if not valid_cross:
        raise HTTPException(status_code=404, detail='sorry currency cross not found')
    return yf.Ticker(currency_cross_dict[currency_cross]).info

@yf_router.get('/history/{currency_cross}')
async def get_candlestick(currency_cross:str,interval:str="5m"):
    currency_cross = currency_cross.strip()
    valid_cross = True if currency_cross in currency_cross_list else False
    if not valid_cross:
        raise HTTPException(status_code=404, detail='sorry currency cross not found')
    valid_interval = True if interval in interval_list else False
    if not valid_interval:
        raise HTTPException(status_code=404, detail='sorry interval not found')
    df = yf.Ticker(currency_cross_dict[currency_cross]).history(interval=interval,period="1mo")
    df = df.tail(500)
    df = df.reset_index()
    del df['Volume']
    del df['Dividends']
    del df['Stock Splits']
    candlestick = []
    for i in range(len(df)):
        candlestick.append(
            json.loads(
                df.iloc[i].to_json()
            )
        )
    return candlestick

@yf_router.get('/news/{currency_cross}')
async def get_news(currency_cross:str):
    currency_cross = currency_cross.strip()
    valid_cross = True if currency_cross in currency_cross_list else False
    if not valid_cross:
        raise HTTPException(status_code=404, detail='sorry currency cross not found')
    return yf.Ticker(currency_cross_dict[currency_cross]).news