frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('temos um Palindromo! ')
else:
    print('A frase não é palíndromo')
print('Você digitou a frase {}, e a frase oposta é {}.'.format(junto, inverso))
