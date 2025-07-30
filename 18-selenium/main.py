import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Browser:
    def __init__(self, driver: str):
        print("Iniciando...")
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        print(f"Abrindo: {url}")
        self.browser.get(url)

    def close_browser(self):
        print("Fechando o navegador...")
        self.browser.quit()


if __name__ == "__main__":
    browser = Browser("../18-selenium/chromedriver")

    browser.open_page("https://www.python.org")
    time.sleep(5)

    browser.close_browser()
