import os
import Pyro5.api
from dotenv import load_dotenv
from handlers.video_control_handler import VideoControlHandler
from handlers.idle_handler import IdleService
from utils.start_server import server_registry
from service.idle_service import IdleService

def app_start(nm_server:str,nm_rmi_server_prefix:str):
    daemon = Pyro5.api.Daemon()
    ns = Pyro5.api.locate_ns()
    idle_handler = IdleService()
    video_control = VideoControlHandler(idle_handler,nm_server)
    video_controler_uri = daemon.register(video_control)
    ns.register(f"{nm_rmi_server_prefix}.video_handler", video_controler_uri)
    
    idle_handler = IdleService()
    idle_handler_uri = daemon.register(idle_handler)
    ns.register(f"{nm_rmi_server_prefix}.idle_handler", idle_handler_uri)
    
    server_registry(nm_server,f"PYRONAME:{nm_rmi_server_prefix}",idle_handler)
    print("Server ready waiting for connections")
    daemon.requestLoop()

if __name__ == "__main__":
    load_dotenv()
    nm_server = os.getenv("NM_RMI_SERVER")
    nm_rmi_server_prefix = os.getenv("NM_RMI_SERVER_URI_PREFIX")
    app_start(nm_server,nm_rmi_server_prefix)