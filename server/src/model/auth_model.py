from pydantic import BaseModel

class AuthRequestModel(BaseModel):
  cdAuthCode:str
  nmUsername:str

