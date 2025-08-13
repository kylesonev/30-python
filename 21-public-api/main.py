from datetime import datetime
from random import choice, randint

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    phrases: list[str] = ["Bem-vindo!", "Você está bacana!", "O tempo está ótimo!"]
    return {"phrase": choice(phrases), "date": datetime.now()}


@app.route("/api/random")
def random():
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
