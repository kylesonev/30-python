import requests
from bs4 import BeautifulSoup


def get_soup() -> BeautifulSoup:
    headers: dict = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0"
    }
    request = requests.get("https://www.cnnbrasil.com.br/", headers=headers)
    html: bytes = request.content

    soup = BeautifulSoup(html, "html.parser")
    return soup


def get_headlines(soup: BeautifulSoup) -> list[str]:
    headlines: set = set()

    for h in soup.findAll(
        "h2",
        class_="font-bold flex w-fit text-lg",
    ):
        headline: str = h.contents[0].lower()
        headlines.add(headline)

    return sorted(headlines)


def check_headlines(headlines: list[str], term: str):
    term_list: list[str] = []
    terms_found: int = 0

    for i, headline in enumerate(headlines, start=1):
        if term.lower() in headline:
            terms_found += 1
            term_list.append(headline)
            print(f'{i}: {headline.capitalize()} <------------------ "{term}"')
        else:
            print(f"{i}: {headline.capitalize()}")

    # Show the new list that contains the headlines if a term was found in them
    print("----------------------------------")
    if terms_found:
        print(f'"{term}" foi mencionado {terms_found} vezes.')
        print("----------------------------------")

        for i, headline in enumerate(term_list, start=1):
            print(f"{i}: {headline.capitalize()}")
    else:
        print(f'Não foi encontrado: "{term}"')
        print("----------------------------------")


def main():
    soup: BeautifulSoup = get_soup()
    headlines: list[str] = get_headlines(soup=soup)

    user_input: str = input("Qual termo você gostaria de procurar? >> ")
    check_headlines(headlines, user_input)


if __name__ == "__main__":
    main()
