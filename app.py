from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

@app.get("/")
def root(name: List[str] = Query(...)):
  name1, name2 = name["names"][0], name["names"][1]
  return {"name1": name1, "name2": name2}
