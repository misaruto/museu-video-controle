import Pyro5.api
from server.src.service.idle_video_control import VideoControl
from server.src.service.impl.video_control_impl import VideoControlImpl

@Pyro5.api.expose
class VideoControlImpl(VideoControl):
    def __init__(self):
        self.server_video_control = None 
        self.video_path = ""
        self.video_status = "Unknow"

    def play(self,video_path):
        print("Play command received")
        self.server_video_control = VideoControlImpl(video_path)
        self.server_video_control.play()

    def pause(self):
        print("Pause command received")
        self.server_video_control.pause()
    def stop(self):
        print("Stop command received")
        self.server_video_control.stop()