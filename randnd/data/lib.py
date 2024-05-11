import json

DATA_FOLDER = "data/items/"
TABLE_FOLDER = "data/tables/"


class Item:
    def __init__(self, name: str, filename: str, tablename: str = None):
        self.name = name

        with open(filename, "r") as f:
            data = "".join(f.readlines())

        self.data = json.loads(data)

        if tablename is not None:
            self.data = self.data[tablename]

    def __str__(self):
        return self.name

    def __repr__(self):
        return "'" + self.__str__() + "'"


class Table(Item):
    def __init__(self, name: str, filename: str, tablename: str = None):
        super().__init__(name, filename, tablename)

        self.size = self.data["size"]
        self.table = {}
        for item in self.data["items"]:
            for i in range(item["min"], item["max"] + 1):
                self.table[i] = item["data"]
