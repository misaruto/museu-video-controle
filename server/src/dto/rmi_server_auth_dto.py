from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional
from src.model.rmi_server_auth_code_model import RmiServerAuthCodeModel

class RmiServerAuthCodeDto(BaseModel):
    idRmiServerAuthCode: Optional[int] = Field(None, description="ID do código de autenticação do servidor RMI")
    idRmiServer: Optional[int] = Field(None, description="ID do servidor RMI")
    cdRmiServerAuth: Optional[str] = Field(max_length=6, description="Código de autenticação do servidor RMI")
    dtCreated: Optional[datetime] = Field(None, description="Data de criação do código")
    inAccessed: bool = Field(False, description="Indica se o código foi acessado")
    dtAccessed: Optional[datetime] = Field(None, description="Data de acesso do código")

    @validator('cdRmiServerAuth')
    def code_must_be_six_chars(cls, v):
        if len(v) != 6:
            raise ValueError('O código de autenticação deve ter 6 caracteres')
        return v

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "idRmiServerAuthCode": 1,
                "idRmiServer": 1,
                "cdRmiServerAuth": "ABC123",
                "dtCreated": "2023-01-01T00:00:00",
                "inAccessed": False,
                "dtAccessed": None
            }
        }

    @classmethod
    def from_orm(cls, obj: RmiServerAuthCodeModel):
        return cls(
            idRmiServerAuthCode=obj.id_rmi_server_auth_code,
            idRmiServer=obj.id_rmi_server,
            cdRmiServerAuth=obj.cd_rmi_server_auth,
            dtCreated=obj.dt_rmi_server_auth_created,
            inAccessed=obj.in_rmi_server_auth_accessed,
            dtAccessed=obj.dt_rmi_server_auth_accessed
        )

    def to_orm(self) -> RmiServerAuthCodeModel:
        return RmiServerAuthCodeModel(
            id_rmi_server_auth_code=self.idRmiServerAuthCode,
            id_rmi_server=self.idRmiServer,
            cd_rmi_server_auth=self.cdRmiServerAuth,
            dt_rmi_server_auth_created=self.dtCreated,
            in_rmi_server_auth_accessed=self.inAccessed,
            dt_rmi_server_auth_accessed=self.dtAccessed
        )

class RmiServerAuthCodeRequestDto(BaseModel):
    rmiServerAuthCode: RmiServerAuthCodeDto

    class Config:
        json_schema_extra = {
            "example": {
                "rmiServerAuthCode": {
                    "idRmiServerAuthCode": 1,
                    "idRmiServer": 1,
                    "cdRmiServerAuth": "ABC123",
                    "dtCreated": "2023-01-01T00:00:00",
                    "inAccessed": False,
                    "dtAccessed": None
                }
            }
        }
class RmiServerAuthCodeResponseDto(BaseModel):
    rmiServerAuthCode: RmiServerAuthCodeDto

    class Config:
        json_schema_extra = {
            "example": {
                "rmiServerAuthCode": {
                    "idRmiServerAuthCode": 1,
                    "idRmiServer": 1,
                    "cdRmiServerAuth": "ABC123",
                    "dtCreated": "2023-01-01T00:00:00",
                    "inAccessed": False,
                    "dtAccessed": None
                }
            }
        }