import Pyro5.api
import cv2
import threading
import time
import sys
from server.src.service.video_control import VideoControl

class VideoControlImpl(VideoControl):
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = None
        self.playing = False
        self.video_thread = None

    def play(self):
        if not self.playing:
            print("Playing video...")
            self.playing = True
            if self.video_thread is None:
                self.video_thread = threading.Thread(target=self._play_video)
                self.video_thread.start()
            elif not self.video_thread.is_alive():
                self.video_thread = threading.Thread(target=self._play_video)
                self.video_thread.start()

    def pause(self):
        print("Pausing video...")
        self.playing = False

    def stop(self):
        print("Stopping video...")
        self.playing = False
        if self.cap:
            self.cap.release()
            self.cap = None
        cv2.destroyAllWindows()

    def _play_video(self):
        self.cap = cv2.VideoCapture(self.video_path)
        while self.cap.isOpened():
            if self.playing:
                ret, frame = self.cap.read()
                if not ret:
                    break
                cv2.imshow('Video', frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                time.sleep(0.1)
        self.stop()
