import os
import vlc
import time

class VideoService:
  def __init__(self,callback):
    self.is_paused = False
    self.video_paht = f"{os.getenv('PATH_VIDEO')}/{os.getenv('NM_VIDEO')}"
    self.instance = vlc.Instance()
    self.midia_player =  self.instance.media_player_new()
    self.midia_player.set_media(self.instance.media_new(self.video_paht))
    self.__attacht_event_to_player(callback) 


  def play(self):
    if self.is_playing():
      return
    self.midia_player.play()
    time.sleep(0.3)
    if not self.is_paused:
      self.midia_player.toggle_fullscreen()
    else:
      self.is_paused = False
  
  
  def pause(self):
    if not self.midia_player:
      raise Exception("Nenhum video sendo exibido")
    if not self.is_paused:
      self.midia_player.pause()
      self.is_paused = True
  
  def stop(self):
    if not self.midia_player:
      raise Exception("Nenhum video sendo exibido")
    self.midia_player.stop()
    self.midia_player = None
    
  def is_playing(self):
    if not self.midia_player:
      return False
    return self.midia_player.is_playing()
  

  def __attacht_event_to_player(self,callback):
    self.event_manager = self.midia_player.event_manager()
    self.event_manager.event_attach(vlc.EventType.MediaPlayerEndReached,callback)
    # self.event_manager.event_attach(vlc.EventType.MediaPlayerPlaying,VideoService.on_video_start)
