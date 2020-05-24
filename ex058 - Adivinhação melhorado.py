from random import randint
from time import sleep
computador = randint(0, 10) # Faz o computador "sortear" o número
print('\33[33m-=-\33[m' * 25)
print('Olá sou o COMPUTADOR...')
print('Vou pensar em um número entre 0 e 10. Tente adivinhar qual...')
print('\33[33m-=-\33[m' * 25)
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))  # Onde o jogador tenta adinhar
    if jogador == computador:
        acertou = True
    else:
        print('Ainda não. Tente outra vez...')
print('\33[31mACERTOU!!!\33[m')
