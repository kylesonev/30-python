"""
Verificador de status de Sites.
"""

import requests
from fake_useragent import UserAgent
from http import HTTPStatus
import csv


def receber_sites(csv_path: str) -> list[str]:
    """
    Recebe a lista dos sites.
    Args:
        csv_path(str): arquivo csv contendo a lista dos sites.
    Returns:
        list(str): lista com os endereços dos sites.
    """
    websites: list[str] = []
    with open(csv_path, "r") as file:
        reader = csv.reader(file)
        for linha in reader:
            if "https://" not in linha[1] or "http://" in linha[1]:
                websites.append(f"https://{linha[1]}")
            else:
                websites.append(linha[1])

        return websites


def receber_user_agent() -> str:
    """
    Receber o agente.
    """
    ua = UserAgent()
    return ua.firefox


def gerar_descricao_site(status_code: int) -> str:
    """
    Gerar a descrição do site.
    Args:
        status_code(int): código de status do site.
    Returns:
        str: descrição de status.
    """
    for value in HTTPStatus:
        if value == status_code:
            description: str = f"({value} {value.name}) {value.description}"
            return description

    return "(???) Código de status desconhecido"


def checar_site(website: str, user_agent):
    """
    Verifica o site.
    Args:
        website(str): site a ser verificado.
        user_agent: agente a ser utilizado.
    """
    try:
        code: int = requests.get(
            website, headers={"User-Agent": user_agent}
        ).status_code
        print(website, gerar_descricao_site(code))
    except Exception:
        print(f"Não foi possível obter informações para o site: {website}")


def main():
    """
    Executa a lógica do programa
    """
    sites: list[str] = receber_sites("~/30-python/08-websites-checker/websites.csv")
    user_agent = receber_user_agent()

    for site in sites:
        checar_site(site, user_agent)


if __name__ == "__main__":
    main()
