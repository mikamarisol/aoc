class Directory:

    def __init__(self, name):
        self.name = name
        self.parent = None
        self.files = []
        self.directories = []
        self.size = 0

    def __str__(self, level=0):
        ret = '.' * level + '- ' + self.name + ' ' + str(self.size) + ' \n'
        for child in self.directories + self.files:
            ret += child.__str__(level + 1)
        return ret

    def get_directories(self):
        return [directory.name for directory in self.directories]

    def get_files(self):
        return [file.name for file in self.files]

    def get_directory(self, name):
        return next(filter(lambda directory: directory.name == name, self.directories))

    def get_file(self, name):
        return next(filter(lambda file: file.name == name, self.files))

    def has_directory(self, directory):
        return directory in self.get_directories()

    def has_file(self, directory):
        return directory in self.get_files()

    def create_directory(self, directory):
        self.directories.append(directory)
        directory.parent = self

    def create_file(self, file):
        self.files.append(file)
        file.parent = self

    def update_size(self):
        self.size = sum([child.size for child in self.files + self.directories])

    def get_descendants(self):
        yield self
        for descendant in self.directories:
            yield from descendant.get_descendants()

