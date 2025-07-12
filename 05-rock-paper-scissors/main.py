from os import supports_dir_fd
from random import choice
import sys

class PPT:
    def __init__(self):
        print("Bem-vindo(a) ao Pedra-Papel-Tesoura!")

        self.moves: dict = {'pedra': '🪨' , 'papel': '📜', 'tesoura': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())   


    def jogar_jogo(self):
        movimento_usuario: str = input("Pedra, papel ou tesoura?").lower().strip()

        if movimento_usuario == 'sair':
            print("Obrigado por jogar!")
            sys.exit()
 

        if movimento_usuario not in self.valid_moves:
            print("Movimento inválido...")
            return self.jogar_jogo()


        movimento_maquina: str = choice(self.valid_moves)


        self.mostrar_movimentos(movimento_usuario, movimento_maquina)
        self.checar_movimentos(movimento_usuario, movimento_maquina)

    def mostrar_movimentos(self, movimento_usuario: str, movimento_maquina: str):
        print("----------")
        print(f"Você: {self.moves[movimento_usuario]}")
        print(f"Máquina: {self.moves[movimento_maquina]}")
        print("----------")

    def checar_movimentos(self, movimento_usuario: str, movimento_maquina: str):
        if movimento_usuario == movimento_maquina:
            print("Empatou!!!")
        elif movimento_usuario == 'pedra' and movimento_maquina == 'tesoura':
            print("Você ganhou!!!")
        elif movimento_usuario == 'papel' and movimento_maquina == 'pedra':
            print("Você ganhou!!!")
        elif movimento_usuario == 'tesoura' and movimento_maquina == 'papel':
            print("Você ganhou!!!")
        else:
            print("Você perdeu!!!!!")


if __name__ == '__main__':
    ppt = PPT()

    while True:
        ppt.jogar_jogo()

