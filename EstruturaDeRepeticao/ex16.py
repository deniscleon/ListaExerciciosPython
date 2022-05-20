#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.


base = 0
i = 2
lfibonacci = [1]

print(lfibonacci)
lfibonacci.append(1)
print(lfibonacci)

while True:
    if (lfibonacci[i-2] + lfibonacci[i-1]) < 500:
        base = (lfibonacci[i - 2] + lfibonacci[i - 1])
        lfibonacci.append(base)
        print(lfibonacci)
        i += 1
    else:
        break