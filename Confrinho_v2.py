# VAMOS DEFINIR A class

class Cofrinho: 
    def __init__(self):
        self.saldo = 0.0
    def guardar_dinheiro(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Sucesso! R${valor:.2f} adicionado.") 
        else:
            print("Você precisa digitar um valor maior que zero")

    def ver_saldo(self):
        print(f"\n--- Seu saldo atual no cofrinho e R${self.saldo:.2f} ---")

    def quebrar_cofrinho(self):
        print(f"\n💥 Você quebrou o cofrinho! Dentro dele havia R${self.saldo:.2f}")
        self.saldo = 0.0 # opcional, zerar saldo após quebrar



cofre = Cofrinho()

while True:

    try:
        valor = float(input("Quanto dinheiro quer colocar no cofrinho? R$: "))
        cofre.guardar_dinheiro(valor)
    except ValueError:
        print("Erro: Digite números válidos (use ponto para centavos) ")

    print("\nO que você deseja agora?")
    print("1 - Depositar novamente")
    print("2 - Finalizar (não mostrar saldo)")
    print("3 - Quebrar o cofrinho e ver saldo\n")

    opcao = int(input("Escolha um opção: "))

    if opcao == 1:
        continue
    elif opcao == 2:
        print("\n✅ O cofrinho foi guardado com sucesso!")
        break
    elif opcao == 3:
        cofre.quebrar_cofrinho()
        break
    else:
        print("Opção inválida! Programa finalizado.")
        break
        

