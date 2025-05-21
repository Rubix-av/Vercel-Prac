from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

@app.get("/")
def root(name: List[str] = Query(...)):
  return {"names": name}
