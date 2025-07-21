from dataclasses import dataclass

from deep_translator import GoogleTranslator
from textblob import TextBlob


@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(input_text: str, *, sensitivity: float) -> Mood:
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
    print("Digite algum texto para ter uma análise de sentimento:")
    while True:
        texto: str = input("Você: ")
        traduzido = GoogleTranslator(source="pt", target="en").translate(texto)
        mood: Mood = get_mood(traduzido, sensitivity=0.3)
        print(f"Bot: {mood.emoji} ({mood.sentiment})")


if __name__ == "__main__":
    run_bot()
