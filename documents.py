

class Document:

    __id_all = 0
    __documents = dir()

    def __init__(self, name: str, document_code: str, description: str):
        self.name = name
        self.description = description
        Document.__id_all = Document.__id_all + 1
        self.__id = Document.__id_all
        Document.__documents[self.__id] = {
            'name': name,
            'file': document_code,
            'description': description
        }

    @property
    def id(self):
        return self.__id

    @staticmethod
    def id_all() -> int:
        return Document.__id_all

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description
