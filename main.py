from fastapi import FastAPI, HTTPException
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/all-champs")
async def get_all_champs():
    with open('AllChampsDetailed.json', 'r') as all_champs:
        return json.load(all_champs)


@app.get("/all-champ-names")
async def get_champ():
    champ_names = []
    with open('AllChampsDetailed.json', 'r') as all_champs:
        all_champs = json.load(all_champs)['data']
    for i in all_champs:
        champ_names.append(i)
    return champ_names


@app.get("/champion/{champion}")
async def get_champ(champion: str):
    with open('AllChampsDetailed.json', 'r') as all_champs:
        all_champs = json.load(all_champs)['data']
    # if champion exists
    if champion in all_champs:
        return all_champs[champion]
    else:
        raise HTTPException(status_code=404, detail="Champion not found")
