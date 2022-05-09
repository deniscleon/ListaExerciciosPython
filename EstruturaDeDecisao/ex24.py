# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

while True:
    while True:  # Valor de n1
        try:
            n1 = float(input('Informe o primeiro numero: '))
            break
        except:
            print('Informe um numero inteiro ou real')

    while True:  # Valor de n2
        try:
            n2 = float(input('Informe o segundo numero: '))
            break
        except:
            print('Informe um numero inteiro ou real')

    while True:
        print('''
                 #######MENU DE OPERAÇÕES########
                 # 1 - SOMA N1 + N2             #
                 # 2 - SUBTRAÇÃO N1 - N2        #
                 # 3 - DIVISÃO N1 / N2          #
                 # 4 - MULTIPLICAÇÃO N1 * N2    #
                 # 5 - ESCOLHER NOVOS NUMEROS   #
                 ################################''')

        escolha = input('Informe a opção desejada: ')


        if escolha == '1':
            print(f'A soma de {n1} + {n2} = {n1+n2}')
            if (n1+n2) % 2 == 0:  # Verifica PAR ou IMPAR
                print('O resultado é PAR!')
            else:
                print('O resultado é IMPAR!')

            if (n1+n2) >= 0:  # Verifica POSITIVO ou NEGATIVO
                print('O resultado é POSITIVO!')
            else:
                print('O resultado é NEGATIVO!')

            if (n1+n2) == round(n1+n2):  # Verifica INTEIRO ou DECIMAL
                print('O resultado é INTEIRO!')
            else:
                print('O resultado é DECIMAL!')

        elif escolha == '2':
            print(f'A subtração de {n1} - {n2} = {n1-n2}')
            if (n1-n2) % 2 == 0:
                print('O resultado é PAR!')
            else:
                print('O resultado é IMPAR!')

            if (n1-n2) >= 0:  # Verifica POSITIVO ou NEGATIVO
                print('O resultado é POSITIVO!')
            else:
                print('O resultado é NEGATIVO!')

            if (n1+n2) == round(n1+n2):  # Verifica INTEIRO ou DECIMAL
                print('O resultado é INTEIRO!')
            else:
                print('O resultado é DECIMAL!')

        elif escolha == '3':
            print(f'A divisão de {n1} / {n2} = {n1/n2}')
            if (n1/n2) % 2 == 0:
                print('O resultado é PAR!')
            else:
                print('O resultado é IMPAR!')

            if (n1/n2) >= 0:  # Verifica POSITIVO ou NEGATIVO
                print('O resultado é POSITIVO!')
            else:
                print('O resultado é NEGATIVO!')

            if (n1+n2) == round(n1+n2):  # Verifica INTEIRO ou DECIMAL
                print('O resultado é INTEIRO!')
            else:
                print('O resultado é DECIMAL!')

        elif escolha == '4':
            print(f'A multiplicação de {n1} * {n2} = {n1*n2}')
            if (n1*n2) % 2 == 0:
                print('O resultado é PAR!')
            else:
                print('O resultado é IMPAR!')

            if (n1*n2) >= 0:  # Verifica POSITIVO ou NEGATIVO
                print('O resultado é POSITIVO!')
            else:
                print('O resultado é NEGATIVO!')

            if (n1+n2) == round(n1+n2):  # Verifica INTEIRO ou DECIMAL
                print('O resultado é INTEIRO!')
            else:
                print('O resultado é DECIMAL!')

        elif escolha == '5':
            break

        else:
            print('Valor invalido!')
