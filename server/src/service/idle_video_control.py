from abc import ABC, abstractmethod

class IdleVideoControl(ABC):
    @abstractmethod
    def play():
        raise NotImplementedError
    
    @abstractmethod
    def stop():
        raise NotImplementedError

