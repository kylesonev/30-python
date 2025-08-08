from random import randint


def choosing_range() -> tuple[int, int]:
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
    numero_gerado = randint(menor, maior)
    return numero_gerado


def guessing() -> int:
    while True:
        try:
            return int(input("\nDigite o seu palpite inicial: "))
        except ValueError:
            print("Digite um número inteiro!")


def playing(guess: int, numero_gerado: int) -> None:
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
