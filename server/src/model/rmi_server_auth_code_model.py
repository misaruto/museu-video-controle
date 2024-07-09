from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from server.src.model.rmi_server_model import RmiServerModel

Base = declarative_base()

class RmiServerAuthCodeModel(Base):
    __tablename__ = 'rmi_server_auth_code'
    __table_args__ = {'schema': 'museu'}

    id_rmi_server_auth_code = Column(BigInteger, primary_key=True, autoincrement=True)
    id_rmi_server = Column(BigInteger, nullable=False)
    cd_rmi_server_auth = Column(String(6), nullable=False)
    dt_created = Column(DateTime, nullable=False, default=func.getdate())
    in_accessed = Column(Boolean, nullable=False, default=False)
    dt_accessed = Column(DateTime)

    __table_args__ = (
        PrimaryKeyConstraint('id_rmi_server_auth_code', name='PK_rmi_server_auth_code'),
        ForeignKeyConstraint(['id_rmi_server'], [RmiServerModel.id_rmi_server], name='FK01_rmi_server_auth_code_X_rmi_server')
    )
    def __repr__(self):
        return (
            f"<RmiServerAuthCodeModel(id_rmi_server_auth_code={self.id_rmi_server_auth_code}, "
            f"id_rmi_server={self.id_rmi_server}, cd_rmi_server_auth='{self.cd_rmi_server_auth}', "
            f"dt_created='{self.dt_created}', in_accessed={self.in_accessed}, "
            f"dt_accessed='{self.dt_accessed}')>"
        )