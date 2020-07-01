soma = cont = 0
while True:
    num = int(input(('Digite um valor... (ou 999 para parar): ')))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Você digitou \33[33m{cont}\33[m valores e a soma é \33[31m{soma}')
