class Cofrinho:
    def __init__(self):
        self.saldo = 0.0

    def guardar_dinheiro(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Sucesso! R$ {valor:.2f} adicionado.")
        else:
            print("Você precisa digitar um valor maior que zero!")

    def ver_saldo(self):
        print(f"\n--- Seu saldo atual no cofrinho é R$ {self.saldo:.2f} ---")


# Uso fora da classe
cofre = Cofrinho()
try:
    valor = float(input("Quanto dinheiro você quer colocar no cofrinho? R$: "))
    cofre.guardar_dinheiro(valor)
except ValueError:
    print("Erro: Digite apenas números válidos (use ponto para centavos).")

cofre.ver_saldo()
