import telebot

from config import currency_keys, TOKEN
from extensions import ConvertionException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу, введите команду боту в следующем формате: \n<имя валюты> \
<в какую валюту перевести> <количество переводимой валюты>\n Увидеть список всех доступных валют: /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    for key in currency_keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values = message.text.split()

    if len(values) != 3:
        raise ConvertionException("Введите 3 параметра, например: доллар рубль 10")

    quote, base, amount = values
    try:
        total_base = CurrencyConverter.convert(quote, base, amount)
        text = f'Цена {amount} {quote} в {base} - {total_base}'
    except ConvertionException as e:
        text = e

    bot.reply_to(message, text)


bot.polling(none_stop=True)
