"""
Programa chat_bot
Recebe uma mensagem do usuário e responde de acordo com o dicionário do bot.
"""

from difflib import get_close_matches

# para fazer: carregar uma json com o dicionário


def pegar_melhor_resposta(pergunta_usuario: str, conhecimento: dict) -> str | None:
    """
    Pega a melhor resposta para o texto inserido pelo usuário
    Args:
        pergunta_usuario(str): texto inserido pelo usuário
        conhecimento(dict): dicionário com a base de conhecimento do bot
    Returns:
        str: retorna a melhor resposta de acordo com o texto inserido pelo usuário
    """

    perguntas: list[str] = [q for q in conhecimento]
    combinacoes: list = get_close_matches(pergunta_usuario, perguntas, n=1, cutoff=0.6)

    if combinacoes:
        return combinacoes[0]


def chat_bot(knowledge: dict):
    """
    Executa a lógica do Programa
    1. Solicita um texto do usuário
    2. Procura dentro da base de conhecimento uma combinação para o texto do usuário
    3. Retorna a combinação ou uma mensagem dizendo que não entendeu...

    """
    usuario_entrada: str = input("You: ")
    melhor_resposta: str | None = pegar_melhor_resposta(
        pergunta_usuario=usuario_entrada, conhecimento=knowledge
    )

    if resposta := knowledge.get(melhor_resposta):
        print(f"Bot: {resposta}")
    else:
        print("Eu não entendi...")


if __name__ == "__main__":
    brain: dict = {"oi": "Olá!", "como você está": "Estou bem, e você?"}

    chat_bot(brain)
