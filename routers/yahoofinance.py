
from fastapi import APIRouter,HTTPException
import yfinance as yf
import json

yf_router = APIRouter(
    prefix="/yahoo",
    tags=["yahoo finance"]
)
currency_cross_list = ['EURUSD=X', 'JPY=X', 'GBPUSD=X', 'AUDUSD=X', 'NZDUSD=X', 'EURJPY=X', 'GBPJPY=X', 'EURGBP=X', 'EURCAD=X', 'EURSEK=X', 'EURCHF=X', 'EURHUF=X', 'EURJPY=X', 'CNY=X', 'HKD=X', 'SGD=X', 'INR=X', 'MXN=X', 'PHP=X', 'IDR=X', 'THB=X', 'MYR=X', 'ZAR=X', 'RUB=X']
interval_list = ['5m','15m','30m','60m','1h']
@yf_router.get('/info/{currency_cross}')
async def get_info(currency_cross:str):
    currency_cross = f'{currency_cross.upper()}=X'
    valid_cross = True if currency_cross in currency_cross_list else False
    if not valid_cross:
        raise HTTPException(status_code=404, detail='sorry currency cross not found')
    return yf.Ticker(currency_cross).info
@yf_router.get('/history/{currency_cross}')
async def get_candlestick(currency_cross:str,interval:str="5m"):
    currency_cross = f'{currency_cross.upper()}=X'
    valid_cross = True if currency_cross in currency_cross_list else False
    if not valid_cross:
        raise HTTPException(status_code=404, detail='sorry currency cross not found')
    valid_interval = True if interval in interval_list else False
    if not valid_interval:
        raise HTTPException(status_code=404, detail='sorry interval not found')
    df = yf.Ticker(currency_cross).history(interval=interval,period="1mo")
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
    currency_cross = f'{currency_cross.upper()}=X'
    valid_cross = True if currency_cross in currency_cross_list else False
    if not valid_cross:
        raise HTTPException(status_code=404, detail='sorry currency cross not found')
    return yf.Ticker(currency_cross).news