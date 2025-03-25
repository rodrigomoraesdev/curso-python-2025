#%%

def soma(a:float, b:float, *args) -> float:
    valores = [a, b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args) -> float:
    valores = [a, b] + list(args)
    return soma(a, b, *args) / (len(args) + 2)

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
d = float(input("Digite o quarto número: "))

print('A media dos números é:', media(a,b,c,d))

#%%
