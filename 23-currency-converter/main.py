import json
from typing import Final

import requests

BASE_URL: Final[str] = "http://api.exchangeratesapi.io/v1/latest"
API_KEY: Final[str] = "1acf200940ca3a433448b5d5087565ca"


def get_rates(mock: bool = False) -> dict:
    """
    Obtém as taxas de câmbio mais recentes da API ExchangeRates ou de um arquivo local mockado.

    Args:
        mock (bool): Se True, lê os dados do arquivo local 'rates.json' em vez de fazer a requisição à API.
                     Útil para testes sem depender de conexão com a internet.
                     Padrão: False.

    Returns:
        dict: Dicionário contendo as taxas de câmbio. Estrutura esperada:
              {
                  "success": bool,
                  "timestamp": int,
                  "base": str,
                  "date": str,
                  "rates": { "USD": float, "BRL": float, ... }
              }
    """
    if mock:
        with open("rates.json", "r") as file:
            return json.load(file)

    payload: dict = {"access_key": API_KEY}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()
    return data


def get_currency(currency: str, rates: dict) -> float:
    """
    Retorna a taxa de câmbio de uma moeda específica.

    Args:
        currency (str): Código da moeda desejada (ex: 'USD', 'BRL', 'EUR').
        rates (dict): Dicionário de taxas de câmbio retornado pela função 'get_rates()'.

    Returns:
        float: Valor da taxa de câmbio da moeda informada.

    Raises:
        ValueError: Se a moeda informada não for encontrada no dicionário de taxas.
    """
    moeda: str = currency.upper()

    if moeda in rates.keys():
        return rates.get(moeda)
    else:
        raise ValueError(f"{currency} não é uma moeda válida!")


def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
    """
    Converte um valor de uma moeda base para outra moeda de destino, usando as taxas de câmbio informadas.

    Args:
        amount (float): Quantia a ser convertida.
        base (str): Código da moeda base (ex: 'EUR').
        vs (str): Código da moeda de destino (ex: 'BRL').
        rates (dict): Dicionário contendo as taxas de câmbio.

    Returns:
        float: Valor convertido, arredondado para duas casas decimais.
    """
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)

    conversion: float = round((vs_rate / base_rate) * amount, 2)

    print(f"{amount:,.2f} ({base}) é: {conversion:,.2f} ({vs})")
    return conversion


def main():
    """
    Função principal do script.

    Obtém as taxas de câmbio (usando o modo mock), extrai o dicionário de taxas e
    realiza um exemplo de conversão de moeda de EUR para BRL.
    """
    data: dict = get_rates(mock=True)
    rates: dict = data.get("rates")

    convert_currency(100, "EUR", "BRL", rates=rates)


if __name__ == "__main__":
    main()
