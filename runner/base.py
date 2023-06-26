from abc import abstractmethod, ABCMeta


class Runner(metaclass=ABCMeta):
    def __init__(self):
        test = 1

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def reset(self):
        pass
