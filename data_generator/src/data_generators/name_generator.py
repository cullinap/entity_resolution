from faker import Faker 
from .base_generator import BaseGenerator

class NameGenerator(BaseGenerator):
    def __init__(self):
        self.fake = Faker()

    def generate(self, count=1):
        return [self.fake.name() for _ in range(count)]