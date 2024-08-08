import random
class BaseGenerator:
    def generate(self, count=1):
        raise NotImplementedError("This method should be overridden by subclasses")

    