import datetime


class Document:
    __id_all = 0

    def __init__(self, name: str, code: str, document_format: str):
        self.name = name
        self.__code = code
        self.__document_format = document_format
        Document.__id_all = Document.__id_all + 1
        self.__id = Document.__id_all
        self.__date_creation = datetime.datetime
        self.__date_last_change = datetime.datetime

    @property
    def data_creation(self):
        return self.__date_creation

    @property
    def data_last_change(self):
        return self.__date_last_change

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def code(self):
        return self.__code

    @property
    def document_format(self):
        return self.__document_format


class DocumentsManager:
    __documents = dict()
    __id = 0

    def __init__(self):
        pass

    # добавление документа
    @staticmethod
    def add_document(chat_id: int, document: Document):
        if type(document) != Document:
            raise "Некорректный формат документа на входе!"

        if chat_id not in DocumentsManager.__documents:
            DocumentsManager.__documents[chat_id] = dict()

        DocumentsManager.__id = DocumentsManager.__id + 1
        id_doc = DocumentsManager.__id
        DocumentsManager.__documents[chat_id][id_doc] = document

    @staticmethod
    def get_document(chat_id, id_doc) -> Document:
        if chat_id not in DocumentsManager.__documents:
            return None

        if id_doc not in DocumentsManager.__documents[chat_id]:
            return None

        return DocumentsManager.__documents[chat_id][id_doc]

    @staticmethod
    def delete_document(chat_id: int, id_doc: int) -> (bool, str):
        if chat_id not in DocumentsManager.__documents:
            return False, 'У пользователя нет документов в базе'

        if id_doc not in DocumentsManager.__documents[chat_id]:
            return False, f'Не было найдено документов по id={id_doc}'

        del DocumentsManager.__documents[chat_id][id_doc]
        return True, f'Документ с id={id_doc} был удален'

    @staticmethod
    def get_all_documents(chat_id) -> dict:
        if chat_id in DocumentsManager.__documents:
            return DocumentsManager.__documents[chat_id]
        else:
            return dict()





