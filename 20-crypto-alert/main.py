import time

from crypto_data import Coin, get_coins


def alert(symbol: str, bottom: float, top: float, coin_list: list[Coin]):
    for coin in coin_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, "!!!!!!!!!!!!!!!!!!!")
            else:
                print(coin)


if __name__ == "__main__":
    while True:
        time.sleep(5)
        coins: list[Coin] = get_coins()

        alert("btc", bottom=100_000, top=120_000, coin_list=coins)
