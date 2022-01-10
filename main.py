# To run api:
# uvicorn main:app --reload
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = [
    "http://localhost:8080",
    # "http://192.168.0.139:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_credentials=True,
    # allow_methods=["*"],
    # allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/all-champs")
async def get_all_champ_data():
    with open('AllChampsDetailed.json', 'r') as all_champs:
        return json.load(all_champs)['data']


@app.get("/all-champ-names")
async def get_all_champ_names():
    champ_names = []
    with open('AllChampsDetailed.json', 'r') as all_champs:
        all_champs = json.load(all_champs)['data']
    for i in all_champs:
        champ_names.append(i)
    return champ_names


# Accepts spaces in request. ex: "miss fortune"
# case does not matter.
# Jarvan is "jarvan iv"
@app.get("/champion/{champion}")
async def get_champ_by_name(champion: str):
    champion = champion.lower()
    with open('AllChampsDetailed.json', 'r') as all_champs:
        all_champs = json.load(all_champs)['data']
    # if champion exists
    for champ in all_champs:
        # searches 'name' because of instances where other fields could be 'MonkeyKing' while name would be 'Wukong'.
        if champion in all_champs[champ]['name'].lower():
            # returns all data for 'champion'
            return all_champs[champ]
    else:
        raise HTTPException(status_code=404, detail="Champion not found.")


@app.get("/test-api")
async def test_api():
    return ''
