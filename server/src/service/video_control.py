from abc import ABC, abstractmethod

class VideoControl(ABC):
    @abstractmethod
    def play(self):
        raise NotImplementedError
    
    @abstractmethod
    def pause(self):
        raise NotImplementedError
    
    @abstractmethod
    def stop(self):
        raise NotImplementedError


