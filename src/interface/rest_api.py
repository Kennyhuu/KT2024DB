from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from interface import FractionCreate
from repository.postgres_function import PostgresFunction
app = FastAPI()

# CORS to allow other port
origins = [
    "http://localhost:3000",  # React dev server origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allow this origin to make requests
    allow_credentials=True,
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)
pos = PostgresFunction()


@app.post('/fraction_insert')
def insert_new_fraction(data: FractionCreate)-> int:
    new_id = pos.postgres_insert_operatives(data)
    return new_id


@app.post('/strategic_ploy_insert')
def insert_new_ploys(fk_id:int , data: dict):
   pos.postgres_insert_strategic(fk_id, data)

@app.get('/get_killteam')
def fetch_all_fraction_from_database():
    db_data = pos.postgres_fetch_fraction()
    fractions_list = []
    for data in db_data:
        for fraction in data:
            fractions_list.append({
                'fraction_id': fraction.id,
                'fraction':fraction.name
            })

    return JSONResponse(fractions_list)


@app.get('/get_killteam_operative')
def fetch_killteam_operative(fraction_name: str):
    db_data = pos.post_get_operative(fraction_name)
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
