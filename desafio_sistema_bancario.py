# Author: Pedro Azevedo da Conceição
# Github: PedroAzC
# Project made for Python Developer Training, from DIO
# This s my solution for the Bank sistem challenge fro DIO

# Autor: Pedro Azevedo da Conceição
# Github: 
# Formação Python Developer
# Codigo para resolucao do desafio sistema bancario da DIO

# table who shows the user valid commands

""" menu = '''
[s] saque
[d] deposito
[e] extrato
[c] cancelar
'''

saldo = 0

valor_saque_atual = 0
VALOR_SAQUE_MAX = 500.00

num_saque_atual = 0
NUM_SAQUE_MAX = 3

extrato = []

while True:

    operacao = input(menu)
    if operacao == "s":

        if num_saque_atual < NUM_SAQUE_MAX:
            print("Insira o valor que deseja sacar ate R$500,00")
            valor_saque_atual = int(input())

            if ((valor_saque_atual <= VALOR_SAQUE_MAX) and (valor_saque_atual> 0) and (valor_saque_atual <= saldo)): # verifica as condicoes para uma operação valida 
                print("Sucesso! O valor sacado foi de: R$",valor_saque_atual)
                saldo = saldo - valor_saque_atual        
                print("Sua conta agora possui R$",saldo,"de saldo")
                extrato.append(valor_saque_atual)  
                num_saque_atual += 1 
                       

            elif valor_saque_atual > saldo:
                print("Saldo insuficiente! Voce possui R$",saldo,"de saldo")

            elif valor_saque_atual > VALOR_SAQUE_MAX:
                print("Valor de saque superior ao limite!")

            elif valor_saque_atual == 0:
                print("Erro! Valor de saque é zero!")

            else:
                print("Um erro inesperado aconteceu!")        
        else:
            print("Número de saques diários excedido!")

    elif operacao == "d":
        print("Insira o valor que deseja depositar.")
        deposito = int(input())
        saldo = saldo + deposito
        print("Seu novo saldo é de: R$",saldo)

    elif operacao == "e":
        print("Seu extrato é:")
        
        for i in range(int(num_saque_atual),0,-1):  # loop necessario para exibir o extrato completo, podendo variar de numero de operações, caso mudemos NUM_SAQUE_MAX
            print(f"R$ {extrato[i-1]} Operação",i) # em um sistema mais completo, adicionaria a data e horario da operação

    elif operacao == "c":
        print("Operação encerrada! Volte sempre!")
        break

    else:
        print("Erro. Comando inválido")
 """

# Author: Pedro Azevedo da Conceição
# Github: PedroAzC
# Project made for Python Developer Training, from DIO
# This s my solution for the Bank sistem challenge fro DIO

# Autor: Pedro Azevedo da Conceição
# Github: 
# Formação Python Developer
# Codigo para resolucao do desafio sistema bancario da DIO

# table who shows the user valid commands

menu = '''
[w] withdraw
[d] deposit
[s] statement
[c] cancel
'''

balance = 0

current_withdraw_value = 0
MAX_WITHDRAW_VALUE = 500.00

current_withdraw_number = 0
MAX_WITHDRAW_NUMBER = 3

statement = []

while True:

    operation = input(menu)
    if operation == "w":

        if current_withdraw_number < MAX_WITHDRAW_NUMBER:
            print("Insert withdraw value up to R$500,00")
            current_withdraw_value = int(input())

            if ((current_withdraw_value <= MAX_WITHDRAW_VALUE) and (current_withdraw_value> 0) and (current_withdraw_value <= balance)): # verifica as condicoes para uma operação valida 
                print("Success! WHitdraw value is: R$",current_withdraw_value)
                balance = balance - current_withdraw_value        
                print("Your account now has R$",balance)
                statement.append(current_withdraw_value)  
                current_withdraw_number += 1 
                        

            elif current_withdraw_value > balance:
                print("Insuficient funds! You have R$",balance)

            elif current_withdraw_value > MAX_WITHDRAW_VALUE:
                print("Error! Wthdraw value higher than your balance!")

            elif current_withdraw_value == 0:
                print("Error! Whithdraw value is zero!")

            else:
                print("An unexpected error occured!")        
        else:
            print("Number of daily withdraw exceeded!")

    elif operation == "d":
        print("Insert deposit value.")
        deposit = int(input())
        balance = balance + deposit
        print("You new balance is: R$",balance)

    elif operation == "s":
        print("Your statement is:")
        
        for i in range(int(current_withdraw_number),0,-1):  # loop necessario para exibir o bank_statement completo, podendo variar de numero de operações, caso mudemos MAX_WITHDRAW_NUMBER
            print(f"R$ {statement[i-1]} Operation",i) # em um sistema mais completo, adicionaria a data e horario da operação

    elif operation == "c":
        print("Operation closed! Come back soon!")
        break

    else:
        print("Error. Invalid command") 