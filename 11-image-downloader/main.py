"""
Baixador de imagens
"""

import os

import requests


def pegar_extensao(image_url: str) -> str | None:
    """
    Pega a extensão da imagem no link passado.
    Args:
        image_url(str): url da imagem que será baixada

    """
    extensions: list[str] = [".png", ".jpeg", ".jpg", ".gif", ".svg"]
    for ext in extensions:
        if ext in image_url:
            return ext


def download_imagem(imagem_url: str, nome: str, folder=None):
    """
    Realiza o download da imagem
    Args:
        image_url(str): url da imagem que será baixada
        nome: nome do arquivo que será salva a imagem
        folder: nome da pasta para baixar a imagem
    """

    if ext := pegar_extensao(imagem_url):
        if folder:
            image_name: str = f"{folder}/{nome}{ext}"
        else:
            image_name: str = f"{nome}{ext}"

    else:
        raise Exception("A extenção da imagem não foi localizada!")

    # Verifica se o nome já existe
    if os.path.isfile(image_name):
        raise Exception("O nome do arquivo já existe...")

    # Baixa a imagem
    try:
        image_content: bytes = requests.get(imagem_url).content
        with open(image_name, "wb") as handler:
            handler.write(image_content)
            print(f"Baixado com sucesso: {image_name}")

    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    """
    Executa a lógica do programa
    1. Solicita ao usuário a url da imagem a ser baixada.
    2. Solicita ao usuário o nome do arquivo para salvar a imagem
    3. Realiza o donwload da imagem
    """
    input_url: str = input("Insira a url da imagem: ")
    input_name: str = input("Digite um nome para o arquivo a ser salvo: ")

    print("Baixando...")
    download_imagem(imagem_url=input_url, nome=input_name, folder="images")
