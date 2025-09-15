"""
Jogo de adivinha.
O usuário escolhe inicialmente um alcance para gerar o número.
Após o número ser gerado o jogo se inicia, onde o usuário deverá adivinhar o número gerado.
O jogo se encerra quando o usuário adivinha o número gerado.
"""

# Realizando importação do módulo randint da biblioteca random
from random import randint


def choosing_range() -> tuple[int, int]:
    """
    Solicita ao usuário dois números.

    Returns:
        tuple(menor, maior): O menor e maior número a ser gerado.
    """
    print("Vamos escolher o alcance do número que será gerado.\n")
    print("Você deverá selecionar o menor e o maior número possível.")
    print("---------------------------------------------------------------")
    while True:
        try:
            menor = int(input("Digite o menor número: "))
            maior = int(input("Digite o maior número: "))
            if menor >= maior:
                print("O menor número de ser menor que o maior!")
            else:
                return menor, maior

        except ValueError:
            print("Digite um número inteiro!!!")


def generating_number(menor: int, maior: int) -> int:
    """
    Gera um número pseudo-aleatório com base em alcance determinado.

    Returns:
        Número inteiro gerado.
    """
    numero_gerado = randint(menor, maior)
    return numero_gerado


def guessing() -> int:
    """
    Executa o loop onde será recebido um número inteiro do usuário.
    """
    while True:
        try:
            return int(input("\nDigite o seu palpite inicial: "))
        except ValueError:
            print("Digite um número inteiro!")


def playing(guess: int, numero_gerado: int) -> None:
    """
    Executa a lógica do jogo de adivinhação.

    O usuário vai recebendo dicas se deve chutar um número maior ou menor.
    Até acertar o número gerado.

    Args:
        guess: Primeiro palpite do usuário.
        numero_gerado: Número que o usuário adeve adivinhar.
    """
    contador = 1
    while True:
        if guess > numero_gerado:
            guess = int(input("\nDigite um número menor... "))
            contador += 1
        elif guess < numero_gerado:
            guess = int(input("\nDigite um número maior... "))
            contador += 1
        else:
            print("Parabéns, você acertou!!!")
            print(f"O número era  {numero_gerado}")
            print(f"Você precisou de {contador} tentativas para acertar!")
            break
    return None


def main():
    while True:
        menor, maior = choosing_range()
        numero_gerado = generating_number(menor, maior)
        palpite = guessing()
        playing(palpite, numero_gerado)

        while True:
            continuar = input("Deseja continuar? (s/n): ").lower().strip()
            if continuar in ("s", "n"):
                break
            else:
                print("Digite uma resposta válida!")

        if continuar == "n":
            print("Valeu por jogar!")
            break


if __name__ == "__main__":
    main()
