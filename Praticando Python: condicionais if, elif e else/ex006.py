horario = int(input('Digite a hopra atual (Formato 24 horas)'))
if horario < 8 or horario > 18:
    print('Acesso negado')

else: 
    print('Acesso permitido')