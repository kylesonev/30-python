"""
Encurtador de links
"""

from typing import Final

import requests

API_KEY: Final[str] = "77700914aa4c7c85cd43d803f232553170a83"
BASE_URL: Final[str] = "https://cutt.ly/api/api.php"


def encurtar_link(link_completo: str):
    """
    Recebe um link do usuário e encurta utilizando a API
    Args:
        link_completo(str): link completo a ser encurtado
    """
    payload: dict = {"key": API_KEY, "short": link_completo}
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    if url_data := data.get("url"):
        if url_data["status"] == 7:
            short_link: str = url_data["shortLink"]
            print("Link: ", short_link)
        else:
            print("Erro: ", url_data["status"])


def main():
    """
    Executa a lógica do programa
    1. Solicita ao usuário o link a ser encurtado
    2. Imprime na tela o link encurtado ou erro
    """
    input_link: str = input("Digite o link que será encurtado: ")
    encurtar_link(input_link)


if __name__ == "__main__":
    main()
