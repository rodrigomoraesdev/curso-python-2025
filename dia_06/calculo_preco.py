#%%

def calc_imposto(preco:float, taxa_base:float, **kwargs) -> float:
    '''
    Função para calcular o imposto de um produto

    Parâmetros:
    preco: float - preço do produto
    taxa_base: float - taxa base de imposto
    **kwargs: dicionário - impostos adicionais

    Retorna:
    float - valor do imposto

    '''
    imposto =  preco * taxa_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]
    return imposto


impostos_gerais = {'municipio': 0.01, 'estado': 0.005, 'federal': 0.001}

calc_imposto(100, 0.03, **impostos_gerais)
 