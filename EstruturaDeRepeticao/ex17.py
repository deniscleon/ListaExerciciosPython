# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

while True:
    n = int(input('Informe a base do fatoria: '))

    base = 1

    while n != 0:
        base = base * n
        n -= 1
    print(base)