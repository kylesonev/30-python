"""
Programa gerador de Código QR.
"""

import qrcode


class MyQR:

    def __init__(self, size: int, padding: int) -> None:
        """
        Inicializa os atributos da classe MyQR
        Args:
            size(int): tamanho em px que será criada a imagem
            padding(int): paddin em px que será criada a imagem
        """
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, fg: str, bg: str) -> None:
        """
        Função responsável por criar a imagem do QRCode
        Args:
            fg(str): Define a cor em HEX do 'traçado' do QRCode
            bg(str): Define a cor em HEX de fundo do QRCode
        """
        entrada_usuário: str = input("Insira um link: ")

        nome_arquivo = self.criar_nome()

        try:
            self.qr.add_data(entrada_usuário)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(nome_arquivo)

            print(f"Criado com sucesso: ({nome_arquivo})")

        except Exception as e:
            print(f"Erro: {e}")

    def criar_nome(self) -> str:
        """
        Solicita ao usuário uma definição de como será salvo o arquivo do QRCode
        Returns:
            str: retorna o nome do arquivo juntamente da extensão .png
        """

        while True:
            nome = input("Digite o nome de como salvará o arquivo: ").lower().strip()
            if nome:
                return nome + ".png"
            print("Nome inválido!")


def main():
    """
    Executa a lógica do programa
    - Solicita ao usuário um link ou texto para transformar em QRCode
    - Solicita ao usuário um nome para salvar o arquivo
    """
    myqr = MyQR(size=50, padding=2)
    myqr.create_qr(fg="#2A2B3F", bg="#FFFFFF")


if __name__ == "__main__":
    main()
