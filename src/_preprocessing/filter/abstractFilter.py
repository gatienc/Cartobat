from abc import ABC, abstractmethod
#abstract class
class abstractFilter(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def filter(self,args):
        pass
        
    def __call__(self,args):
            return filter(args) # type: ignore