# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

while True:
    base = 0
    i = 2
    lfibonacci = [1, 1]
    n = int(input('Informe o numero termo de Fibonacci: '))

    if n == 1:
        print(lfibonacci[0])

    if n == 2:
        print(lfibonacci)

    if n >= 3:
        while i != n:
            base = lfibonacci[i-2] + lfibonacci[i-1]
            lfibonacci.append(base)
            i += 1

        print(lfibonacci)