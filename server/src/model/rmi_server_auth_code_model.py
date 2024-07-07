from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint

Base = declarative_base()

class RmiServerAuthCodeModel(Base):
    __tablename__ = 'rmi_server_auth_code'
    __table_args__ = {'schema': 'museu'}

    id_rmi_server_auth_code = Column(BigInteger, primary_key=True, autoincrement=True)
    id_rmi_server = Column(BigInteger, ForeignKey('museu.rmi_server.id_rmi_server'), nullable=False)
    cd_rmi_server_auth = Column(String(6), nullable=False)
    in_accessed = Column(Boolean, nullable=False, default=False)
    dt_created = Column(DateTime, nullable=False, default=func.getdate())

    __table_args__ = (
        PrimaryKeyConstraint('id_rmi_server_auth_code', name='PK_rmi_server_auth_code'),
        ForeignKeyConstraint(['id_rmi_server'], ['museu.rmi_server.id_rmi_server'], name='FK01_rmi_server_auth_code_X_rmi_server')
    )
