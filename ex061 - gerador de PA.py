print('-='*30)
print('GERADOR DE PROGRESSÃO ARITIMÉTICA - 10 TERMOS - P.A.')
print('-='*30)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Qual a razão da P.A.? '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='') # alt+26 para fazer a setinha
    termo = termo + razão
    cont += 1
print('FIM')
