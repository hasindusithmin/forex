
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routers.yahoofinance import yf_router

app = FastAPI()

@app.get('/')
def root():
    return RedirectResponse('/docs')


app.include_router(yf_router)
