class User:
    def __init__(self, id, name, passwd):
        self.id = id
        self.name = name
        self.passwd = passwd


class Game:
    def __init__(self, name, category, game_console, id=None):
        self.id = id
        self.name = name
        self.category = category
        self.game_console = game_console

