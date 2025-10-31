from datetime import datetime
from random import choice, randint

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    """
    Retorna uma frase aleatória de boas-vindas e a data/hora atual.

    Returns:
        dict: Um dicionário contendo:
            - "phrase" (str): Uma frase aleatória.
            - "date" (datetime): O momento atual no servidor.

    """
    phrases: list[str] = ["Bem-vindo!", "Você está bacana!", "O tempo está ótimo!"]
    return {"phrase": choice(phrases), "date": datetime.now()}


@app.route("/api/random")
def random():
    """
    Gera um número aleatório baseado em um número fornecido via query string.

    Parâmetros de entrada (via URL):
        - number (int): Valor máximo para o número aleatório.
        - text (str, opcional): Texto customizado. Padrão é "default_text".

    Exemplo de uso:
        /api/random?number=10&text=teste

    Returns:
        dict: Um dicionário contendo:
            - "input" (int): O número fornecido pelo usuário.
            - "random" (int): Número aleatório entre 0 e o valor informado.
            - "text" (str): O texto enviado pelo usuário.
            - "date" (datetime): A data e hora atuais.

        Caso o parâmetro "number" não seja válido:
            {"Error": "Por favor, digite apenas números..."}
    """
    number_input = request.args.get("number", type=int)
    text_input = request.args.get("text", type=str, default="default_text")

    if isinstance(number_input, int):
        return {
            "input": number_input,
            "random": randint(0, number_input),
            "text": text_input,
            "date": datetime.now(),
        }
    else:
        return {"Error": "Por favor, digite apenas números..."}


if __name__ == "__main__":
    app.run()
