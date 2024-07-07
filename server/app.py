import os
import Pyro5.api
from dotenv import load_dotenv
from src.infra.database import DatabaseConnection
from src.repository.impl.rmi_server_sepository_impl import RmiServerRepositoryImpl
from src.repository.impl.rmi_server_auth_code_repository_impl import RmiServerAuthCodeRepositoryImpl
from src.utils.server_util import StartServer
from src.service.impl.video_control_impl import VideoControlImpl


def start_database_connection():
    db_conn = DatabaseConnection()

    DB_USER = os.getenv("DB_USER")
    DB_PASSWD = os.getenv("DB_PASSWD")
    DB_SEVER_NAME = os.getenv("DB_SEVER_NAME")
    DB_NAME = os.getenv("DB_NAME","museu")
    DB_PORT = os.getenv("DB_PORT",1433)

    connection_string = f"mssql+pymssql://{DB_USER}:{DB_PASSWD}@{DB_SEVER_NAME}:{DB_PORT}/{DB_NAME}"
    db_conn.initialize(connection_string)
    return db_conn.get_session()

def app_start(nm_server:str,nm_rmi_server_prefix:str):
    daemon = Pyro5.api.Daemon()
    ns = Pyro5.api.locate_ns()
    uri = daemon.register(VideoControlImpl)
    ns.register(f"{nm_rmi_server_prefix}.video_control", uri)
    session = start_database_connection()
    server_repo = RmiServerRepositoryImpl(session)
    server_auth_repo = RmiServerAuthCodeRepositoryImpl(session)
    server_data = StartServer(
        server_repo,
        server_auth_repo,
        nm_server,
        f"PYRONAME:{nm_rmi_server_prefix}"
    )
    data = server_data.start_server()
    print(data)
    print(f"{nm_server} is ready.")
    daemon.requestLoop()

if __name__ == "__main__":
    load_dotenv()
    nm_server = os.getenv("NM_RMI_SERVER")
    nm_rmi_server_prefix = os.getenv("NM_RMI_SERVER_URI_PREFIX")
    app_start(nm_server,nm_rmi_server_prefix)
