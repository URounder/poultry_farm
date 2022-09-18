from .chickens import Flock,Poultry
from datetime import datetime, date


def test_chicken():
    my_test_chicken = Poultry("20/06/2022", type='duck',
                              breed='Rhode Island Red', sex='F')
    delta = datetime.today().date() - datetime.strptime(my_test_chicken.birthday, 
                                                        "%d/%m/%Y").date()
    assert my_test_chicken.breed == 'Rhode Island Red'
    assert my_test_chicken.age == my_test_chicken.age == delta.days

def test_flock():
    my_test_flock = Flock('birds')
    assert my_test_flock.name == 'birds'
    assert len(my_test_flock.the_flock) == 0
    my_test_chicken = Poultry("20/06/2022",'Rhode Island Red', 'F')
    my_test_flock.add_to_flock(my_test_chicken)
    assert len(my_test_flock.the_flock) == 1