from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.functions import *

import app.dbConnection as dbc

app = FastAPI()

@app.get('/liveness')
def test():
    return True if dbc.get_connection() else False

@app.get('/first')
def firts(index_road: int) -> JSONResponse:
    return JSONResponse(content = get_first(index_road))

@app.get('/second')
def second(point_from, point_to) -> dict:
    return JSONResponse(content = get_second(point_from, point_to))

@app.get('/third')
def third(road, day_of_week, time_range, time_start, time_end, car_type, zone, transponder, transponder_type, tariff, direction):
    ans = get_third(road, day_of_week, time_range, time_start, time_end, car_type, zone, transponder, transponder_type, tariff, direction)
    return ans