#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
# cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
# e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

l_carnes = [('File Duplo', 4.90, 5.80), ('Alcatra', 5.90, 6.80), ('Picanha', 6.90, 7.80)]
l_escolhas = ['1','2','3']
l_pagamentos = ['Dinheiro', 'Cartão Tabajara', 'Cheque']
vl_desconto = 0
while True:
    print('''
#######MENU DE CARNES#########
#    1 - File Duplo          #
#    2 - Alcatra             #
#    3 - Picanha             #
##############################''')

    escolha_menu_carnes = input('Qual carne desejada? ')
    while escolha_menu_carnes not in l_escolhas:
        print('Escolha invalida')
        escolha_menu_carnes = input('Qual carne desejada? ')

    while True:
        try:
            quantidade = float(input('Quantos kilos? '))
            break
        except:
            print('Valor incorreto.')

    print('''
    #######MENU DE PAGAMENTO######
    #    1 - DINHEIRO            #
    #    2 - CARTÃO TABAJARA     #
    #    3 - CHEQUE              #
    ##############################''')

    escolha_menu_pagamento = input('Qual forma de pagamento desejada? ')
    while escolha_menu_pagamento not in l_escolhas:
        print('Escolha invalida')
        escolha_menu_pagamento = input('Qual forma de pagamento desejada? ')

    if quantidade <= 5:
        vl_carne = l_carnes[int(escolha_menu_carnes)-1][1] * quantidade
    elif quantidade > 5:
        vl_carne = l_carnes[int(escolha_menu_carnes)-1][2] * quantidade

    if escolha_menu_pagamento == '2':
        vl_desconto = vl_carne * 5 / 100

    print(f'''
    #########Cupom Fiscal ######################
    #Tipo de Carne:  {l_carnes[int(escolha_menu_carnes)-1][0]}
    ##                                        ##
    #Quantidade   :  {quantidade} KG 
    ##                                        ##
    #Forma de pagamento: {l_pagamentos[int(escolha_menu_pagamento)-1]}
    ##                                        ##
    #Valor do desconto: R${vl_desconto}
    ##                                        ##
    #Valor a pagar: R${vl_carne - vl_desconto}. 
    ############################################    ''')


