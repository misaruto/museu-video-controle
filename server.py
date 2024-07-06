# server.py

import Pyro5.api
from common import VideoControl
from ServerVideoControlImpl import ServerVideoControlImpl

@Pyro5.api.expose
class VideoControlImpl(VideoControl):
    def __init__(self):
        self.server_video_control = None 
        self.video_path = ""
        self.video_status = "Unknow"

    def play(self,video_path):
        print("Play command received")
        self.server_video_control = ServerVideoControlImpl(video_path)
        self.server_video_control.play()

    def pause(self):
        print("Pause command received")
        self.server_video_control.pause()
    def stop(self):
        print("Stop command received")
        self.server_video_control.stop()

def main():
    daemon = Pyro5.api.Daemon()
    ns = Pyro5.api.locate_ns()
    uri = daemon.register(VideoControlImpl)
    ns.register("example.video_control", uri)
    print("Server is ready.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
