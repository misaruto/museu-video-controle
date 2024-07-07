import os
import Pyro5.api
from server.src.service.idle_video_control import VideoControl
from server.src.service.impl.video_control_impl import VideoControlImpl

def app_start(nm_server:str,nm_rmi_server_prefix:str):
    daemon = Pyro5.api.Daemon()
    ns = Pyro5.api.locate_ns()
    uri = daemon.register(VideoControlImpl)
    ns.register(f"{nm_rmi_server_prefix}.video_control", uri)
    print(f"{nm_server} is ready.")
    daemon.requestLoop()

if __name__ == "__main__":
    nm_server = os.getenv("NM_RMI_SERVER")
    nm_rmi_server_prefix = os.getenv("NM_RMI_SERVER_URI_PREFIX")
    app_start(nm_server,nm_rmi_server_prefix)
