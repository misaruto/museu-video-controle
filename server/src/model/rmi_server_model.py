from sqlalchemy.schema import PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, func

Base = declarative_base()

class RmiServerModel(Base):
    __tablename__ = 'rmi_server'
    __table_args__ = {'schema': 'museu'}

    id_rmi_server = Column(BigInteger, primary_key=True, autoincrement=True)
    nm_rmi_server = Column(String(30), nullable=False)
    nm_rmi_server_uri = Column(String(60), nullable=False)
    dt_created = Column(DateTime, nullable=False, default=func.getdate())
    dt_disabled = Column(DateTime, nullable=True)
    in_active = Column(Boolean, nullable=False, default=True)

    __table_args__ = (
        PrimaryKeyConstraint('id_rmi_server', name='PK_rmi_server'),
    )