from fastapi import FastAPI, HTTPException
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/all-champs")
async def get_all_champ_data():
    with open('AllChampsDetailed.json', 'r') as all_champs:
        return json.load(all_champs)


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
