from abc import ABC
from abc import abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
<<<<<<< HEAD
    def process(self, data, inputs):
        pass


class StepException(Exception):  # ---Exception 是Python 內建的 abstract method
=======
    def process(self, inputs):
        pass


class StepException (Exception):
>>>>>>> origin/main
    pass
