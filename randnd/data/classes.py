from randnd.data.lib import Item, DATA_FOLDER


class Class(Item):
    def __init__(self, classname: str):
        # TODO: make proper class instead of using dict
        super().__init__(classname, DATA_FOLDER + "classes.json", tablename=classname)


class Background(Item):
    def __init__(self, backgroundname: str):
        # TODO: make proper class instead of using dict
        super().__init__(
            backgroundname, DATA_FOLDER + "backgrounds.json", tablename=backgroundname
        )


class Gender(Item):
    def __init__(self, gender: str):
        super().__init__(gender, DATA_FOLDER + "genders.json", tablename=gender)
