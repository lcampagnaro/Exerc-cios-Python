from random import randint
from time import sleep
computador = randint(0, 10) # Faz o computador "sortear" o número
print('\33[33m-=-\33[m' * 25)
print('Olá sou o COMPUTADOR...')
print('Vou pensar em um número entre 0 e 10. Tente adivinhar qual...')
print('\33[33m-=-\33[m' * 25)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))  # Onde o jogador tenta adinhar
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            sleep(1)
            print('\33[31mÉ MAIS... \33[mTente outra vez: ')
        else:
            sleep(1)
            print('\33[31mÉ MENOR... \33[mTente mais uma vez: ')
print('\33[33m-=-\33[m' * 25)
print('\33[31mACERTOU!!!\33[m Com {} Tentativas...\33[m'.format(palpites))
print('\33[33m-=-\33[m' * 25)
