# common.py
import Pyro5.api

@Pyro5.api.expose
class VideoControl:
    def play(self):
        pass

    def pause(self):
        pass

    def stop(self):
        pass


