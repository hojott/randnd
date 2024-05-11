import random

from character import Character

from tables import gender


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
        self.character.gender = gender[dice(100)]
