
from fastapi import APIRouter
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
    try:
        currency_cross = f'{currency_cross.upper()}=X'
        can_done = True if currency_cross in currency_cross_list else False
        if not can_done:
            raise Exception("")
        return yf.Ticker(currency_cross).info
    except:
        return {
            "error":"currency cross not found"
        }

@yf_router.get('/history/{currency_cross}')
async def get_candlestick(currency_cross:str,interval:str):
    try:
        currency_cross = f'{currency_cross.upper()}=X'
        can_done = True if currency_cross in currency_cross_list and interval in interval_list else False
        if not can_done:
            raise Exception("")
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
    except:
        return {
            "error":"currency cross not found"
        }

