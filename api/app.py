from fastapi import FastAPI, Query
from typing import List
import json

app = FastAPI()

@app.get("/")
def root(name: List[str] = Query(...)):
  
  name1, name2 = name[0].strip('"'), name[1].strip('"')
  
  marks_list = []
  
  with open("q-vercel-python.json", "r") as f:
    data = json.load(f)  
  
  flag = False

  for details in data:
    if details["name"] == name1:
      marks_list.append(details["marks"])
      flag = True
    
    if flag == True and details["name"] == name2:
      marks_list.append(details["marks"])
    
  return {"marks": marks_list}
