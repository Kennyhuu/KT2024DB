import json
from fractions import Fraction
from typing import List

import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse

from interface import FractionCreate
from repository.postgres_function import PostgresFunction
app = FastAPI()

pos = PostgresFunction()


@app.post('/fraction_insert')
def insert_new_fraction(data: FractionCreate)-> int:
    new_id = pos.postgres_insert_operatives(data)
    return new_id


@app.post('/strategic_ploy_insert')
def insert_new_ploys(fk_id:int , data: dict):
   pos.postgres_insert_strategic(fk_id, data)

@app.get('/get_killteam')
def get_killteam(fraction_name: str):
    db_data = pos.post_get_fraction(fraction_name)
    print(db_data)
    for data in db_data:
        print(data)
        for id in data:
            print(id.name)


@app.get('/get_killteam_operatoive')
def get_killteam_operative(fraction_name: str):
    db_data = pos.post_get_operative(fraction_name)
    print(fraction_name)
    print(db_data)
    operative_list  = []
    for operatives_list in db_data:
        for op in operatives_list:
            operative_list .append({
                "name": op.name,
                "type": op.type,
                "stats": {
                    "APL": op.apl,
                    "MOVE": op.move,
                    "SAVE": op.save,
                    "WOUNDS": op.wounds
                },
                "weapons": op.weapons,
                "abilities": op.abilities
            })
    result = {
        "name": fraction_name,
        "operatives": operative_list
    }
    return JSONResponse(content=result)
