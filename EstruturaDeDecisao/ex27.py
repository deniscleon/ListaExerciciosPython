# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar
# R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo
# para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
# e escreva o valor a ser pago pelo cliente.

precokgmorango = 2.5
precokgmaca = 1.8
preco5kgmorango = 2.2
preco5kgmaca = 1.5

while True:

    while True:
        try:
            kgmorango = float(input('Informe KG morango? '))
            break
        except:
            print('Valor incorreto.')

    while True:
        try:
            kgmaca = float(input('Informe KG maça? '))
            break
        except:
            print('Valor incorreto.')

    if kgmorango < 5:
        vltotalmorango = kgmorango * precokgmorango

    if kgmaca < 5:
        vltotalmaca = kgmaca * precokgmaca

    if kgmorango >= 5:
        vltotalmorango = kgmorango * preco5kgmorango

    if kgmaca >= 5:
        vltotalmaca = kgmaca * preco5kgmaca

    vltotal = vltotalmorango + vltotalmaca
    kgtotal = kgmorango + kgmaca

    if vltotal > 25 or kgtotal > 8:
        vltotaldesc = vltotal - (vltotal* 0.1)
        vltotal = vltotaldesc


    print(f'''
##################################################################    
#                   Foram comprados:                             #   
#{kgmorango} KG - Morangos # Valor Total Morango = {vltotalmorango} #
#{kgmaca}    KG - Maças    # Valor Total Maças   = {vltotalmaca}    #
# Valor total das compras com descontos:         = {vltotal}        #
##################################################################''')