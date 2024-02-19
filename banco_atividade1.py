menu = '''Bem Vindo ao Banco Python!!!

Por favor digite uma das opções abaixo:

[1] Deposito
[2] Saque
[3] Extrato
[0] Sair

Operação Desejada:'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        print("\n####Deposito####\n")
        valor_deposito = float(input("Por favor, insira o valor a ser depositado:"))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
            print("O valor depositado já está disponível em sua conta!")
        else:
            print("Valor inválido!!!")
        
    elif opcao == 2:
        print("\n####Saque####\n")
        valor_saque = float(input("Por favor, insira o valor a ser sacado:")) 
        if numero_saques < LIMITE_SAQUES:
            if valor_saque <= 500:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    numero_saques += 1
                    extrato += f"Saque: R${valor_saque:.2f}\n"
                    print("Saque concluído, retire o valor solicitado!")
                else:
                    print("Você não possui saldo suficiente para concluir esta operação!")
            else:
                print("O valor selecionado excede o limite por transação!")
        else:
            print("Número de saques diários excedido!")
        


    elif opcao == 3:
        print("\n####Extrato####")
        print("\n=======================")
        print(extrato)
        print(f'Saldo em conta: R${saldo:.2f}')
        print("=======================")

    elif opcao == 0:
        print("Obrigado por utilizar os nossos sistemas bancários!")
        break
    else:
        print("Operação inválida, selecione novamente a operação desejada")
