import yfinance

from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()

@app.get("/stocks")
def get_stock_prices():
    """get data"""
    pass

