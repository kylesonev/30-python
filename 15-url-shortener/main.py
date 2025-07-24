from typing import Final

import requests

API_KEY: Final[str] = "77700914aa4c7c85cd43d803f232553170a83"
BASE_URL: Final[str] = "https://cutt.ly/api/api.php"


def shorten_link(full_link: str):
    payload: dict = {"key": API_KEY, "short": full_link}
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    if url_data := data.get("url"):
        if url_data["status"] == 7:
            short_link: str = url_data["shortLink"]
            print("Link: ", short_link)
        else:
            print("Erro: ", url_data["status"])


def main():
    input_link: str = input("Digite o link que será encurtado: ")
    shorten_link(input_link)


if __name__ == "__main__":
    main()
