# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute é maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.

#%%
import random

sorteio = random.randint(1, 15)

def get_input():
    while True:
        try:
            escolha = int(input('Escolha o número sorteado:'))
        except ValueError as err:
            print('Valor inválido!')
            continue

        if 1 <= escolha <= 15:
            return escolha
        print('Valor inválido!, o número deve ser entre 1 e 15')

def check_numbers(sorteio, escolha):
    if escolha < sorteio:
        print(f'O Número sorteado é maior do que {escolha}.\n')
        return False
    elif escolha > sorteio:
        print(f'O Número sorteado é menor do que {escolha}.\n')
        return False
    else:
        print(f'Parabéns você acertou, o número escolhido é {sorteio}\n')
        return True

for i in range(3):
        escolha = get_input()
        if check_numbers(sorteio,escolha):
            break
else:
    print('Número de tentativas ultrapassou 3, tente novamente\n')