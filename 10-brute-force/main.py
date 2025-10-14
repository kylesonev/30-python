import itertools
import string
import time


def palpite_comum(palavra: str) -> str | None:
    """
    Verifica um arquivo cheio de palavras comuns e procura a palavra passada pelo usuário nesse arquivo
    Args:
        word(str): palavra que será crackeada.

    Returns:
        str: Retorna a posição da palavra no banco de palavras
    """

    with open("words.txt", "r") as palavras:
        lista_palavras: list[str] = palavras.read().splitlines()

    for i, match in enumerate(lista_palavras, start=1):
        if match == palavra:
            return f"Combinação: {match} (#{i})"


# Goes through every combination of chars
def forca_bruta(word: str, length: int, digits=False, symbols=False) -> str | None:
    """
    Executa força bruta para crackear uma palavra.
    """

    # Modify this for total symbols
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for palpite in itertools.product(chars, repeat=length):
        attempts += 1
        guess: str = "".join(palpite)

        if guess == word:
            return f'"{word}" foi crackeada em {attempts:,} palpites.'
        # print(guess, attempts) # Comentar se não estiver testando


def main():
    print("Procurando...")
    password: str = "godofwar"

    start_time: float = time.perf_counter()

    if common_match := palpite_comum(password):
        print(common_match)
    else:
        if cracked := forca_bruta(password, length=5, digits=True, symbols=False):
            print(cracked)
        else:
            print("Não houve combinação...")

    # Get the end time
    end_time: float = time.perf_counter()

    # Display the time it took
    print(round(end_time - start_time, 2), "s")


if __name__ == "__main__":
    main()
