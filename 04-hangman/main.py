from random import choice


def list_words(quantidade: int) -> list[str]:
    lista: list = []
    for _ in range(quantidade):
        palavra: str = input("Digite uma palavra para inserir na lista do jogo: ")
        lista.append(palavra)

    return lista


def run_game(lista: list[str]):
    palavra: str = choice(lista)

    certo: str = ""
    tentativas: int = 3

    while tentativas > 0:
        vazias: int = 0
        print("Palavra: ", end="")
        for char in palavra:
            if char in certo:
                print(char, end="")
            else:
                print("_", end="")
                vazias += 1
        print()

        if vazias == 0:
            print("Você acertou!!! ")
            break

        palpite: str = input("Digite uma letra: ")

        if palpite in certo:
            print(f"Você já tentou:  {palpite}'. Tente outra letra!")
            continue
        certo += palpite

        if palpite not in palavra:
            tentativas -= 1
            print(f"Desculpe, você errou... {tentativas}  restantes.")
            if tentativas == 0:
                print("Você perdeu...")
                break


def main() -> None:
    nome: str = input("Qual o seu nome? ")
    print(f"Bem-vindo(a) {nome}")
    quantidade: int = int(input("Digite a quantidade de palavras: "))
    palavras_jogo: list[str] = list_words(quantidade)
    run_game(palavras_jogo)


if __name__ == "__main__":
    main()
