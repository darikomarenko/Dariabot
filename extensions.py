import requests

from config import currency_keys


class ConvertionException(Exception):
    pass


class CurrencyConverter():
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        quote = quote.lower()
        base = base.lower()

        if quote == base:
            raise ConvertionException(f"Не могу перевести одинаковую валюту {quote}. Введите разные валюты")
        try:
            quote_ticker = currency_keys[quote]
            base_ticker = currency_keys[base]
        except KeyError:
            raise ConvertionException(
                f"Не могу обработать такую валюту. Проверить список доступных валют - введите команду /values")
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не удалось обработать {amount}, введите цифру")

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}"
        headers = {"apikey": "dokJIFNf4oOKtyT9KnWcbFEOC5330VAU"}
        response = requests.get(url, headers=headers)
        return response.json()['result']
