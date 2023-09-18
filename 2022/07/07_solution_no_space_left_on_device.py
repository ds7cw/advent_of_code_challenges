# The outermost directory is called /

# lines that begin with $ are commands you executed

# cd means change directory

# cd x moves in one level: it looks in the current dir for the dir named x and makes it the current dir

# cd .. moves out one level: it finds the dir that contains the current dir, then makes that directory the current dir

# cd / switches the current directory to the outermost directory, /

# ls means list. It prints out all of the files and dirs immediately contained by the current dir

# 123 abc means that the current dir contains a file named abc with size 123

# dir xyz means that the current dir contains a dir named xyz

#
from abc import ABC, abstractmethod
from typing import List


class FileDirTemplate(ABC):
    def __init__(self, name: str, path: list, parent: str="Root") -> None:
        self.name = name
        self.path = path
        self.parent = parent

    @abstractmethod
    def dir_size(self):
        pass


class Dir(FileDirTemplate):

    def __init__(self, name: str, path: list, parent: str="No Parent") -> None:
        super().__init__(name, path, parent)
        self.items: List[Dir, dict] = []


    def dir_size(self) -> int:
        size = 0
        for item in self.items:
            size += item.dir_size()

        return size

    def add_dir_or_file(self, item) -> None:
        self.items.append(item)


class File(FileDirTemplate):

    def __init__(self, name, path: list, parent, size) -> None:
        super().__init__(name, path, parent)
        self.size = size


    def dir_size(self) -> int:
        return self.size


class FileManager:

    def __init__(self) -> None:
        self.items = []
        self.dir_file_sizes = {}
        self.le_one_hundred = {}

    def directory_size(self, path: list) -> int:
        # assume dir_name is a valid entry
        item = [el for el in self.items if el.path == path][0]

        if self.dir_file_sizes.get(item):
            return self.dir_file_sizes[item]


        dir_size = item.dir_size()
        self.dir_file_sizes[item] = dir_size
        if dir_size <= 100_000:
            self.le_one_hundred[item] = dir_size
        return dir_size

    def create_new_dir(self, name: str, path: list, parent: str="No Parent"):
        new_dir = Dir(name, path, parent)
        self.items.append(new_dir)

        if parent != "No Parent":
            parent_obj = [el for el in self.items if el.name == parent and el.path == path[:-1]][0]
            parent_obj.add_dir_or_file(new_dir)

    def create_new_file(self, name, path: list, parent: str, size: int) -> None:
        new_file = File(name, path, parent, size)
        parent_dir = [el for el in self.items if el.name == parent and el.path == path][0]
        parent_dir.add_dir_or_file(new_file)


with open("07_input.txt", "r") as f:
    data = f.readlines()

i = 0

file_manager = FileManager()
current_dir = None
path = []

while i < len(data):
    row = data[i].strip()
    # print(i)


    if data[i].startswith("$ cd /"):
        dir_name = data[i].split()[-1]
        path.append(dir_name)
        copy_path = path[:]
        file_manager.create_new_dir(dir_name, copy_path)


    elif data[i].startswith("$ cd"):
        dir_name = data[i].split()[-1]
        if dir_name == "..":
            path.pop()

        else:
            path.append(dir_name)

    elif data[i].startswith("$ ls"):
        i += 1

        while i < len(data):
            if data[i].startswith("$"):
                break

            if data[i].startswith("dir"):
                dir_name = data[i].split()[-1]
                copy_path = path[:] + [dir_name]
                file_manager.create_new_dir(dir_name, copy_path, copy_path[-2])

            else:
                file_size, file_name = data[i].split()
                copy_path = path[:]
                file_manager.create_new_file(file_name, copy_path, copy_path[-1], int(file_size))
            # print(path)
            i += 1

        continue

    i += 1

part_one_answer = 0

for obj in file_manager.items:
    result = obj.dir_size()
    if result <= 100_000:
        part_one_answer += result

print(f"Part 1 Answer: {part_one_answer}")
