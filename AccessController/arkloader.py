import os

from AccessController.fileloader import FileLoader


class ArkLoader(FileLoader):
    def __enter__(self):
        # Check for directory and file if not return false
        if not os.path.exists(self.file_path) and not os.path.exists(os.path.join(self.file_path, self.file_name)):
            raise Exception("[" + self.__class__.__name__ + "] " + self.file_path + " path does not exist.")
        self.load(self.load_callback)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save(self.save_callback)

    def load_callback(self, data: []):
        return data.read().splitlines()

    def save_callback(self, data: []):
        return '\n'.join(data)

    def add(self, element):
        if not self.exists(element):
            self.data.append(element)
            return element
        return None

    def remove(self, element) -> bool:
        if self.exists(element):
            self.data.pop(self.data.index(element))
            return True
        return False

    def find_one(self, element):
        if self.exists(element):
            return element
        return None

    def find_all(self) -> []:
        return self.data

    def exists(self, element: str) -> bool:
        if element in self.data:
            return True
        return False

    def clear(self) -> bool:
        self.data.clear()

        if len(self.data) == 0:
            return True
        return False
