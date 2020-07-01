from time import sleep
while True:
    num = int(input('Quer ver a tabuada de qual número? '))
    print('Número negativo para FIM.')
    print('<>' * 15)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num*c}')
        sleep( 0.7)
    print('<>' * 15)
print('\33[34m-*-*' * 10)
print('\33[31mPROGRAMA DE TABUADA ENCERRADO. \33[33mObrigado por utilizar!')
