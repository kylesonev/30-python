import string
import secrets


def gerar_senha(tamanho: int, nivel: int) -> str:
    """
    A senha será gerada de acordo com o tamanho e nível inseridos pelo usuário.
    Args:
        tamanho(int): o tamanho que a senha terá, devendo ser maior que 6.
        nivel(int): o nível que a senha terá, sendo:
        - Fraca (minúsculas e números)
        - Média (minúsculas, maiúsculas e números)
        - Forte (minúsculas, maiúsculas, números e caracteres especiais)
    Returns:
        senha(str): senha gerada de acordo com o número e nível
    """

    senha = ""
    if nivel == 1:
        combinacao: str = string.ascii_lowercase + string.digits

    if nivel == 2:
        combinacao: str = string.ascii_letters + string.digits

    if nivel == 3:
        combinacao: str = string.ascii_letters + string.digits + string.punctuation

    return senha.join(secrets.choice(combinacao) for _ in range(tamanho))



def main():
    """
    Executa a lógica do programa.
    1. O usuário indica quantas senhas gostaria de criar.
    2. O usuário indica o número de caracteres que a senha deverá conter.
    3. O usuário indica a força da senha.
    4. As senhas são geradas e mostradas na tela.
    """
    while True:
        try:
            total_senhas: int = int(input("Quantas senhas deseja gerar? "))
            if total_senhas <= 0:
                print("Digite um total de senhas maior que 0!")
                continue

            tamanho: int = int(
                input(
                    "\nInsira o número de caracteres que a senha deve conter(mínimo 6): "
                )
            )
            if tamanho <= 5:
                print("Digite um tamanho maior que 0!")
                continue

            print(
                "\nSelecione o nível da senha: \n"
                "1 - Fraca: contém Letras minúsculas e números \n"
                "2 - Média: contém Letras minúsculas, maiúsculas e números\n"
                "3 - Forte: contém Letras minúsculas, maiúsculas, números e caracteres especiais"
            )
            nivel: int = int(input())
            if nivel not in [1, 2, 3]:
                print("Digite um nível válido!")
                continue
            break

        except ValueError:
            print("Digite um número válido!")

    print("\nSenhas geradas:\n" + "-" * 20)

    for _ in range(total_senhas):
        senha = gerar_senha(tamanho=tamanho, nivel=nivel)
        print(senha)


if __name__ == "__main__":
    main()
