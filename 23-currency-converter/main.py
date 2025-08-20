import json
from typing import Final

import requests

BASE_URL: Final[str] = "http://api.exchangeratesapi.io/v1/latest"
API_KEY: Final[str] = "1acf200940ca3a433448b5d5087565ca"


def get_rates(mock: bool = False) -> dict:
    if mock:
        with open("rates.json", "r") as file:
            return json.load(file)

    payload: dict = {"access_key": API_KEY}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()
    return data


def get_currency(currency: str, rates: dict) -> float:
    moeda: str = currency.upper()

    if moeda in rates.keys():
        return rates.get(moeda)
    else:
        raise ValueError(f"{currency} não é uma moeda válida!")


def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)

    conversion: float = round((vs_rate / base_rate) * amount, 2)

    print(f"{amount:,.2f} ({base}) é: {conversion:,.2f} ({vs})")
    return conversion


def main():
    data: dict = get_rates(mock=True)
    rates: dict = data.get("rates")

    convert_currency(100, "EUR", "BRL", rates=rates)


if __name__ == "__main__":
    main()
