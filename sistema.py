saldo = 0
limite = 500
extrato = ""
contadordesaques = 0
limitesaque = 500

def obter_valor_valido(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Digite um valor válido!")

def deposit():
    global saldo, extrato
    valor = obter_valor_valido("Digite o valor desejado:")
    if valor > 0:
        saldo += valor
        extrato += f'- Depósito no valor de R${valor:.2f}\n'
        print(extrato)
    elif valor < 0:
        print("Não é possivel depositar valores negativos.")
    else:
        print("Operação falhou!!")

def saque(valor=0):
    global saldo, extrato, contadordesaques, limitesaque
    valor = obter_valor_valido("Digite o valor que deseja sacar: ")
    excedeusaldo = valor > saldo
    excedeulimite = valor > limitesaque
    excedeuvezes = contadordesaques > 3
    if excedeusaldo:
        print("Saldo insuficiente.")
    elif excedeulimite:
        print("Limite de valor atingido.")
    elif excedeuvezes:
        print("Limite de saques diários atingido.")
    elif valor < 0:
        print("Não é possivel sacar valores negativos.")
    else:
        saldo -= valor
        extrato += f'- Saque no valor de R${valor:.2f}\n'
        print(extrato)
        contadordesaques += 1

def mostrar_extrato():
    global extrato
    if extrato:
        print(f'{extrato}')
    else:
        print('Não houve movimentações')    

while True:

    opcao = str(input('''
            [D] - depositar
            [S] - sacar
            [E] - extrato
            [X] - sair
    ->: ''')).strip().upper()[0]

    if opcao == 'D':
        deposit()
    
    elif opcao == 'S':
         saque()

    elif opcao == 'E':
         print("\nEXTRATO:")
         print("=-="*10)
         mostrar_extrato()
         print("=-="*10)

    elif opcao == 'X':
        break

    else:
        print("Opção inválida")
