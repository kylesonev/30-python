"""
Programa para extração automática de endereços de e-mail de páginas web.
"""

import re
from typing import Final

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


EMAIL_REGEX: Final[
    str
] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""


class Browser:
    """
    Classe que gerencia o navegador Selenium para extração de e-mails.

    Atributos|:
        chrome_options (Options): Opções de configuração do navegador Chrome
        service (Service): Serviço do ChromeDriver responsável por inicializar o navegador
        browser (webdriver.Chrome): Instância do navegador Chrome controlada pelo Selenium
    """

    def __init__(self, driver: str) -> None:
        """Inicializa o navegador Chrome em modo headless.

        Args:
            driver (str): Caminho para o executável do ChromeDriver
        """
        print("Iniciando browser.")
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-gpu")

        self.service = Service(driver)
        self.browser = webdriver.Chrome(
            service=self.service, options=self.chrome_options
        )

    def scrape_emails(self, url: str) -> set:
        """
        Extrai endereços de e-mail válidos de uma página web.

        Abre a URL fornecida, obtém o conteúdo HTML e utiliza uma expressão regular
        para encontrar todos os endereços de e-mail válidos.

        Args:
            url (str): endereço da página a ser varrida

        Returns:
            set: Um conjunto de endereços de e-mail únicos encontrados na página
        """
        print(f"Vasculhando: {url} por emails")
        self.browser.get(url)
        page_source: str = self.browser.page_source

        list_of_emails: set = set()
        for re_match in re.finditer(EMAIL_REGEX, page_source):
            list_of_emails.add(re_match.group())

        return list_of_emails

    def close_browser(self) -> None:
        """
        Fecha o navegador controlado pelo Selenium
        """
        print("Fechando o navegador...")
        self.browser.close()


def main():
    """
    Função principal que executa o processo de scraping de e-mails.

    Inicializa o navegador, acessa uma página de exemplo com e-mails gerados aleatoriamente,
    extrai os endereços e exibe os resultados no terminal
    """
    driver: str = "../19-email-scrapper/chromedriver"
    browser = Browser(driver=driver)

    emails: set = browser.scrape_emails(
        "https://www.randomlists.com/email-addresses?qty=50"
    )

    for i, email in enumerate(emails, start=1):
        print(i, email, sep=": ")

    browser.close_browser()


if __name__ == "__main__":
    main()
