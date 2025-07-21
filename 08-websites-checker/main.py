import requests
from fake_useragent import UserAgent
from http import HTTPStatus


def get_websites(csv_path: str) -> list[str]:

    websites: list[str] = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for linha in reader:
            if "https://" not in linha[1] or 'http://' in linha[1]:
                websites.append(f'https://{linha[1]}')
            else:
                websites.append(linha[1])

        return websites


def get_user_agent() -> str:
    ua = UserAgent()
    return ua.firefox


def get_status_description(status_code: int) -> str:
    for value in HTTPStatus:
        if value == status_code:
            description: str = f'({value} {value.name}) {value.description}'
            return description

    return '(???) Código de status desconhecido'


def check_website(website: str, user_agent):
    try:
        code: int = requests.get(
            website, headers={'User-Agente': user_agent}).status_code
        print(website, get_status_description(code))
    except Exception:
        print(f"Não foi possível obter informações para o site: {website}")


def main():
    sites: list[str] = get_websites('08-websites-checker/websites.csv')
    user_agent = get_user_agent()

    for site in sites:
        check_website(site, user_agent)


if __name__ == '__main__':
    main()
