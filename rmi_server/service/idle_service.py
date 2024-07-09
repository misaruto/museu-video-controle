import subprocess

class IdleService:
  def __init__(self) -> None:
    
    self.subproccess = None
    self.idle_gif = './assets/idle.gif'
    self.command = ["python",'./utils/idle_utils.py']

  def start_idle(self,code):
    if not self.subproccess:
      self.subproccess = subprocess.Popen([*self.command,code,self.idle_gif])
  def stop_idle(self):
    self.subproccess.kill()
    self.subproccess = None