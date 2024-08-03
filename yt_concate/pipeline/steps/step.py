from abc import ABC
from abc import abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs):
        pass


class StepException(Exception):  # ---Exception 是Python 內建的 abstract method
    pass
