from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

## annotated is used to add metadata to the fields in the model
## Field - validator is use to set the default value
class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]  ## Optional list of allergies, max 5 items
    contact_details: Dict[str, str]


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'rih', 'email':'rih@gmail.com', 'linkedin_url':'http://linkedin.com/', 
                'age': '30', 'weight': 75.2,'contact_details':{'phone':'9898989'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)