from abc import ABC, abstractmethod
#abstract class
class abstractCleaner(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def cleaner(self,args):
        pass
        
    def __call__(self,args):
            return self.cleaner(args) # type: ignore