# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

while True:
    controle = 0
    resposta = ''
    while resposta != 's' or resposta != 'n':
        resposta = input('Telefonou para a vítima? s ou n? ').lower()
        if resposta == 's':
            controle += 1
            resposta = ''
            break
        elif resposta == 'n':
            resposta = ''
            break

    while resposta != 's' or resposta != 'n':
        resposta = input('Esteve no local do crime? s ou n ? ').lower()
        if resposta == 's':
            controle += 1
            resposta = ''
            break
        elif resposta == 'n':
            resposta = ''
            break

    while resposta != 's' or resposta != 'n':
        resposta = input('Mora perto da vítima? s ou n ? ').lower()
        if resposta == 's':
            controle += 1
            resposta = ''
            break
        elif resposta == 'n':
            resposta = ''
            break

    while resposta != 's' or resposta != 'n':
        resposta = input('Devia para a vítima? s ou n ? ').lower()
        if resposta == 's':
            controle += 1
            resposta = ''
            break
        elif resposta == 'n':
            resposta = ''
            break

    while resposta != 's' or resposta != 'n':
        resposta = input('Já trabalhou com a vítima? s ou n ? ').lower()
        if resposta == 's':
            controle += 1
            resposta = ''
            break
        elif resposta == 'n':
            resposta = ''
            break

    print(controle)

    if controle == 0 or controle == 1:
        print('Inocente!')

    if controle == 2:
        print('Suspeito')

    if controle == 3:
        print('Cumplice')

    if controle >= 4:
        print('Assassino')