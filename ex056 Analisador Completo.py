pessoas = int(input('Quantas pessoas tem no grupo? '))
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, (pessoas + 1)):
    print(' ----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M / F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 6
print('A média de idade do grupo é de \33[33m{:.2f} \33[manos.'.format(mediaidade))
print('O homem mais velho tem \33[31m{} \33[manos e se chama \33[33m{}.\33[m'.format(maioridadehomem, nomevelho))
print('Ao todo tem \33[31m{} \33[mmulher(es) com menos de 20 anos.'.format(totmulher20))
