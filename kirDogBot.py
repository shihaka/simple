import telebot
bot = telebot.TeleBot('1585933379:AAF1cYbB3hCbdIs5v0WeIz6UoNgiXJJkuPc')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я - бот. Приятно познакомится, {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')


bot.polling(none_stop=True)
