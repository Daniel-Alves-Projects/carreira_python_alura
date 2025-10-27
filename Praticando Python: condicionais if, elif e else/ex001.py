vendas_macas = int(input('Digite a quantidade de maças vendidas: '))
vendas_bananas = int(input('Digite a quantidade de bananas vendidas: '))

if vendas_bananas > vendas_macas:
    print('As bananas tiveram mais vendas.')
elif vendas_macas > vendas_bananas:
    print('As maçãs tiveram mais vendas')
else:
    print('Bananas e Maçãs venderam a mesma quantia.')