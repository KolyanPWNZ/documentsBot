import config
import telebot
from telebot import types
from documents import DocumentsManager, Document

bot = telebot.TeleBot(config.telegram_token)

CONTENT_TYPES = ["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                 "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                 "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                 "migrate_from_chat_id", "pinned_message"]

doc_mng = DocumentsManager()

@bot.message_handler(commands=['start'])
def start(message):
    welcome_message = 'Привет! Это бот-помошник по хранению ваших документов и фотографий.'
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_item_mydocuments = types.KeyboardButton('Посмотреть список загруженных документов')
    menu_item_get = types.KeyboardButton('Получить документ')
    menu_item_add = types.KeyboardButton('Добавить новый документ')
    menu_item_delete = types.KeyboardButton('Удалить документ из бота')
    menu.add(menu_item_mydocuments)
    menu.add(menu_item_get)
    menu.add(menu_item_add)
    menu.add(menu_item_delete)
    bot.send_message(message.chat.id, welcome_message, reply_markup=menu)

@bot.message_handler(commands=['help'])
def help(message):
    info = 'Данный бот не хранит у себя ваши документы, а лишь достает по вашему запросу ' \
           'нужные вам документы, которые хранятся на сервере телеграмм'
    bot.send_message(message.chat.id, message)

@bot.message_handler(content_types=['text'])
def input_handler(message):
    if message.text == 'Посмотреть список загруженных документов':
        docs = doc_mng.get_all_documents(message.chat.id)
        print_docs(message.chat.id, docs)


    elif message.text == 'Получить документ':
        send = bot.send_message(message.chat.id, 'Пришлите id документа, который хотите получить.'
                                                 'Узнать id документа можно, запросить у меня список всех документов'
                                                 'в другом пункте меню.')
        bot.register_next_step_handler(send, add_document_to_server)

    elif message.text == 'Добавить новый документ':
        send = bot.send_message(message.chat.id, 'Пришлите мне ваш документ')
        bot.register_next_step_handler(send, add_document_to_server)

    elif message.text == 'Удалить документ из бота':
        bot.send_message(message.chat.id, 'Привет')

    else:
        bot.send_message(message.chat.id, 'Не понимаю :(')


def print_docs(chat_id: int, docs: dict):
    if len(docs) == 0:
        bot.send_message(chat_id, 'Документы не найдены')
        return

    doc_info = 'Ваши документы:'
    for id in docs:
        doc_info = doc_info + '\n' + f'\t{id}: {docs[id].name}'
    bot.send_message(chat_id, doc_info)


d

# функция обработчик: добавление нового документа
def add_document_to_server(message):
    if message.content_type != 'document':
        bot.send_message(message.chat.id, 'Но это не документ...')
        return

    file_code   = message.document.file_id
    file_name   = message.document.file_name
    file_format = message.document.mime_type.split('/')[1]
    doc = Document(file_name, file_code, file_format)
    doc_mng.add_document(message.chat.id, doc)
    bot.send_message(message.chat.id, f'Документ {file_name} добавлен')



bot.polling(none_stop=True)