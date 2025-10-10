from random import choice
import sys


class PPT:
    def __init__(self) -> None:
        """
        Inicializa os atributos inicias da classe PPT.
        """
        print("Bem-vindo(a) ao Pedra-Papel-Tesoura!\n")
        self.moves: dict[str, str] = {
            "pedra": "🪨", "papel": "📜", "tesoura": "✂️"}
        self.valid_moves: list[str] = list(self.moves.keys())
        self.empate: int = 0
        self.vitoria: int = 0
        self.derrota: int = 0

    def jogar_jogo(self) -> None:
        """
        Executa a lógica por trás do jogo.
        - Solicita o movimento do usuário, realizando a checagem de movimento válido.
        - Gera um movimento para a 'máquina'
        - Mostra os dois movimentos: Usuário e Máquina.
        - Determina o resultado da rodada (Vitória, empate ou derrota)
        - Pergunta ao usuário se gostararia de continuar jogando.
        """
        print("Pedra, papel ou tesoura? ")
        movimento_usuario: str = input().lower().strip()

        if movimento_usuario not in self.valid_moves:
            print("Movimento inválido...")
            return self.jogar_jogo()

        movimento_maquina: str = choice(self.valid_moves)

        self.mostrar_movimentos(movimento_usuario, movimento_maquina)
        self.checar_movimentos(movimento_usuario, movimento_maquina)
        self.continuar_jogo()

    def mostrar_movimentos(
        self, movimento_usuario: str, movimento_maquina: str
    ) -> None:
        """
        Exibe os movimentos da rodada: Usuário e Máquina.
        Args:
            movimento_usuario(str): jogada do usuário (Pedra, papel ou tesoura)
            movimento_maquina(str): jogada da máquina (Pedra, papel ou tesoura)
        """
        print("-------------")
        print(f"Você: {self.moves[movimento_usuario]}")
        print(f"Máquina: {self.moves[movimento_maquina]}")
        print("-------------")

    def checar_movimentos(self, movimento_usuario: str, movimento_maquina: str) -> None:
        """
        Compara os movimentos do usuário e da máquina, determina o resultado da rodada
        e atualiza os contadores de vitórias, derrotas e empates.

        Args:
            movimento_usuario(str): jogada do usuário -> Pedra, papel ou tesoura
            movimento_maquina(str): jogada da máquina -> Pedra, papel ou tesoura
        """

        if movimento_usuario == movimento_maquina:
            print("Empatou!!!")
            self.empate += 1
        elif movimento_usuario == "pedra" and movimento_maquina == "tesoura":
            print("Você ganhou!!!")
            self.vitoria += 1
        elif movimento_usuario == "papel" and movimento_maquina == "pedra":
            print("Você ganhou!!!")
            self.vitoria += 1
        elif movimento_usuario == "tesoura" and movimento_maquina == "papel":
            print("Você ganhou!!!")
            self.vitoria += 1
        else:
            print("Você perdeu!!!!!")
            self.derrota += 1

    def continuar_jogo(self) -> None:
        """
        Pergunta ao usuário se deseja jogar outra rodada.
        Caso não deseje, exibe o placar final e finaliza o programa.
        """

        while True:
            opcao = input("\nDeseja continuar jogando? (s/n) ").strip().lower()

            if opcao in ("sim", "s"):
                break
            elif opcao in ("não", "n"):
                print(
                    f"Você ganhou: {self.vitoria} {'vez' if self.vitoria <= 1 else 'vezes'}"
                )
                print(
                    f"Você perdeu: {self.derrota} {'vez' if self.derrota <= 1 else 'vezes'}"
                )
                print(
                    f"Você empatou: {self.empate} {'vez' if self.empate <= 1 else 'vezes'}"
                )
                print("Valeu por jogar! Até mais!")
                sys.exit()
            else:
                print("Opção inválida!")


if __name__ == "__main__":
    ppt = PPT()

    while True:
        ppt.jogar_jogo()
