from random import randint
print('\033[33m-=' * 20)
print('\033[31mVAMOS JOGAR...')
print('\033[33m-=' * 20)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''\033[mSuas opções:
[0] \033[31mPEDRA\033[m
[1] \033[33mPAPEL\033[m
[2] \033[36mTESOURA\033[m''')
jogador = int(input('\033[mQual é a sua jogada? '))
from time import sleep
print('\033[31mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!\033[m')
print('\033[33m-=' * 20)
print('\033[mO Computador escolheu {}'.format(itens[computador]))
print('O Jogador ecolheu {}'.format(itens[jogador]))
print('\033[33m-=\033[m'* 20)
if computador == 0: # Computador escolheu PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 1: # Computador escolheu PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 2: # Computador escolheu TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada INVÁLIDA!')
