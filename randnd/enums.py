import json
from enum import Enum

TYPE_DATA = "data/items/"


class Class:
    def __init__(self):
        with open(TYPE_DATA + "classes.json", "r") as f:
            data = "".join(f.readlines())

        self.classdata = json.loads(data)

        self.Fighter = self.classdata["fighter"]

    Rogue = 2
    Ranger = 3
    Barbarian = 4
    Druid = 5
    Cleric = 6
    Paladin = 7
    Bard = 8
    Warlock = 9
    Wizard = 10
    Sorcerer = 11
    Artificer = 12


class Gender(Enum):
    Male = 1
    Female = 2
    NonBinary = 3


class Background(Enum):
    Acolyte = 1
    Sage = 2
    Soldier = 3
    Charlatan = 4
    Criminal = 5
    FarWanderer = 6
    Noble = 7
    FolkHero = 8
    Entertainer = 9


class Race(Enum):
    Human = 1
    HumanVariant = 2
    Elf = 3
    HalfElf = 4
    Dwarf = 5
    Halfling = 6
    Gnome = 7
    HalfOrc = 8
    Orc = 9
    Dragonborn = 10
    Tiefling = 11


class Type(Enum):
    Humanoid = 1
    Fey = 2
    Celestial = 3
    Elemental = 4
    Infernal = 5


class Size(Enum):
    Tiny = 1
    Small = 2
    Medium = 3
    Large = 4
    Gargantual = 5  # TODO: fix?


class WeaponType(Enum):
    Martial = 1
    Melee = 2
    Sword = 3
    Polearm = 4
    Dagger = 5
    Quarterstaff = 6
    Longbow = 7
    ShortBow = 8
    HeavyCrossbow = 9
    LightCrossbow = 10


class ArmorType(Enum):
    Heavy = 1
    Medium = 2
    Light = 3
    Shield = 4


class ToolType(Enum):
    ThievesTools = 1
    # TODO


class Attribute(Enum):
    Strength = 1
    Dexterity = 2
    Constitution = 3
    Wisdom = 4
    Intelligence = 5
    Charisma = 6


class Skill(Enum):
    Athletics = 1
    AnimalHandling = 2
    Perception = 3
    Insight = 4
    Intimidation = 5
    Persuasion = 6
    History = 7
    Religion = 8
    Arcana = 9


class Language(Enum):
    Common = 1
    Elvish = 2
    Dwarvish = 3
    Gnomish = 4
    Halfling = 5
    Orcish = 6


class Feature(Enum):
    SecondWind = 1


class Equipment(Enum):
    ShortSword = 1


class Spell(Enum):
    Firebolt = 1
