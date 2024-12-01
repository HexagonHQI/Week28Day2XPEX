#Ex1:
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}' + ('s' if self.amount != 1 else '')

    def __repr__(self):
        return f'{self.amount} {self.currency}' + ('s' if self.amount != 1 else '')

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                return Currency(self.currency, self.amount + other.amount)
            else:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        elif isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        else:
            raise TypeError("Invalid type for addition")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount += other.amount
            else:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        elif isinstance(other, int):
            self.amount += other
        else:
            raise TypeError("Invalid type for addition")
        return self
#Ex2:

#For this ex i have to open two files in Vscode and because i do all XP exercises together, i'll write it like that:

#First file func.py:
def sum_two_numbers(a, b):
    result = a + b
    print(f"The result of adding {a} and {b} is {result}")
#Second file One.py
from func import sum_two_numbers

sum_two_numbers(5, 10)

#Ex3:
import random
import string

def generate_random_string(length=5):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

print(generate_random_string())
#Ex4:
from datetime import datetime

def display_current_date():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

display_current_date()
#Ex4:
from datetime import datetime

def time_left_until_new_year():
    now = datetime.now()
    next_new_year = datetime(now.year + 1, 1, 1)
    time_left = next_new_year - now
    print(f"Time left until January 1st: {time_left}")

time_left_until_new_year()
#Ex5:
from datetime import datetime

def minutes_lived(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    now = datetime.now()
    delta = now - birthdate
    minutes_lived = delta.total_seconds() / 60
    print(f"You have lived {int(minutes_lived)} minutes.")


minutes_lived('1990-01-01')
#Ex6:
from datetime import datetime

def minutes_lived(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    now = datetime.now()
    delta = now - birthdate
    minutes_lived = delta.total_seconds() / 60
    print(f"You have lived {int(minutes_lived)} minutes.")


minutes_lived('1990-01-01')
#Ex7:
from faker import Faker

fake = Faker()

users = []

def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)


for _ in range(3):
    add_user()

print(users)
