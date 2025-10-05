"""
Rolar dados
O usuário insere a quantidade de dados de 6 lados que será rolado.
"""


from random import randint


def get_quantity() -> int:
    while True: 
        try:
            quantidade = int(input("\nQuantos dados gostaria de rolar? "))
            
            if quantidade <= 0:
                print("Insira um número maior que 0...")

            else:
                return quantidade

        except ValueError:
            print("Digite um número válido! ")


def rolling_dice(quantidade: int) -> list[int]:
    rolls = []
    for _ in range(quantidade):
        rolls.append(randint(1, 6))
    return rolls


def main():
    while True:
        quantidade = get_quantity()
        dados = rolling_dice(quantidade)
        contador = 1
        for dado in dados:
            print(f"{contador}° dado: {dado} ")
            contador += 1
        
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
