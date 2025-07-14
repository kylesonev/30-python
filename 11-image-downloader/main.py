import os

import requests


def get_extension(image_url: str) -> str | None:
    extensions: list[str] = [".png", ".jpeg", ".jpg", ".gif", ".svg"]
    for ext in extensions:
        if ext in image_url:
            return ext


def download_image(image_url: str, name: str, folder: str = None):
    if ext := get_extension(image_url):
        if folder:
            image_name: str = f"{folder}/{name}{ext}"
        else:
            image_name: str = f"{name}{ext}"

    else:
        raise Exception("A extenção da imagem não foi localizada!")

    # Verifica se o nome já existe
    if os.path.isfile(image_name):
        raise Exception("O nome do arquivo já existe...")

    # Baixa a imagem
    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, "wb") as handler:
            handler.write(image_content)
            print(f"Baixado com sucesso: {image_name}")

    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    input_url: str = input("Insira a url da imagem: ")
    input_name: str = input("Digite um nome para o arquivo a ser salvo: ")

    print("Baixando...")
    download_image(image_url=input_url, name=input_name, folder="images")

