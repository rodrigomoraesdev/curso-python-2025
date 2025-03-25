#%%

def par_impar(x:int) -> int:
    '''
    A fóruma par_impar recebe um número inteiro e retorna 
    se ele é par ou ímpar.
    '''
    if x % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Ímpar'
    print(f'O número informado: {x} é {resultado}')
    return 

while True:
    numero = input("Digite um número: ")
    if numero == '':
        break
    else:
        numero_int  = int(numero)  
        par_impar(numero_int)