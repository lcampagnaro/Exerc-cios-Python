n1 = int(input('Digite um número: '))
n2 = int(input("Digite outro número: "))
op = 0
while op != 6:
    print('''    \33[33m[1]\33[m Somar
    \33[33m[2]\33[m Subtrair
    \33[33m[3]\33[m Divisão
    \33[33m[4]\33[m Multiplicação
    \33[33m[5]\33[m Novos números
    \33[31m[6] Sair\33[m''')
    op = int(input('\33[31m>>>>> Qual é a sua opção?\33[m '))
    if op == 1:
        soma = n1 + n2
        print('A soma vale {}.'.format(soma))
    elif op == 2:
        subt = n1 - n2
        print('{} - {} é igual à {}.'.format(n1, n2, subt))
    elif op == 3:
        div = n1 / n2
        print('A divisão entre {} e {}, vale {}'.format(n1, n2, div))
    elif op == 4:
        mult = n1 * n2
        print('A multiplação vale {}'.format(mult))
    elif op == 5:
        print('Informe os valores novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('Opção inválida. Tente novamente.')
    print('\33[36m-=-=-\33[m' * 5)
print('Fim do programa... Volte sempre!!!')
