from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional
from src.model.rmi_server_session_model import RmiServerSessionModel

class RmiServerSessionDto(BaseModel):
    idRmiServerSession: Optional[int] = Field(None, description="ID da sessão do servidor RMI")
    idRmiServerAuthCode: int = Field(..., description="ID do código de autenticação do servidor RMI")
    inRmiServerSessionExpired: bool = Field(False, description="Indica se a sessão do servidor RMI expirou")
    cdRmiServerSessionToken: str = Field(..., max_length=36, description="Token da sessão do servidor RMI")
    qtSessionDurationSeconds: Optional[int] = Field(None, description="Duração da sessão em segundos")
    dtfExpectedRmiServerSession: datetime = Field(..., description="Data esperada de expiração da sessão")
    dtfRmiServerSession: Optional[datetime] = Field(None, description="Data real de expiração da sessão")
    dtCreated: Optional[datetime] = Field(None, description="Data de criação da sessão")
    nmUserCreatedSession: Optional[str] = Field(None, max_length=30, description="Nome do usuário que criou a sessão")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "idRmiServerSession": 1,
                "idRmiServerAuthCode": 1,
                "inRmiServerSessionExpired": False,
                "cdRmiServerSessionToken": "123e4567-e89b-12d3-a456-426614174000",
                "qtSessionDurationSeconds": 3600,
                "dtfExpectedRmiServerSession": "2023-01-01T00:00:00",
                "dtfRmiServerSession": None,
                "dtCreated": "2023-01-01T00:00:00",
                "nmUserCreatedSession": "user1"
            }
        }

    @classmethod
    def from_orm(cls, obj: RmiServerSessionModel):
        return cls(
            idRmiServerSession=obj.id_rmi_server_session,
            idRmiServerAuthCode=obj.id_rmi_server_auth_code,
            inRmiServerSessionExpired=obj.in_rmi_server_session_expired,
            cdRmiServerSessionToken=obj.cd_rmi_server_session_token,
            qtSessionDurationSeconds=obj.qt_session_duration_seconds,
            dtfExpectedRmiServerSession=obj.dtf_expected_rmi_server_session,
            dtfRmiServerSession=obj.dtf_rmi_server_session,
            dtCreated=obj.dt_rmi_server_session_created,
            nmUserCreatedSession=obj.nm_user_created_session
        )

    def to_orm(self) -> RmiServerSessionModel:
        return RmiServerSessionModel(
            id_rmi_server_session=self.idRmiServerSession,
            id_rmi_server_auth_code=self.idRmiServerAuthCode,
            in_rmi_server_session_expired=self.inRmiServerSessionExpired,
            cd_rmi_server_session_token=self.cdRmiServerSessionToken,
            qt_session_duration_seconds=self.qtSessionDurationSeconds,
            dtf_expected_rmi_server_session=self.dtfExpectedRmiServerSession,
            dtf_rmi_server_session=self.dtfRmiServerSession,
            dt_rmi_server_session_created=self.dtCreated,
            nm_user_created_session=self.nmUserCreatedSession
        )

class RmiServerSessionRequestDto(BaseModel):
    rmiServerSession: RmiServerSessionDto

    class Config:
        json_schema_extra = {
            "example": {
                "rmiServerSession": {
                    "idRmiServerSession": 1,
                    "idRmiServerAuthCode": 1,
                    "inRmiServerSessionExpired": False,
                    "cdRmiServerSessionToken": "123e4567-e89b-12d3-a456-426614174000",
                    "qtSessionDurationSeconds": 3600,
                    "dtfExpectedRmiServerSession": "2023-01-01T00:00:00",
                    "dtfRmiServerSession": None,
                    "dtCreated": "2023-01-01T00:00:00",
                    "nmUserCreatedSession": "user1"
                }
            }
        }

class RmiServerSessionResponseDto(BaseModel):
    rmiServerSession: RmiServerSessionDto

    class Config:
        json_schema_extra = {
            "example": {
                "rmiServerSession": {
                    "idRmiServerSession": 1,
                    "idRmiServerAuthCode": 1,
                    "inRmiServerSessionExpired": False,
                    "cdRmiServerSessionToken": "123e4567-e89b-12d3-a456-426614174000",
                    "qtSessionDurationSeconds": 3600,
                    "dtfExpectedRmiServerSession": "2023-01-01T00:00:00",
                    "dtfRmiServerSession": None,
                    "dtCreated": "2023-01-01T00:00:00",
                    "nmUserCreatedSession": "user1"
                }
            }
        }
