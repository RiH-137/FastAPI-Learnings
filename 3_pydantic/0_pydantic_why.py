## pydantyc is used for type validation and serialization (str, int)
## pydantic is used for data validation and settings management using Python type annotations.

from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int

## dictionary --> correct
patient_info={
    "name":"John Doe",
    "age":30
}

## -->wrong
# patient_info={
#     "name":"John Doe",
#     "age":'thirty'  ## This will raise a validation error because 'thirty' is not an int
# }



patient1=Patient(**patient_info)            ## ** unpacking the dictionary into the Patient model



def insert_patient_data(patient: Patient):
    """
    Function to insert patient data into a database.
    This is a placeholder function and does not perform any actual database operations.
    """

    print(f"Inserting patient data: {patient.name}, {patient.age} years old")   
    print('inserted')


## calling the function
insert_patient_data(patient1)




## update
def update_patient_data(patient: Patient):
    """
    Function to update patient data in a database.
    This is a placeholder function and does not perform any actual database operations.
    """

    print(f"Updating patient data: {patient.name}, {patient.age} years old")
    print('updated')

## calling the update function
update_patient_data(patient1)