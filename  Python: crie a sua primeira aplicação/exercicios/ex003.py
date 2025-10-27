user = input('Digite um nome de usuario: ')
passwd = input('Digite uma senha de no mínimo 4 digitos: \n')

contagem = len(passwd)


if contagem < 4:
    print('Digite uma senha de no minimo 4 caracteres')
    
