peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Vocês está abaixo do peso.')
elif imc >18 and imc < 25:
    print('Você está com peso normal')
elif imc >= 25:
    print('Você está acima do peso.')