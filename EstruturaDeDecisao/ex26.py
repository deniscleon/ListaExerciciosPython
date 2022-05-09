#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o
# preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

valortotal = 0
alcool = 1.90
gasolina = 2.50
while True:

    while True:
        try:
            quantidade = int(input('Informe a quantidade de litros? '))
            break
        except:
            print('Valor incorreto!')

    while True:
        escolha = input('Infome o tipo de combustivel. 1 - Alcool, 2 - Gasolina? ')

        if escolha == '1':  # Alcool
            combustivel = 'Alcool'
            if quantidade <= 20:
                valortotal = (quantidade * alcool) - (quantidade * alcool * 3 / 100)
            else:
                valortotal = (quantidade * alcool) - (quantidade * alcool * 5 / 100)
            break

        if escolha == '2':  # Gasolina
            combustivel = 'Gasolina'
            if quantidade <= 20:
                valortotal = (quantidade * gasolina) - (quantidade * gasolina * 4 / 100)
            else:
                valortotal = (quantidade * gasolina) - (quantidade * gasolina * 6 / 100)
            break

        print('Valor inválido.')

    print(f'Valor total para {quantidade} litros de {combustivel} é R${valortotal}')