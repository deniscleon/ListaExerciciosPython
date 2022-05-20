# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a
# quantidade de números impares.

while True:
    print('Digite 10 numeros inteiros.')
    i = 1
    lista = []
    par = []
    impar = []
    qpar = 0
    qimpar = 0

    while i < 11:
        while True:
            try:
                n = int(input(f'Digite o {i}º numero: '))
                break
            except:
                print('Valor invalido.')

        lista.append(n)
        i += 1

    #print(lista)
    for item in lista:
        if item % 2 == 0:
            par.append(item)
            qpar += 1
        else:
            impar.append(item)
            qimpar += 1

    print(f'Foram digitados numeros {qpar} pares que são: {par}')
    print(f'Foram digitados numeros {qimpar} impares que são: {impar}')