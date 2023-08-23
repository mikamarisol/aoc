class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.parent = None

    def __str__(self):
        return self.name