import json
from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field  # Field for adding metadata to model fields, Computed_Field for calculations
from typing import Annotated, Literal  # Annoted for adding description, Literal for fixed values


app=FastAPI()


class Patient(BaseModel):
    ## adding fields to the Patient model
    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]  
    ## ... means this field is required

    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kgs')]

    ## creating a computed field for BMI
    @computed_field
    @property
    def bmi(self) -> float:
        """Calculate Body Mass Index (BMI)"""
        bmi=round(self.weight / (self.height ** 2), 2)
        return bmi

    ## creating a computed field, so giving result of bmi ie, underweight, normal, overweight, obese
    @computed_field
    @property
    def verdict(self)-> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese'

def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)
    return data

## creating post method to add a new patient
@app.post('/create')
def create_patient(patient: Patient):

    # load existing data
    data = load_data()

    # check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')

    # if not then add new patient add to the database
    ## data is the variable and we need to add the patient(object) to the data,
    ## so we are using 'model_dump' to convert the patient object to a dictionary
    data[patient.id] = patient.model_dump(exclude=['id']) 
    ## here we exclude the old 'id' field, and create a new one

    # save into the json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message':'patient created successfully'})


def save_data(data):
    with open('patient.json', 'w') as f:
        json.dump(data, f, indent=4)  # indent=4 for pretty printing
   

## uvicorn main:app --reload