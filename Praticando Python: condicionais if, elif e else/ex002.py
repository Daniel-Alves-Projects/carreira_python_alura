atividade_a = int(input('Informe os dias para a atividade A: '))

atividade_b = int(input('Informe os dias para a atividade B: '))

atividade_c = int(input('Informe os dias para a atividade C: '))

if atividade_a >= 0 and atividade_b >= 0 and atividade_c >= 0:
    total = atividade_a + atividade_b + atividade_c
    print(f'O total de dias para conclusão das atividades é {total}')
else:
    print('Os dias não podem ser negativos')