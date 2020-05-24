from time import sleep
print('-*' * 10)
print('Os fogos vão começar....')
t = int(input('Quantos segundos faltam? '))
print('-*' * 10)
print('Então... Conte comigo...')
for c in range(t, 0, -1):
    print(c, end=', ')
    sleep(1)
print('Começaram os fogos...')
for f in range(1, 10 +1):
    print(f, '🎇 ' * 35)
    sleep(0.3)
