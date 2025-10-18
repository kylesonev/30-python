"""
Bot de análise de sentimento.
"""

from dataclasses import dataclass

from deep_translator import GoogleTranslator
from textblob import TextBlob


@dataclass
class Mood:
    """
    Definição dos atributos da classe
    """

    emoji: str
    sentiment: float


def get_mood(input_text: str, *, sensitivity: float) -> Mood:
    """
    Recebe o texto do usuário e a sensi do bot para realizar a análise
    Args:
        input_text(str): o texto inserido pelo usuário
        sensitivity(float): o nível de sensibilidade do bot

    """
    polarity: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold: float = sensitivity
    hostile_threshold: float = -sensitivity

    if polarity >= friendly_threshold:
        return Mood("☺️", polarity)
    elif polarity <= hostile_threshold:
        return Mood("😠", polarity)
    else:
        return Mood("😐", polarity)


def run_bot():
    """
    Executa a lógica do programa.
    1. Solicita ao usuário para inserir um texto
    2. Executa a análise de sentimento desse texto

    """
    print("Digite algum texto para ter uma análise de sentimento:")
    while True:
        texto: str = input("Você: ")
        traduzido = GoogleTranslator(source="pt", target="en").translate(texto)
        mood: Mood = get_mood(traduzido, sensitivity=0.3)
        print(f"Bot: {mood.emoji} ({mood.sentiment})")


if __name__ == "__main__":
    run_bot()
