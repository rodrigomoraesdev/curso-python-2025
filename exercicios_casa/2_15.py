#%% 
lista = [1, 2,4,5,6,4,3,1,2,3,2,2,2,1,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
numero = input("Digite uma lista de números separados por espaço: ")
numero = int(numero)

contador = 0
for i in lista:
    if i == numero:
        contador += 1
print(contador)