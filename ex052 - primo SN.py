num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\33[1;32m', end='')
        tot += 1
    else:
        print('\33[0;31m', end='')
    print('{} '.format(c), end='')
print('\n\33[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print("Então ele \33[33mÉ SIM \33[mum número PRIMO.")
else:
    print('Nesse caso ele NÃO É um número PRIMO.')
