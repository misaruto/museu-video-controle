from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional
from src.model.rmi_server_model import RmiServerModel


class RmiServerDto(BaseModel):
    idRmiServer: Optional[int] = Field(None, description="ID do servidor RMI")
    nmRmiServer: str = Field(..., max_length=30, description="Nome do servidor RMI")
    nmRmiServerUri: str = Field(..., max_length=60, description="URI do servidor RMI")
    dtCreated: Optional[datetime] = Field(None, description="Data de criação do servidor")
    dtDisabled: Optional[datetime] = Field(None, description="Data de desativação do servidor")
    inActive: bool = Field(True, description="Indica se o servidor está ativo")

    @validator('nmRmiServer', 'nmRmiServerUri')
    def must_not_be_empty(cls, v):
        if not v or v.strip() == "":
            raise ValueError('Campo não pode ser vazio')
        return v

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "idRmiServer": 1,
                "nmRmiServer": "ExampleServer",
                "nmRmiServerUri": "http://example.com/server",
                "dtCreated": "2023-01-01T00:00:00",
                "dtDisabled": None,
                "inActive": True
            }
        }

    @classmethod
    def from_orm(cls, obj: RmiServerModel):
        return cls(
            idRmiServer=obj.id_rmi_server,
            nmRmiServer=obj.nm_rmi_server,
            nmRmiServerUri=obj.nmRmiServerUri,
            dtCreated=obj.dt_created,
            dtDisabled=obj.dt_disabled,
            inActive=obj.in_active
        )

    def to_orm(self) -> RmiServerModel:
        return RmiServerModel(
            id_rmi_server=self.idRmiServer,
            nm_rmi_server=self.nm_rmi_server,
            nm_rmi_server_uri=self.nmRmiServerUri,
            dt_created=self.dtCreated,
            dt_disabled=self.dtDisabled,
            in_active=self.inActive
        )

class RmiServerRequestDto(BaseModel):
    rmiServer: RmiServerDto

    class Config:
        schema_extra = {
            "example": {
                "rmiServer": {
                    "idRmiServer": 1,
                    "nmRmiServer": "ExampleServer",
                    "nmRmiServerUri": "http://example.com/server",
                    "dtCreated": "2023-01-01T00:00:00",
                    "dtDisabled": None,
                    "inActive": True
                }
            }
        }