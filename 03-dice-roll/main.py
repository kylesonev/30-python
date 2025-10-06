"""
Rolar dados
O usuário insere a quantidade de dados de 6 lados que serão rolados.
"""


from random import randint
from collections import Counter

def pegar_quantidade() -> int:
    """
    Solicita ao usuário a quantidade de dados de 6 lados que serão rolados.

    Returns:
        int: a quantidade de dados que serão rolados.
    """
    while True: 
        try:
            quantidade = int(input("\nQuantos dados gostaria de rolar? "))
            
            if quantidade <= 0:
                print("Insira um número maior que 0...")

            else:
                return quantidade

        except ValueError:
            print("Digite um número válido! ")

def rolar_dados(quantidade: int) -> list[int]:
    """
    Rola a quantidade de dados especificada, gerando números aleatórios entre 1 e 6.

    Args:
        quantidade(int): a quantidade de dados que serão rolados.
    Returns: 
        list[int]: lista contendo os resultados dos dados rolados.

    """
    dados = []
    for _ in range(quantidade):
        dados.append(randint(1, 6))
    return dados


def mostrar_resultados(dados: list[int]) -> None:
    """
    Mostra os resultados obtidos ao rolar os dados.
    Args:
        dados(list[int]): lista contendo os resultados dos dados rolados.
    """
    quantidade = len(dados)
    print(f"\nResultado {'do dado' if quantidade == 1 else 'dos dados'}:")

    for i, dado in enumerate(dados, start=1):
            print(f"{i}° dado: {dado} ")
    


def mostrar_frequencia(opcao: str, dados: list[int]) -> None:
    """
    Mostra a frequência de cada dado contido na lista de dados rolados.
    Args:
        opcao(str): a opção inserida pelo usuário.
        dados(list[int]): lista contendo os resultados dos dados rolados.
    """
    try:
        if opcao in ('s', 'sim'):
            contagem = Counter(dados)
            print("\nFrequência dos números: ")
            for numero in range(1, 7):
                print(f"Número {numero}: {contagem.get(numero, 0)} {'vez' if contagem.get(numero, 0) <= 1 else 'vezes'}")
        elif opcao in ('n', 'não'):
            pass
    except ValueError:
        print("Entrada inválida!")


def main():
    """
    Controla o fluxo principal do programa:
    1. Solicita a quantidade de dados a serem rolados.
    2. Exibe os resultados.
    3. Pergunta se o usuário quer ver a frequência dos números.
    4. Pergunta se deseja jogar novamente.
    """
    while True:
        quantidade = pegar_quantidade()
        dados = rolar_dados(quantidade)
        mostrar_resultados(dados)
        opcao = input("\nGostaria de ver a frequência dos números? (s/n)").lower().strip()
        mostrar_frequencia(opcao, dados)
                   
        while True:
            try:
                play_again = input("\nGostaria de rolar novamente? (s/n)").lower().strip()                
                if play_again in ('s', 'sim'):
                    break
                elif play_again in ('n', 'não'):
                    print("Obrigado por jogar!")
                    return
                else:
                    print("Entrada inválida! ")
            except ValueError:
                continue

if __name__ == '__main__':
    main()
