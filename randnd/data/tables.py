from randnd.data.lib import Table, TABLE_FOLDER
from randnd.data.classes import Gender


class GenderTable(Table):
    def __init__(self):
        super().__init__("gendertable", TABLE_FOLDER + "genders.json")
        for i, v in self.table.items():
            self.table[i] = Gender(v)
