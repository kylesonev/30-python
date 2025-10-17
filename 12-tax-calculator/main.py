"""
Calculadora de impostos
"""

import customtkinter as ctk


class CalculadoraImposto:
    """
    Classe responsável pela criação e execução da calculadora de impostos.
    """

    def __init__(self):
        """
        Inicializa a janela principal com todos os componentes da interface.
        """
        # Inicializar a janela
        self.window = ctk.CTk()
        self.window.title("Calculadora de Imposto")
        self.window.geometry("300x200")
        self.window.resizable(False, False)

        self.padding: dict = {"padx": 20, "pady": 10}

        # Renda
        self.renda_label = ctk.CTkLabel(self.window, text="Renda: ")
        self.renda_label.grid(row=0, column=0, **self.padding)
        self.renda_entry = ctk.CTkEntry(self.window)
        self.renda_entry.grid(row=0, column=1, **self.padding)

        # Porcentagem
        self.imposto_label = ctk.CTkLabel(self.window, text="Porcentagem: ")
        self.imposto_label.grid(row=1, column=0, **self.padding)
        self.imposto_entry = ctk.CTkEntry(self.window)
        self.imposto_entry.grid(row=1, column=1, **self.padding)

        # Resultado
        self.resultado_label = ctk.CTkLabel(self.window, text="Imposto: ")
        self.resultado_label.grid(row=2, column=0, **self.padding)
        self.resultado_entry = ctk.CTkEntry(self.window)
        self.resultado_entry.insert(0, "0")
        self.resultado_entry.grid(row=2, column=1, **self.padding)

        # Botão Calculadora
        self.botao_calcular = ctk.CTkButton(
            self.window, text="Calcular", command=self.calcular_imposto
        )
        self.botao_calcular.grid(row=3, column=1, **self.padding)

    def atualizar_resultado(self, text: str) -> None:
        """
        Atualiza o campo de resultado.
        Args:
            text(str): texto que será exibido no campo de resultado.
        """
        self.resultado_entry.delete(0, ctk.END)
        self.resultado_entry.insert(0, text)

    def calcular_imposto(self) -> None:
        """
        Realiza o cálculo do imposto com base na renda e porcentagem inseridas.

        O valor é exibido no campo de resultado formatado em reais (R$).
        Caso o usuário insira um valor inválido, é exibida uma mensagem de erro.
        """
        try:
            renda: float = float(self.renda_entry.get())
            porcentagem: float = float(self.imposto_entry.get())
            self.atualizar_resultado(f"R$ {renda * (porcentagem / 100):,.2f}")
        except ValueError:
            self.atualizar_resultado("Número inválido!")

    def run(self) -> None:
        """
        Inicia o loop principal da aplicação, mantendo a janela aberta.
        """
        self.window.mainloop()


if __name__ == "__main__":
    """
    Cria uma instância da classe CalculadoraImposto e inicia a execução.
    """
    tc = CalculadoraImposto()
    tc.run()
