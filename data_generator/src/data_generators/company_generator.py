from faker import Faker 
import random
from .base_generator import BaseGenerator

class CompanyGenerator(BaseGenerator):
    def __init__(self):
        self.fake = Faker()

    def generate(self, count=1):
        return [self.fake.company() for _ in range(count)]

    def random_deletion(self, s):
        if len(s) == 0:
            return s 
        index_to_remove = random.randint(0, len(s) - 1)
        return s[:index_to_remove] + s[index_to_remove + 1:]

    def generate_mix_dataset(self):
        names_to_be_modified = self.generate(count=2)
        modified_names = [self.random_deletion(i) for i in names_to_be_modified]
        static_names = self.generate(count=10)

        return names_to_be_modified + modified_names + static_names



    