
from fastapi import APIRouter
import yfinance as yf

yf_router = APIRouter(
    prefix="/yahoo",
    tags=["yahoo finance"]
)
currency_cross_list = ['EURUSD=X', 'JPY=X', 'GBPUSD=X', 'AUDUSD=X', 'NZDUSD=X', 'EURJPY=X', 'GBPJPY=X', 'EURGBP=X', 'EURCAD=X', 'EURSEK=X', 'EURCHF=X', 'EURHUF=X', 'EURJPY=X', 'CNY=X', 'HKD=X', 'SGD=X', 'INR=X', 'MXN=X', 'PHP=X', 'IDR=X', 'THB=X', 'MYR=X', 'ZAR=X', 'RUB=X']

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

