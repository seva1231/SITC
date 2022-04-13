import telebot
bot = telebot.TeleBot("2054714414:AAHCgXWFcCp44dMaM9e4jlMVBkGKwANj_DU")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, Пользователь. Это официальный бот корпорации SITC. Опишите свой вопрос.")


@bot.message_handler(commands=['dispetcher'])
def send_welcome(message):
    bot.reply_to(message, "Контактный центр Телефон:+380957683983, +380967683983, +38075098536")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Ты можешь оставить вопрос, который я передам диспетчеру.")

@bot.message_handler(commands=['sait'])
def send_welcome(message):
    bot.reply_to(message, "")




bot.polling()
