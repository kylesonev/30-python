import customtkinter as ctk


class TaxCalculator:
    def __init__(self):
        # Inicializar a janela
        self.window = ctk.CTk()
        self.window.title("Calculadora de Imposto")
        self.window.geometry("300x200")
        self.window.resizable(False, False)

        self.padding: dict = {"padx": 20, "pady": 10}

        # Renda
        self.income_label = ctk.CTkLabel(self.window, text="Renda: ")
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        # Porcentagem
        self.tax_label = ctk.CTkLabel(self.window, text="Porcentagem: ")
        self.tax_label.grid(row=1, column=0, **self.padding)
        self.tax_entry = ctk.CTkEntry(self.window)
        self.tax_entry.grid(row=1, column=1, **self.padding)

        # Resultado
        self.result_label = ctk.CTkLabel(self.window, text="Imposto: ")
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, "0")
        self.result_entry.grid(row=2, column=1, **self.padding)

        # Botão Calculadora
        self.calculate_button = ctk.CTkButton(
            self.window, text="Calcular", command=self.calculate_tax
        )
        self.calculate_button.grid(row=3, column=1, **self.padding)

    def update_result(self, text: str):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def calculate_tax(self):
        try:
            renda: float = float(self.income_entry.get())
            porcentagem: float = float(self.tax_entry.get())
            self.update_result(f"R$ {renda * (porcentagem / 100):,.2f}")
        except ValueError:
            self.update_result("Número inválido!")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    tc = TaxCalculator()
    tc.run()
