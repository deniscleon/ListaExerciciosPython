# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50


while True:
    i = 1
    while True:
        try:
            n = int(input('Escolha o numero inteiro para base da tabuada: '))
            break
        except:
            print('Valor incorreto!')

    while i < 11 :
        print(f'{n} x {i} = {n*i}')
        i += 1


