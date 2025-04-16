import telebot

TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Қарақалпақ аўдарма ботқа қош келдиңиз!")

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    # Мұнда нағыз аўдарма функциясы қосылады
    bot.reply_to(message, f"Аударылып жатыр: {message.text}")

bot.infinity_polling()
