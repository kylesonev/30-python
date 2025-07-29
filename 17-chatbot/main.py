from difflib import get_close_matches

# para fazer: carregar uma json com o dicionário


def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]


def chat_bot(knowledge: dict):
    user_input: str = input("You: ")
    best_match: str | None = get_best_match(user_input, knowledge)

    if answer := knowledge.get(best_match):
        print(f"Bot: {answer}")
    else:
        print("Eu não entendi...")


if __name__ == "__main__":
    brain: dict = {"oi": "Olá!", "como você está": "Estou bem, e você?"}

    chat_bot(brain)
