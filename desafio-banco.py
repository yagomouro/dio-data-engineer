def exibir_menu():
    print("""
    Bem-vindo!
    
    Escolha a operação desejada:
    1 - Depósito
    2 - Saque
    3 - Extrato
    4 - Sair
    """)

def realizar_deposito(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido. O depósito não foi realizado.")
    return saldo, extrato

def realizar_saque(saldo, extrato, numero_saques, limite_saques, limite):
    if numero_saques >= limite_saques:
        print("Você já realizou o número máximo de saques diários.")
        return saldo, extrato, numero_saques

    valor = float(input("Informe o valor do saque: "))
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor > limite:
        print(f"O valor do saque excede o limite permitido de R$ {limite:.2f}.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido. O saque não foi realizado.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n=== Extrato ===")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for item in extrato:
            print(item)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("================\n")

def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            saldo, extrato = realizar_deposito(saldo, extrato)
        elif opcao == "2":
            saldo, extrato, numero_saques = realizar_saque(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        elif opcao == "4":
            print("Obrigado por usar o Banco Python. Até logo!")
            break
        else:
            print("Opção inválida! Escolha uma opção válida.")

if __name__ == "__main__":
    main()
