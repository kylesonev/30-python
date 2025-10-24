"""
Programa simples utilizando selenium
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Browser:
    def __init__(self, driver: str) -> None:
        """
        Inicilização da classe browser
        driver(str): caminho para o driver do navegador
        """
        print("Iniciando...")
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def abrir_pagina(self, url: str) -> None:
        """
        Abre o navegador na página inserida
        Args:
            url(str): endereço da página que será aberta no navegador
        """
        print(f"Abrindo: {url}")
        self.browser.get(url)

    def fechar_browser(self) -> None:
        """
        Fechad o navegador
        """
        print("Fechando o navegador...")
        self.browser.quit()


if __name__ == "__main__":
    browser = Browser("../18-selenium/chromedriver")

    browser.abrir_pagina("https://www.python.org")
    time.sleep(5)

    browser.fechar_browser()
