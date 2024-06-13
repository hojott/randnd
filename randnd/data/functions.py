from randnd.data.classes import Class, Background, Gender
from randnd.data.tables import GenderTable


def get_class(cclass: str):
    return Class(cclass)


def get_background(background: str):
    return Background(background)


def get_gender(gender: str):
    return Gender(gender)


def get_gender_table():
    return GenderTable().table
