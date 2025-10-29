from dataclasses import dataclass
from typing import Final
import requests

BASE_URL: Final[str] = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"


@dataclass
class Coin:
    """
    Representa uma criptomoeda obtida a partir da API da CoinGecko.

    Attributes:
        name (str): nome completo da moeda
        symbol (str): símbolo da moeda
        current_price (float): preço atual em USD
        high_24h (float): maior preço nas últimas 24h
        low_24h (float): menor preço nas últimas 24h
        price_change_24h (float): variação absoluta de preço nas últimas 24h
        price_change_percentage_24h (float): variação percentual nas últimas 24h
    """

    name: str
    symbol: str
    current_price: float
    high_24h: float
    low_24h: float
    price_change_24h: float
    price_change_percentage_24h: float

    def __str__(self):
        """
        Retorna uma representação formatada da moeda

        Returns:
            str: Exemplo -> 'Bitcoin (btc):  U$65,432.5'
        """
        return f"{self.name} ({self.symbol}):  U${self.current_price:,}"


def get_coins() -> list[Coin]:
    """
    Obtém dados de criptomoedas da API pública da CoinGecko.

    Faz uma requisição HTTP para obter informações de mercado em USD
    das principais criptomoedas (ordenadas por capitalização de mercado)
    e retorna uma lista de objetos 'Coin'.

    Returns:
        list[Coin]: Lista contendo os dados das criptomoedas.

    Raises:
        requests.exceptions.RequestException: Caso a conexão com a API falhe.
    """
    payload: dict = {"vs_currency": "usd", "order": "market_cap_desc"}
    data = requests.get(BASE_URL, params=payload)
    json: dict = data.json()

    coin_list: list[Coin] = []
    for item in json:
        current_coin: Coin = Coin(
            name=item.get("name"),
            symbol=item.get("symbol"),
            current_price=item.get("current_price"),
            high_24h=item.get("high_24h"),
            low_24h=item.get("low_24h"),
            price_change_24h=item.get("price_change_24h"),
            price_change_percentage_24h=item.get("price_change_percentage_24h"),
        )
        coin_list.append(current_coin)

    return coin_list


if __name__ == "__main__":
    """
    Imprime a lista de moedas com seus preços atuais.

    Executado diretamente, este módulo realiza a requisição de dados via 'get_coins()'
    e imprime no console cada moeda com seu preço atual formatado.
    """
    coins = get_coins()
    for coin in coins:
        print(coin)
