from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

<<<<<<< HEAD
    def run(self, inputs):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs)
            except StepException as e:
                print('Exception happened: ', e)
                break
=======
    def run (self, inputs):
        for step in steps:
            try:
                step.process(inputs)
            except StepException as e:
                print('Exception happened: ', e)
                break
>>>>>>> origin/main
