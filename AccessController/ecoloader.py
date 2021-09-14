from typing import Optional, Union

from AccessController.jsonloader import JSONLoader


class EcoLoader(JSONLoader):
    def add(self, element: Union[str, list]) -> bool:
        if not self.exists(element):
            if type(element) is str:
                self.data['UserPermission']['WhiteList']['Collection']['System.String']['$values'].append(element)
            else:
                for i in element:
                    if i not in self.data['UserPermission']['WhiteList']['Collection']['System.String']['$values']:
                        self.data['UserPermission']['WhiteList']['Collection']['System.String']['$values'].append(i)
            return True
        return False

    def remove(self, element: Union[str, list]) -> bool:
        if self.exists(element) or type(element) is list:
            if type(element) is str:
                self.data['UserPermission']['WhiteList']['Collection']['System.String']['$values'].remove(element)
            else:
                final_list = list(set(self.data['UserPermission']['WhiteList']['Collection']['System.String']['$values']
                                      ) - set(element))
                self.clear()
                self.data['UserPermission']['WhiteList']['Collection']['System.String']['$values'].extend(final_list)
            return True
        return False

    def clear(self) -> bool:
        self.data['UserPermission']['WhiteList']['Collection']['System.String']['$values'].clear()

        if len(self.data['UserPermission']['WhiteList']['Collection']['System.String']['$values']) == 0:
            return True
        return False

    def find_one(self, element) -> Optional[str]:
        if element in self.data['UserPermission']['WhiteList']['Collection']['System.String']['$values']:
            return element
        else:
            return None

    def find_all(self) -> []:
        return self.data['UserPermission']['WhiteList']['Collection']['System.String']['$values']

    def exists(self, element) -> bool:
        return element in self.data['UserPermission']['WhiteList']['Collection']['System.String']['$values']
