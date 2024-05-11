from randnd.data.classes import Class, Gender


class Character:
    def __init__(self):
        self.name: str
        self.age: int
        self.gender: Gender
        self.cclass: Class
        self.race: str
        self.background: str
        self.type: str
        self.size: str

        self.attributes: list[int, int, int, int, int, int]

        self.maxhealth: int
        self.hitdice: list[int, int]
        self.ac: int

        self.weapon_profs: set[str]
        self.armor_profs: set[str]
        self.tool_profs: set[str]
        self.ability_profs: set[str]
        self.skill_profs: set[str]
        self.languages: set[str]

        self.features: set[str]

        self.equipment: list[str]
        self.backpack: list[str]

        self.spells: list[str]
        self.spellbook: list[str]
