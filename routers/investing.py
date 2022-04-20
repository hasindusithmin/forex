
from fastapi import APIRouter,HTTPException
import investpy
import json

currency_cross_list = ['EUR/USD', 'USD/JPY', 'GBP/USD', 'AUD/USD', 'NZD/USD', 'EUR/JPY', 'GBP/JPY', 'EUR/GBP', 'EUR/CAD', 'EUR/SEK', 'EUR/CHF', 'EUR/HUF', 'EUR/JPY', 'USD/CNY', 'USD/HKD', 'USD/SGD', 'USD/INR', 'USD/MXN', 'USD/PHP', 'USD/IDR', 'USD/THB', 'USD/MYR', 'USD/ZAR', 'USD/RUB']
timeframe_list = ['5mins', '15mins', '30mins','lhour']
invest_route = APIRouter(
    prefix='/invest',
    tags=['investing.com']
)

@invest_route.get('/moving_averages/{currency_cross}')
async def get_moving_averages(currency_cross:str,timeframe:str="5mins"):
    currency_cross = f'{currency_cross[:3]}/{currency_cross[3:]}'.upper()
    valid_cross = True if currency_cross in currency_cross_list else False
    if not valid_cross:
        raise HTTPException(status_code=404, detail='sorry currency cross not found')
    valid_timeframe = True if timeframe in timeframe_list else False
    if not valid_timeframe:
        raise HTTPException(status_code=404, detail='sorry time frame not found')
    df = investpy.technical.moving_averages(name=currency_cross, country=None, product_type='currency_cross', interval=timeframe)
    moving_averages = []
    for i in range(len(df)):
        moving_averages.append(
            json.loads(
                df.iloc[i].to_json()
            )
        ) 
    return moving_averages

@invest_route.get('/pivot_points/{currency_cross}')
async def get_pivot_points(currency_cross:str,timeframe:str="5mins"):
    currency_cross = f'{currency_cross[:3]}/{currency_cross[3:]}'.upper()
    valid_cross = True if currency_cross in currency_cross_list else False
    if not valid_cross:
        raise HTTPException(status_code=404, detail='sorry currency cross not found')
    valid_timeframe = True if timeframe in timeframe_list else False
    if not valid_timeframe:
        raise HTTPException(status_code=404, detail='sorry time frame not found')
    df = investpy.technical.pivot_points(name=currency_cross, country=None, product_type='currency_cross', interval=timeframe)
    pivot_points = []
    for i in range(len(df)):
        pivot_points.append(
            json.loads(
                df.iloc[i].to_json()
            )
        ) 
    return pivot_points

@invest_route.get('/technical_indicators/{currency_cross}')
async def get_technical_indicators(currency_cross:str,timeframe:str="5mins"):
    currency_cross = f'{currency_cross[:3]}/{currency_cross[3:]}'.upper()
    valid_cross = True if currency_cross in currency_cross_list else False
    if not valid_cross:
        raise HTTPException(status_code=404, detail='sorry currency cross not found')
    valid_timeframe = True if timeframe in timeframe_list else False
    if not valid_timeframe:
        raise HTTPException(status_code=404, detail='sorry time frame not found')
    df = investpy.technical.technical_indicators(name=currency_cross, country=None, product_type='currency_cross', interval=timeframe)
    technical_indicators = []
    for i in range(len(df)):
        technical_indicators.append(
            json.loads(
                df.iloc[i].to_json()
            )
        ) 
    return technical_indicators

@invest_route.get('/economic_calendar')
async def get_economic_calendar():
    df = investpy.economic_calendar()
    economic_calendar = []
    for i in range(len(df)):
        economic_calendar.append(
            json.loads(
                df.iloc[i].to_json()
            )
        )
    return economic_calendar