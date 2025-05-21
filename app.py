from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()

# # Enable CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
#     allow_headers=["*"],  # Allow all headers
# )

@app.get("/api")
def root(name: List[str] = Query(...)):

    marks_list = []

    with open("q-vercel-python.json", "r") as f:
        data = json.load(f)

    flag = False

    for n in name:
      for details in data:
        if details["name"] == n.strip('"'):
          marks_list.append(details["marks"])
          break

    return { "marks": marks_list }
