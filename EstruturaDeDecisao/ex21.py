#Faça um Programa para um caixa eletrônico.
#O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
# quatro notas de 10, uma nota de 5 e quatro notas de 1.


while True:
    parteinteira50 = 0
    parteinteira20 = 0
    parteinteira10 = 0
    parteinteira5 = 0
    parteinteira1 = 0

    valor = 0

    while valor < 10 or valor > 600:
        try:
            valor = int(input('Informe o valor que deseja retirar? O valor deve ser maior que 10 ou menor 600. R$:'))
        except:
            valor = int(input('O valor deve ser maior que 10 ou menor 600. R$:'))

    if valor >= 50:
        parteinteira50 = valor // 50
        resto = valor % 50
    else:
        resto = valor

    if resto >= 20:
        parteinteira20 = resto // 20
        resto = resto % 20

    if resto >= 10:
        parteinteira10 = resto // 10
        resto = resto % 10

    if resto >= 5:
        parteinteira5 = resto // 5
        resto = resto % 5

    if resto >= 1:
        parteinteira1 = resto // 1

    print(f'Notas 50 = {parteinteira50}')
    print(f'Notas 20 = {parteinteira20}')
    print(f'Notas 10 = {parteinteira10}')
    print(f'Notas 5 = {parteinteira5}')
    print(f'Notas 1 = {parteinteira1}')