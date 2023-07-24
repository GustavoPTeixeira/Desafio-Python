
menu = ""
LIMITE_SAQUE = 500,00
LIMITE_SAQUES = 3
deposito = 0
saque = 0
extrato = ""
numero_saques = 0

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor_deposito = float(input("Informe o valor do deposito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: RS {valor_deposito:.2f}\n"
        else:
            print("Operação falhou! O valor é inválido")
       
       
    elif opcao == "s":
       valor = float(input("informe o valor a sacar: "))
       
       excedeu_saldo = valor > excedeu_saldo
       
       excedeu_limte = valor > LIMITE_SAQUE
       
       excedeu_saques = numero_saques >= LIMITE_SAQUES
       
       if excedeu_saldo:
           print('Operação falhou! Você não tem saldo suficiente')
        
       elif excedeu_limte:
           print('Operação falhou! Valor acima do límite')
           
       elif excedeu_saques: 
           print('Operação falhou! Excedeu o limite de saques')
           
       elif valor >0:
           saldo -= valor
           extrato += f"Saque: R$ {valor:.2f}\n"
           numero_saques += 1
           
       else:
           print('Operação falhou! Valor informado é inválido')
       
    elif opcao == "e":
        print('\n=================EXTRATO=================')
        print("Não foram realizadas movimentaçãoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {valor:.2f}")
        print("===========================================")
        
    elif opcao == "q":
        break
    
    else:
        print("Opção inválida, por favor selecione novamente a opção desejada.")
