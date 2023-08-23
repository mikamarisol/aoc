class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.parent = None

    def __str__(self, level):
        return '.' * level + '- ' + self.name + ' ' + str(self.size) + ' \n'
