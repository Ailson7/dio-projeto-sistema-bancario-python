from datetime import datetime

menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
data_hoje = datetime.now()
data_saque = data_hoje.strftime("%d %B %Y, %H:%M")

while True:

    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"{data_saque} | Depósito: R$ {valor:.2f}\n"
            print (f"\nValor depositado com sucesso! Seu novo saldo é: R$ {saldo:.2f}") 

        else:
            print("O valor informado não é válido, por favor reinicie a operação!")

    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Falha na operação! Saldo insulficiente.")

        elif excedeu_limite:
            print("Falha na operação! O valor do saque excedeu o limite diário.")

        elif excedeu_saques:
            print("Falha na operação! Número máximo de saques foi excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"{data_saque} | Saque: R$ {valor:.2f}\n" 
            numero_saques += 1
            print (f"\nSaque realizado com sucesso! Seu novo saldo é: R$ {saldo:.2f}")

        else:
            print("O valor informado não é válido, por favor reinicie a operação!")

    elif opcao == "2":
        print("\n================ EXTRATO ================\n")
        print("Não constam movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n==========================================")

    elif opcao == "3":
        print ("\nObrigado por utilizar nossos serviços. Até breve!\n") 
        break

    else:
        print("Operação inválida, por favor reinicie a operação!")