import config
import bot_func
import telebot
from telebot import types

# инициализация бота и виженера
bot = telebot.TeleBot(config.TOKEN)

# тексты
help_message = 'Нажмите кнопку "Зашифровать/Расшифровать", чтобы получить зашифрованный/исходный текст при помощи ключа'
cr_or_encr_message = 'Чтобы получить зашфрованное сообщение напишите в следующей форме:\n Текст: опять работать Ключ: ' \
                     'альфа/nЧтобы расшифровать текст:\n Шифр:фыдапшдмифнмц Ключ: альфа '


def button(text):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(text)
    return murkup.add(btn)


@bot.message_handler(commands=['start'])
def born(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Зашифровать/Расшифровать")
    markup.add(item1)
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный шифровать и "
                     "расшифровывать сообщения. /help - расскажет как мной пользоваться".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['help'])
def helpme(message):
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(content_types=['text'])
def qwe(message):
    if message.chat.type == 'private':
        if message.text == 'Зашифровать/Расшифровать':
            bot.send_message(message.chat.id, cr_or_encr_message)
        elif message.text[:5].lower() == 'текст' or message.text[:5].lower() == 'шифр:':
            result_of_crypt = bot_func.crypt_decrypt(message.text)
            bot.send_message(message.chat.id, result_of_crypt)
        else:
            bot.send_message(message.chat.id, 'Альберт пидр')

def scenario():
    """
    Запускает сценарий шифратора/дешифратора.
    При нажатии на кнопку "Зашифровать/Расшифровать" бот предлагает действие через inline keyboard.
    После  выбора действия (нажатия inline button) бот предлагает написать текст (шифр), а затем
    написать ключ. После этого бот пишет шифр (расшифрованный текст)
    :return: текст или шифр (в зависимости от выбора)
    """
    @bot.message_handler(content_types=["text"])
    def default_test(message):
        keyboard = types.InlineKeyboardMarkup()
        tocrypt_button = types.InlineKeyboardButton(text="Зашифровать")
        fromcrypt_button = types.InlineKeyboardButton(text="Расшифровать")
        keyboard.add(tocrypt_button, fromcrypt_button)
        bot.send_message(message.chat.id, "Выберите действие.", reply_markup=keyboard)

if __name__ == "__main__":
    bot.polling(none_stop=True)
