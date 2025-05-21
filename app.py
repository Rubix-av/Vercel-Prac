from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/api")
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
