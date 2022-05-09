#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

while True:
    while True:
        try:
            n = float(input('Informe um numero: '))
            break
        except:
            print('O valor deve ser um numero inteiro ou real.')

    if n == (round(n)):
        print('O valor digitado é inteiro')
    else:
        print('O valor digitado é decimal')
        