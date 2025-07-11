import qrcode

class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)


    def create_qr(self, nome_arquivo: str, fg: str, bg: str):
        user_input: str = input("Insira texto: ")

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(nome_arquivo)

            print(f"Criado com sucesso: ({nome_arquivo})")

        except Exception as e:
            print(f"Erro: {e}")



def main():
    myqr = MyQR(size=50, padding=2)
    myqr.create_qr(nome_arquivo='exemplo.png',
                   fg='#2A2B3F',
                   bg='#FFFFFF')


if __name__ == '__main__':
    main()
