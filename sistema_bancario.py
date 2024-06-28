from datetime import datetime

import textwrap



def menu():

    menu = """

    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Nova Conta
    [4] Listar Contas
    [5] Novo Usuário
    [6] Sair

    => """

    return input(textwrap.dedent(menu))


agencia = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
data_hoje = datetime.now()
data_saque = data_hoje.strftime("%d %B %Y, %H:%M")
usuarios = []
contas = []



def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"{data_saque} | Depósito: R$ {valor:.2f}\n"
        print(f"\nValor depositado com sucesso! Seu novo saldo é: R$ {saldo:.2f}")
    else:
        print("\nO valor informado não é válido, por favor reinicie a operação!")

    return saldo, extrato



def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nFalha na operação! Saldo insulficiente.")

    elif excedeu_limite:
        print("\nFalha na operação! O valor do saque excedeu o limite diário.")

    elif excedeu_saques:
        print("\nFalha na operação! Número máximo de saques foi excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"{data_saque} | Saque: R$ {valor:.2f}\n" 
        numero_saques += 1
        print(f"\nSaque realizado com sucesso! Seu novo saldo é: R$ {saldo:.2f}")

    else:
        print("\nO valor informado não é válido, por favor reinicie a operação!")

    return saldo, extrato



def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================\n")
    print("Não constam movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n==========================================")



def criar_usuario(usuarios):
    cpf = input("Digite o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe cadastro para este usuário (Confira o CPF digitado)!")
        return

    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (DD-MM-AAAA): ")
    endereco = input("Digite o endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nCadastro de usuário realizado com sucesso!\n")



def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None



def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não localizado, por favor reinicie a operação!")



def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))



while True:

    opcao = menu()

    if opcao == "0":
        valor = float(input("Informe o valor a ser depositado: "))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = limite_saques,
            )

    elif opcao == "2":
        exibir_extrato(saldo, extrato = extrato)

    elif opcao == "3":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

    elif opcao == "4":
            listar_contas(contas)

    elif opcao == "5":
            criar_usuario(usuarios)

    elif opcao == "6":
        print ("\nObrigado por utilizar nossos serviços. Até breve!\n") 
        break

    else:
        print("Operação inválida, por favor reinicie a operação!")