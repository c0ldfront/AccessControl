import json
import os

from AccessController.fileinterface import FileInterface


class JSONLoader(FileInterface):
    def load(self) -> bool:
        print("[" + self.__class__.__name__ + "]" + " loading file.")

        try:
            with open(os.path.join(self.file_path, self.file_name), "r", encoding="utf-8") as loaded_file:
                print("[" + self.__class__.__name__ + "] " + self.file_name + " loaded into memory.")
                self.data = json.load(loaded_file)
                return True
        except Exception as e:
            print("[" + self.__class__.__name__ + "]" + "Exception fault: " + str(e))
            return False

    def save(self) -> bool:
        try:
            # init file mode is write
            file_mode: str = 'w'
            if self.file_overwrite:
                print("[" + self.__class__.__name__ + "] " + self.file_name + " removing file.")
                # if overwriting set file mode to x for creation
                file_mode = 'x'
                os.remove(os.path.join(self.file_path, self.file_name))

            with open(os.path.join(self.file_path, self.file_name), file_mode, encoding="utf-8") as loaded_file:
                json.dump(self.data, loaded_file)
                return True

        except Exception as e:
            print("[" + self.__class__.__name__ + "]" + "Exception fault: " + str(e))
            return False
