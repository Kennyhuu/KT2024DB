from fractions import Fraction
from typing import List

import uvicorn
from fastapi import FastAPI

from interface import FractionCreate
from repository.postgres_function import PostgresFunction
app = FastAPI()

pos = PostgresFunction()


@app.post('/fraction_insert')
def insert_new_fraction(data: FractionCreate)-> int:
    new_id = pos.postgres_insert_operatives(data)
    return new_id


@app.post('/strategic_ploy')
def insert_new_ploys(fk_id:int , data: dict):
   pos.postgres_insert_poly(fk_id, data)
