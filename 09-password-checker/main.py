def check_senha(senha: str) -> None:
    with open('09-password-checker/100k-most-used-passwords.txt') as file:
        senhas_comuns: list[str] = file.read().splitlines()

    for i, senha_comum in enumerate(senhas_comuns, start=1):
        if senha == senha_comum:
            print("Sua senha é muito comum!!!")
            print(f"{senha}: ⛔ (# {i})")
            return

    print("Sua senhe é bem maneira!")
    print(f"{senha}: ✅ (Unique)")


def main() -> None:
    usuario: str = input("Digite uma senha para verificar: ")
    check_senha(usuario)


if __name__ == '__main__':
    main()
