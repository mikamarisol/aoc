from file import File


class Directory:

    def __init__(self, name):
        self.name = name
        self.parent = None
        self.files = []
        self.directories = []
        self.size = 0

    def __str__(self):
        return self.name

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
        self.size += directory.size

    def create_file(self, file):
        self.files.append(file)
        file.parent = self
        self.size += file.size

if __name__ == '__main__':
    root = Directory('/')
    root.create_directory(Directory('abc'))
    root.create_file(File('file', 2))
    root.create_file(File('another', 67))
    print(root.has_directory('abc'))
    print(root.get_directories())
    print(root.has_file('file'))
    print(root.get_files())

    node = Directory('node')
    root.create_directory(node)
    print(node.parent)
    print(root.get_directories())

    print(root.get_directory('abc').parent)
    print(root.get_file('file').size)
    print(root.size)