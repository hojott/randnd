import json

from enums import Gender

TABLE_DATA = "data/tables/"


class Table:
    def __init__(self, filename, tablename=None):
        with open(filename, "r") as f:
            data = "".join(f.readlines())

        data = json.loads(data)

        if tablename is not None:
            data = data[tablename]

        self.size = data["size"]
        self.table = {}
        for item in data["items"]:
            for i in range(item["min"], item["max"] + 1):
                self.table[i] = item["data"]


class GenderTable(Table):
    def __init__(self):
        super().__init__(TABLE_DATA + "generic.json", tablename="gender")
        for i, v in self.table.items():
            if v == "male":
                self.table[i] = Gender.Male
            elif v == "female":
                self.table[i] = Gender.Female
            elif v == "nonbinary":
                self.table[i] = Gender.NonBinary
            else:
                raise Exception(
                    "Uhhhh please don't add to the gender table. It's work in progress!"
                )
