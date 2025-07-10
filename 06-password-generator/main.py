import string 
import secrets

def contem_maiuscula(senha: str) -> bool:

    for char in senha:
        if char.isupper():
            return True

    return False


def contem_simbolo(senha: str) -> bool:
    
    for char in senha:
        if char in string.punctuation:
            return True
    
    return False


def gerar_senha(tamanho: int, simbolos: bool, maiuscula: bool) -> str:

    combinacao: str = string.ascii_lowercase + string.digits


    if simbolos:
        combinacao += string.punctuation

    if maiuscula:
        combinacao += string.ascii_uppercase

    combinacao_comprimento: int = len(combinacao)

    nova_senha: str = ''

    for _ in range(tamanho):
        nova_senha += combinacao[secrets.randbelow(combinacao_comprimento)]

    
    return nova_senha



if __name__ == '__main__':
    for i in range(1):
        n_senha: str = gerar_senha(tamanho=12, simbolos=True, maiuscula=True)
        specs: str = f"M: {contem_maiuscula(n_senha)}, S: {contem_simbolo(n_senha)}"

        print(len(n_senha))
        print(f"{i} -> {n_senha} ({specs})")
