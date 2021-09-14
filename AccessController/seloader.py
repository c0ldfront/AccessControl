from typing import Optional
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

from AccessController.xmlloader import XMLLoader


class SELoader(XMLLoader):

    def __enter__(self):
        super().__enter__()
        self.root = self.data.getroot()
        self.whitelist = self.root.find("Whitelist")
        self.plugins = self.root.find("Plugins")
        return self

    def add(self, element: str):
        if not self.exists(element):
            self.whitelist.append(self.create_new_element('unsignedLong', element))
            return True
        return False

    def remove(self, element) -> bool:
        if self.exists(element):
            self.whitelist.remove(self.select_element(element))
            return True
        return False

    def find_one(self, element):
        if self.exists(element):
            return element
        return None

    def find_all(self):
        if len(self.whitelist) > 0:
            return self.whitelist.getchildren()
        return None

    def exists(self, element) -> bool:
        for child in self.whitelist:
            if child.text == element:
                return True
        return False

    def select_element(self, element) -> Optional[Element]:
        for child in self.whitelist:
            if child.text == element:
                return child
        return None

    def clear(self) -> bool:
        self.whitelist.clear()

        if len(self.whitelist) == 0:
            return True
        return False

    def create_new_element(self, tag: str, text: str) -> Element:
        element = ElementTree.Element(tag)
        element.text = text
        return element
