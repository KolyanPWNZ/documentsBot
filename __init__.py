import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.telegram_token)

CONTENT_TYPES = ["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                 "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                 "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                 "migrate_from_chat_id", "pinned_message"]

@bot.message_handler(commands=['start'])
def start(message):
    welcome_message = 'Привет! Это бот-помошник по хранению ваших документов и фотографий.'
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_item_mydocuments = types.KeyboardButton('Посмотреть загруженные документы')
    menu_item_get = types.KeyboardButton('Получить документ', )
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
    if message.text == 'Посмотреть загруженные документы':
        bot.send_message(message.chat.id, 'Привет')


bot.polling(none_stop=True)