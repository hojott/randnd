import random

from randnd.character import Character

from randnd.data.functions import get_gender_table


def dice(max: int, amount=1) -> int:
    sum = 0
    for _ in range(amount):
        sum += random.randint(1, max)
    return sum


class Randomizer:
    def __init__(self, seed=random.random()):
        self.character = Character()
        random.seed(seed)

    def generate_name(self):
        """Gender, race and background should be generated first"""

    def generate_gender(self):
        gender_table = get_gender_table()
        self.character.gender = gender_table[dice(100)]
