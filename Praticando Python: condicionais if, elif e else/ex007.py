primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))
media = (primeira_nota + segunda_nota + terceira_nota) / 3

if media >= 7:
    print('Aprovado')
elif 5 <= media and media < 7:
    print('Recuperação')
else:
    print('Reprovado')

print(f'Sua média foi: {media}')