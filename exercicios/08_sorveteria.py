#%%
print('Bem-vindo à sorveteria')

#Tipo Sorvete
print('''Tipo Sorvete
1 - Casquinha: R$ 1,00  
2 - Cascão: R$ 2,50
3 - Cestinha: R$ 4,00''')
tipo = input('Escolha o código do tipo de sorvete: ')

if tipo == '1':
    tipo = 'Casquinha'
    tipovalor = 1.00
elif tipo == '2':
    tipo = 'Cascão'
    tipovalor = 2.50
elif tipo == '3':
    tipo = 'Cestinha'
    tipovalor = 4.00
else:
    print('Tipo de sorvete não encontrado, digite uma opção correta')
    exit()
#Sabor Sorvete
print('''Sabor Sorvete
1 - Morango
2 - Creme
3 - Chocolate''')
sabor  = input('Escolha o código do sabor do sorvete: ')

if sabor == '1':
    sabor = 'Morango'
elif sabor == '2':
    sabor = 'Creme'
elif sabor == '3':
    sabor = 'Chocolate'
else:
    print('Sabor de sorvete não encontrado, digite uma opção correta')
    exit()
    
#Cobertura
print('''Cobertura
1 - Caramelo: R$ 1,50'
2 - Morango: R$ 1,50''
3 - Chocolate: R$ 1,50''')
cobertura = input('Escolha o código da cobertura: ')

if cobertura == '1':
    cobertura = 'Caramelo'
    coberturavalor = 1.50
elif cobertura == '2':
    cobertura = 'Morango'
    coberturavalor = 1.50
elif cobertura == '3':
    cobertura = 'Chocolate'
    coberturavalor = 1.50
else:
    print('Cobertura não encontrada, digite uma opção correta')
    exit()

total = tipovalor + coberturavalor
print(f'Sorvete escolhido: {tipo} + {sabor} + {cobertura}. Total R${total}')


