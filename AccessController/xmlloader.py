import os
from xml.etree import ElementTree

from bs4 import BeautifulSoup

from AccessController.fileinterface import FileInterface


class XMLLoader(FileInterface):
    def load(self) -> bool:
        print("[" + self.__class__.__name__ + "]" + " loading file.")

        try:
            with open(os.path.join(self.file_path, self.file_name), "r", encoding="utf-8") as loaded_file:
                print("[" + self.__class__.__name__ + "] " + self.file_name + " loaded into memory.")
                self.data = ElementTree.parse(loaded_file)
                return True
        except Exception as e:
            print("[" + self.__class__.__name__ + "]" + "Exception fault: " + str(e))
            return False

    # Recursive function (do not call this method)
    def _get_prettified(self, tag, curr_indent, indent):
        out = ''
        for x in tag.find_all(recursive=False):
            if len(x.find_all()) == 0:
                if x.string is not None:
                    content = x.string.strip(' \n')
                else:
                    content = ''
            else:
                content = '\n' + self._get_prettified(x, curr_indent + ' ' * indent, indent) + curr_indent

            attrs = ' '.join([f'{k}="{v}"' for k, v in x.attrs.items()])
            out += curr_indent + (
                '<%s %s>' % (x.name, attrs) if len(attrs) > 0 else '<%s>' % x.name) + content + '</%s>\n' % x.name

        return out

    # Call this method
    def get_prettified(self, tag, indent):
        return self._get_prettified(tag, '', indent);

    def save(self) -> bool:
        try:
            # init file mode is write
            file_mode: str = 'w'
            if self.file_overwrite:
                print("[" + self.__class__.__name__ + "] " + self.file_name + " removing file.")
                # if overwriting set file mode to x for creation
                file_mode = 'x'
                os.remove(os.path.join(self.file_path, self.file_name))

            soup = BeautifulSoup(ElementTree.tostring(self.data.getroot(), encoding='utf8', method='xml'), 'xml')
            output = self.get_prettified(soup, indent=4)
            with open(os.path.join(self.file_path, self.file_name), file_mode, encoding="utf-8") as loaded_file:
                loaded_file.write(output)
                return True

        except Exception as e:
            print("[" + self.__class__.__name__ + "]" + "Exception fault: " + str(e))
            return False
