import time
from crypto_data import Coin, get_coins


def alert(symbol: str, bottom: float, top: float, coin_list: list[Coin]):
    """
    Exibe alertas de preço para uma moeda específica

    Percorre a lista de moedas ('coin_list') e verifica se a moeda com o símbolo
    especificado ('symbol') está fora do intervalo de preços definido por 'bottom' e 'top'.

    Se o preço atual ('current_price') estiver abaixo de 'bottom' ou acima de 'top',
    um alerta visual será impresso no console.

    Args:
        symbol (str): Símbolo da moeda a ser monitorada (ex: "btc").
        bottom (float): Limite inferior de preço.
        top (float): Limite superior de preço.
        coin_list (list[Coin]): Lista de objetos Coin com dados de preço.
    """
    for coin in coin_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, "!!!!!!!!!!!!!!!!!!!")
            else:
                print(coin)


if __name__ == "__main__":
    """
    Loop principal do script de monitoramento

    Executa a cada 5 segundos:
        - Obtém a lista atualizada de moedas via 'get_coins()'
        - Chama a função 'alert()' para verificar se o preço do Bitcoin está dentro ou fora do intervalo definido
    """
    while True:
        time.sleep(5)
        coins: list[Coin] = get_coins()
        alert("btc", bottom=100_000, top=120_000, coin_list=coins)
