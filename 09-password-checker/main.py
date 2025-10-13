"""
Verificador de senha comum.
"""


def verificar_senha(senha: str) -> None:
    """
    Verifica o quão comum é a senha inserida pelo usuário.
    Args:
        senha(str): senha a fornecida a ser verificada.
    """
    with open("100k-most-used-passwords.txt") as file:
        senhas_comuns: list[str] = file.read().splitlines()

    for i, senha_comum in enumerate(senhas_comuns, start=1):
        if senha == senha_comum:
            print("Sua senha é muito comum!!!")
            print(f"{senha}: ⛔ (# {i})")
            return

    print("Sua senha é bem maneira!")
    print(f"{senha}: ✅ (Única)")


def main() -> None:
    """
    Executa a lógica por principal do programa.
    1. Solicita ao usuário uma senha a ser verificada.
    2. Retorna o quão comum a senha é.
    """
    usuario: str = input("Digite uma senha para verificar: ")
    verificar_senha(usuario)


if __name__ == "__main__":
    main()
