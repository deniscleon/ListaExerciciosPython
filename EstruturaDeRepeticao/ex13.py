
# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

while True:
    i = 1
    valor = 0
    base = int(input('Informe o numero base? '))
    expoente = int(input('Informe o numero expoente? '))
    valor = base
    while i != expoente:
        valor = valor * base
        i += 1
    print(valor)