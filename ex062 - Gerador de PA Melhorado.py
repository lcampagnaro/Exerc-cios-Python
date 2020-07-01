print('-='*30)
print('GERADOR DE PROGRESSÃO ARITIMÉTICA - 10 TERMOS - P.A.')
print('-='*30)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Qual a razão da P.A.? '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='') # alt+26 para fazer a setinha
        termo = termo + razão
        cont += 1
    print('PAUSA')
    mais = int(input("Quantos termos você quer mostrar à mais? "))
print("Fim do programa... com o total de {} termos mostrados!".format(total))
