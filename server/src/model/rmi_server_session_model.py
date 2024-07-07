from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from src.model.rmi_server_auth_code_model import RmiServerAuthCodeModel
Base = declarative_base()

class RmiServerSessionModel(Base):
    __tablename__ = 'rmi_server_session'
    __table_args__ = {'schema': 'museu'}

    id_rmi_server_session = Column(BigInteger, primary_key=True, autoincrement=True)
    id_rmi_server_auth_code = Column(BigInteger, ForeignKey('museu.rmi_server_auth_code.id_rmi_server_auth_code'), nullable=False)
    in_rmi_server_session_expired = Column(Boolean, nullable=False, default=False)
    dtf_expected_rmi_server_session = Column(DateTime, nullable=False)
    dtf_rmi_server_session = Column(DateTime, nullable=True)
    dt_created = Column(DateTime, nullable=False, default=func.getdate())
    nm_user_created_session = Column(String(30), nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id_rmi_server_session', name='PK_rmi_server_session'),
        ForeignKeyConstraint(['id_rmi_server_auth_code'], [RmiServerAuthCodeModel.id_rmi_server_auth_code], name='FK01_rmi_server_session_X_rmi_server_auth_code')
    )
    def __repr__(self):
        return (
            f"<RmiServerSessionModel(id_rmi_server_session={self.id_rmi_server_session}, "
            f"id_rmi_server_auth_code={self.id_rmi_server_auth_code}, "
            f"in_rmi_server_session_expired={self.in_rmi_server_session_expired}, "
            f"dtf_expected_rmi_server_session='{self.dtf_expected_rmi_server_session}', "
            f"dtf_rmi_server_session='{self.dtf_rmi_server_session}', "
            f"dt_created='{self.dt_created}', "
            f"nm_user_created_session='{self.nm_user_created_session}')>"
        )