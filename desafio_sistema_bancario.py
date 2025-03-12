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
