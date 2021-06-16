import telebot
from telebot import types
import config
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def hi(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a1 = types.KeyboardButton ("Начать")
    markup.add(a1)

    bot.send_message(message.chat.id, "Приветсвую тебя! Загадай число от 1 до 1000, и я угадаю его за 12 вопросов",parse_mode='html', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def blablabla(message):
    if message.chat.type == 'private':
        markup = types.InlineKeyboardMarkup(row_width=2)
        for i in range(1, 4):
            button1 = types.InlineKeyboardButton("Больше", callback_data='>')
            button2 = types.InlineKeyboardButton("Меньше", callback_data='<')
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Загаданное число больше или меньше ", "500", "?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    try:
        if call.data == ">":
            bot.send_message(call.message.chat.id, "Ok")
    except Exception as e:
        print(e)
bot.polling(none_stop=True)