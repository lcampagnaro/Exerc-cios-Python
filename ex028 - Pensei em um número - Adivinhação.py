from random import randint
from time import sleep
computador= randint(0, 5) # Faz o computador "sortear" o número
print('-=-' * 25)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar qual...')
print('-=-' * 25)
jogador= int(input("Em qual número eu pensei? ")) # Onde o jogador tenta adinhar
print('PROCESSANDO...')
sleep(2)
if computador == jogador:
    print('PARABÉNS! Você acertou e me venceu')
else:
    print('GANHEI! Na verdade eu pensei no número {} e não no {}'.format(computador, jogador))
