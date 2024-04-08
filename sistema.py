saldo = 0
limite = 500
extrato = ""
contadordesaques = 0
limitesaque = 500

while True:

    opcao = str(input('''
            [D] depositar
            [S] sacar
            [E] extrato
            [X] sair
    ->: ''')).strip().upper()[0]

    if opcao == 'D':
        
        valor = float(input("Digite o valor do depósito desejado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito no valor de R${valor:.2f}\n'
            print(extrato)
        else:
            print("Operação falhou!!")

    elif opcao == 'S':
        valor = float(input("Digite o valor do saque: "))

        excedeusaldo = valor > saldo
        excedeulimite = valor > limitesaque
        excedeuvezes = contadordesaques > 3

        
        if excedeusaldo:
            print("Saldo insuficiente.")

        elif excedeulimite:
            print("Limite de valor atingido.")

        elif excedeuvezes:
            print("Limite de saques diários atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque no valor de R${valor:.2f}\n'
            print(extrato)
            contadordesaques += 1
        else:
            print("Algo deu errado")
    elif opcao == 'E':
        if extrato:
            print(extrato)
        else:
            print("Não teve movimentações")
    elif opcao == 'X':
        break
