import json
import requests
from config import keys


class ConvertionException(Exception):
    pass


class Convertor:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {quote}.")
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {base}.")
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}!')

        r = requests.get(f"https://v6.exchangerate-api.com/v6/ea0df45e544ee148736eeec3/pair/{quote_ticker}/{base_ticker}")
        total_base = json.loads(r.content)[keys[base]]

        return total_base