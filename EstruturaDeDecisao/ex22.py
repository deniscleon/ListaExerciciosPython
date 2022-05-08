#Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

while True:
    while True:
        try:
            n = int(input('Favor digitar um valor inteiro: '))
            break
        except:
            print('Valor incorreto!')
    if n % 2 == 0:
        print('O valor é PAR!')
    else:
        print('O valor é IMPAR!')