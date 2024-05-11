from enums import (
    Class,
    Gender,
    Background,
    Race,
    Type,
    Size,
    WeaponType,
    ArmorType,
    ToolType,
    Attribute,
    Skill,
    Language,
    Feature,
    Equipment,
    Spell,
)


class Character:
    def __init__(self):
        self.name: str
        self.age: int
        self.gender: Gender
        self.cclass: Class
        self.race: Race
        self.background: Background
        self.type: Type
        self.size: Size

        self.attributes: list[int, int, int, int, int, int]

        self.maxhealth: int
        self.hitdice: list[int, int]
        self.ac: int

        self.weapon_profs: set[WeaponType]
        self.armor_profs: set[ArmorType]
        self.tool_profs: set[ToolType]
        self.ability_profs: set[Attribute]
        self.skill_profs: set[Skill]
        self.languages: set[Language]

        self.features: set[Feature]

        self.equipment: list[Equipment]
        self.backpack: list[Equipment]

        self.spells: list[Spell]
        self.spellbook: list[Spell]
