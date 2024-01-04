from datetime import datetime

class EasyBank:

    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = {}

    def inicializar_contador_diario(self):
        hoje = datetime.now().date()
        if hoje not in self.saques_diarios:
            self.saques_diarios[hoje] = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +{valor}")
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Erro : O valor do depósito precisa ser maior que zero")

    def sacar(self, valor):
        self.inicializar_contador_diario()
        hoje = datetime.now().date()
        if self.saques_diarios[hoje] < 3:
            if valor > 0 and valor <= 500 and valor <= self.saldo:
                self.saldo -= valor
                self.extrato.append(f"Sque: -{valor}")
                self.saques_diarios[hoje] += 1
                print(f"Saque de R${valor} realizado com sucesso.")
            else:
                print("Erro: Saldo insuficiente ou valor do saque inválido.")
        else:
            print("Limite de saques diários excedido. Não é permitido mais saques hoje.")


    def mostrar_extrato(self):
        print("\n--- EXTRATO ---")
        for movimento in self.extrato:
            print(movimento)
        print(f"Saldo atual: R${self.saldo}\n")

if __name__== "__main__":
    app = EasyBank()

    
    while True:
        print("\n   Easy Bank  ")
        print("1 - Depositar")
        print("2 - Saque")
        print("3 - Extrato")
        print("4 - Sair")

        escolha = input("Escolha uma opção:")

        if escolha == "1":
            valor_deposito = float(input("Digite o valor para depósito:"))
            app.depositar(valor_deposito)
        elif escolha == "2":
            valor_saque = float(input("Digite o valor para saque:"))
            app.sacar(valor_saque)
        elif escolha == "3":
            app.mostrar_extrato()
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha um aopção válida")
