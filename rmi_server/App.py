import os
import Pyro5.api
from dotenv import load_dotenv
from handlers.video_control_handler import VideoControlHandler


def app_start(nm_server:str,nm_rmi_server_prefix:str):
    daemon = Pyro5.api.Daemon()
    ns = Pyro5.api.locate_ns()
    uri = daemon.register(VideoControlHandler)
    ns.register(f"{nm_rmi_server_prefix}.video_control", uri)
    print("Server ready waiting for connections")
    daemon.requestLoop()

if __name__ == "__main__":
    load_dotenv()
    nm_server = os.getenv("NM_RMI_SERVER")
    nm_rmi_server_prefix = os.getenv("NM_RMI_SERVER_URI_PREFIX")
    app_start(nm_server,nm_rmi_server_prefix)