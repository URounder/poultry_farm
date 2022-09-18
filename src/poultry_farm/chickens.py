from datetime import datetime, date
    

class Flock:
    def __init__(self, name):
        self.the_flock = []
        self.name = name

    def add_to_flock(self, chicken):
        self.the_flock.append(chicken)


class Poultry:
    """A model to use for raising poultry."""
    class_counter = 0
    def __init__(self, birthday, type='chicken', breed='cornish_cross', sex='female', ):
        """Initialize the attributes"""
        self.id = Poultry.class_counter
        self.birthday = birthday
        self.type = type
        self.breed = breed
        self.sex = sex # Can I use a bool for this but user sees 'M/F'
        delta = datetime.today().date() - datetime.strptime(self.birthday, "%d/%m/%Y").date()  # (year, month, day)
        self.age = delta.days
        Poultry.class_counter += 1

    def __repr__(self):
        self.week = round(1 + (self.age / 7), 0)
        self.amount = daily_broiler_consumption[self.week]
        return f'''I am {self.type}:{self.id}, a {self.sex} {self.breed} and I am {self.age} days old.
        Following the week {int(self.week)} guidelines I will eat {self.amount} oz of food today.
        '''
    
    @classmethod
    def create_breed_chicken(cls, breed):
        pass

    @classmethod
    def make_chickens():
        for _ in range(30):
            flock.append(Poultry())


flock = []

daily_broiler_consumption = {
    1: 2.0,
    2: 2.0,
    3: 3.0,
    4: 3.0,
    5: 4.0,
    6: 4.0,
    7: 5.0,
    8: 6.0,
    9: 7.0,
    10: 8.0,
    11: 8.0,
    12: 8.0,
    }


flock_1 = {}

chicken_1 = Poultry("20/06/2022",'chicken','Big Red Broiler','female')
chicken_2 = Poultry("20/06/2022",'chicken','Big Red Broiler','male')

print(chicken_1)
print(chicken_2)
print(f'''Today the chickens are {chicken_1.week} weeks old and you need to feed
      them {(chicken_1.amount/16)*30} pounds of feed.''')

if __name__ == '__main__':
    pass