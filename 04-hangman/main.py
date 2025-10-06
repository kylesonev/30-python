"""
Jogo da forca.
O usuário cria um banco de palavras a ser utilizado no jogo.
O objetivo do jogo é advinhar a palavra antes de 3 erros.
"""

from random import choice


def listar_palavras(quantidade: int) -> list[str]:
    """
    Cria uma lista com as palavras a serem utilizadas no jogo de acordo com a quantidade fornecida.
    Args:
        quantidade(int): número de palavras a serem adicionadas na lista.
    Returns:
        lista(list[str]): lista contendo as palavras a serem utilizadas no jogo.
    """
    lista_palavras: list = []
    for _ in range(quantidade):
        palavra: str = input("\nDigite uma palavra para inserir na lista do jogo: ")
        lista_palavras.append(palavra)

    return lista_palavras


def jogar(lista_palavras: list[str]):
    """
    Executa a lógica do jogo.
    O usuário tenta acertar a palavra que foi selecionada pelo choice.
    A cada acerto o '_' é substituído pela letra correta.

    Args:
        lista(list[str]): lista contendo as palavras a serem utilizadas no jogo.
    """
    palavra: str = choice(lista_palavras)

    certo: str = ""
    tentativas: int = 3

    while tentativas > 0:
        vazias: int = 0
        print("\nPalavra: ", end="")
        for caracter in palavra:
            if caracter in certo:
                print(caracter, end="")
            else:
                print("_", end="")
                vazias += 1

        if vazias == 0:
            print("\nVocê acertou!!! ")
            break

        print()
        palpite: str = input("\nDigite uma letra: ")

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
    """
    Controla o fluxo principal do jogo.
    1. Solicita o número de palavras que serão adicionadas ao banco.
    2. Insere as palavras em uma lista
    3. O usuário tenta advinhar palavra 'sorteada'
    """
    print("Primeiro vamos criar um banco com as palavras a serem jogadas.")
    quantidade: int = int(input("\nDigite a quantidade de palavras: "))
    palavras_jogo: list[str] = listar_palavras(quantidade)
    
    while True:    
        print("-----------------------------------------------------------------")
        print("Vamos jogar!!!")
        jogar(palavras_jogo)

        while True:
            try:
                jogar_novamente = input("\nGostaria de rolar novamente? (s/n)").lower().strip()
                if jogar_novamente in ('s', 'sim'):
                    break
                elif jogar_novamente in ('n', 'não'):
                    print("Obrigado por jogar!")
                    return
                else:
                    print("Entrada inválida!")
            except ValueError:
                continue


if __name__ == "__main__":
    main()
