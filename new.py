import telebot
from telebot import types
import config
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def hi(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a1 = types.KeyboardButton ("Начать")
    markup.add(a1)

    bot.send_message(message.chat.id, "Приветсвую тебя! Я Телеграм бот Тимура, который запускаеться в его сервере!",parse_mode='html', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def blablabla(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, "Давай поиграем!")
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Давай", callback_data='start')
        button2 = types.InlineKeyboardButton("Неа", callback_data='stop')
        markup.add(button1, button2)
            


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    try:
        if call.data == "start":
            markup = types.InlineKeyboardMarkup(row_width=2)
            bot.send_message(call.message.chat.id, "Ok, выбери число")
            button1 = types.InlineKeyboardButton("1", callback_data='1')
            button2 = types.InlineKeyboardButton("2", callback_data='2')
            markup.add(button1, button2)
        else:
            bot.send_message(call.message.chat.id, "Ok")

    except Exception as e:
        print(e)
bot.polling(none_stop=True)