# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute é maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.

#%%
#Bibliotecas
import random

#Número Sorteado
sorteio = random.randint(1,15)
print(sorteio)

# Input

def get_input():
    while True:
            try:
                escolha = int(input('Infome o número que acredita ser o sorteado:'))
            except ValueError as err:
                print('Valor inválido! Digite um número válido.')
                continue
            
            if 1 <= escolha <= 15:
                return escolha
            print('Valor inválido!, o número deve ser entre 1 e 15')

def check_numbers(sorteio, escolha):
    if escolha == sorteio:
        print(f'Parabéns, você acertou o número sorteado: {sorteio}')
        return True
    elif escolha <= sorteio:
        print(f'Errado, o número sorteado é maior que {escolha} ')
        return False
    else:
        print(f'Errado, o número sorteado é menor que {escolha} ')   
        return False    

for i in range(3):
        escolha = get_input()
        if check_numbers(sorteio, escolha):
             break
        elif i == 2:
            print('Você excedeu 3 tentativas')

        









1# %%

# %%
