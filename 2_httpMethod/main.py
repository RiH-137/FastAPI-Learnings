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
from fastapi import Path
from fastapi import HTTPException
from fastapi import Query

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
@app.get("/view_all")
def view():
    data=load_data()
    return data


## getting a patient data by id, id is dynamic in nature, anbd id is called as path parameter
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str):
    # load the data from json file
    data=load_data()

    if patient_id in data:
        return data[patient_id] ## list of patients
    else:
        return {"error": "Patient not found"}


## getting a patient data by id, using 'Path' function; ... indicates that this parameter is required
@app.get("/patientPath/{patient_id}")
def view_patient(patient_id: str=Path(..., description="The ID of the patient to view", example="P0001")):
    # load the data from json file
    data=load_data()

    if patient_id in data:
        return data[patient_id] ## list of patients
    else:
        return {"error": "Patient not found"}



## if the query asked by the user is not found, return 404 error/ status code
@app.get("/patient_withException/{patient_id}")
def view_patient_with_exception(patient_id: str):
    # load the data from json file
    data=load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")



## query parameter
### allow the user to sort by height/ weight/ bmi in ascending (default) or descending order (optional)
@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data
