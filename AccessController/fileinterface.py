import os
from abc import abstractmethod, ABC


class FileInterface(ABC):

    def __init__(self, path: str, file_name: str, overwrite: bool = False):
        if self.__class__.__name__ == "FileInterface":
            raise Exception("[" + self.__class__.__name__ + "]" + " cannot initializing base class.")
        print("[" + self.__class__.__name__ + "]" + " initializing.")
        self.data = None
        self.file_path = path
        self.file_name = file_name
        self.file_overwrite = overwrite

    def __enter__(self):
        # Check for directory and file if not return false
        if not os.path.exists(self.file_path) and not os.path.exists(os.path.join(self.file_path, self.file_name)):
            raise Exception("[" + self.__class__.__name__ + "] " + self.file_path + " path does not exist.")
        # if not os.path.exists(self.file_path):
        #     raise Exception("[" + self.__class__.__name__ + "] " + self.file_path + " path does not exist.")
        #
        # if not os.path.exists(os.path.join(self.file_path, self.file_name)) and not self.file_overwrite:
        #     raise Exception("[" + self.__class__.__name__ + "] " + self.file_name + " file does not exist.")

        self.load()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save()

    @abstractmethod
    def load(self) -> bool:
        pass

    @abstractmethod
    def save(self) -> bool:
        pass

    @abstractmethod
    def add(self, element):
        pass

    @abstractmethod
    def remove(self, element) -> bool:
        pass

    @abstractmethod
    def find_one(self, element):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def exists(self, element) -> bool:
        pass

    @abstractmethod
    def clear(self) -> bool:
        pass
