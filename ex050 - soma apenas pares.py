soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {} Valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou \33[33m{} \33[mnúmeros PARES e a soma  foi \33[33m{}.'.format(cont, soma))
