 #%%
nome_fruta = input("Digite o nome da fruta: ")

frutas = {
    "Pera": "R$1,25",
    "Goiaba": "R$2,15",
    "Abacaxi": "R$3,20",
    "Jaca": "R$5,80",
    "Laranja": "R$0,65",
    "Limão": "R$1,25",
    "Maçã": "R$1,50",
    "Banana": "R$2,75",
    "Uva": "R$1,90"
}

if nome_fruta in frutas:
    print(f'{nome_fruta}:',frutas[nome_fruta])
else:
    print("Fruta não encontrada")