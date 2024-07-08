from pydantic import BaseModel


class SessionResponseModel(BaseModel):
  cdSessionToken:str
  nmUserName:str
  qtSessionDurationSeconds:int
  dtfSession:str