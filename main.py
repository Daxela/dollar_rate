import time
import telebot
import rate

bot = telebot.TeleBot('7728399159:AAHr_rHxl6xRuKJTtbHZywKpnyHXXhy135U')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, 'Добрый день. Как вас зовут?')
    else:
        currency = rate.Currency()
        dollar_rate = currency.get_currency_price()
        result = f"Рад знакомству, {message.text}! Курс доллара сегодня {str(dollar_rate)}р"
        bot.send_message(message.from_user.id, result)


print("Bot listening")
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)