## Objective:
'''
    We are building an api that has following end-points:
        1. /create
        2. /view    (/raed)
        3. /view/<id>
        4./update/<id>
        5. /delete/<id>
'''

from fastapi import FastAPI
import json


app= FastAPI()

## function for loading the json data or read the json file
def load_data():
    with open("patient.json", "r") as f:
        data = json.load(f)
    return data



@app.get("/")
def hello():
    return {"message": "Patient Managements System"}

@app.get("/about")
def about():
    return{"message": "A fully functional Patient Management System API"}

## getting all the patients data
@app.get("/view")
def view():
    data=load_data()
    return data