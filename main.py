
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routers.yahoofinance import yf_router
from routers.investing import invest_route

app = FastAPI()

@app.get('/')
def root():
    return RedirectResponse('/docs')


app.include_router(yf_router)
app.include_router(invest_route)
