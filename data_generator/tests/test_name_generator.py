import pytest 
from src.data_generators.name_generator import NameGenerator 

@pytest.fixture 
def name_generator():
    return NameGenerator()

def test_generate_single_name(name_generator):
    name = name_generator.generate(count=1)
    assert isinstance(name, list)
    assert len(name) == 1
    assert isinstance(name[0], str)
    assert len(name[0]) > 0 


