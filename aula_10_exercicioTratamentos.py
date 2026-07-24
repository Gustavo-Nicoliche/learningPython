# DESAFIO TRATAMENTO DE ERROS 1

''' Eunciado

Escreva a função leiaInt(), que vai funcionar de forma semelhante à função input()
do Python, so que fazendo a validação para aceitar apenas um valor numérico.
Ex: leiaInt('Digite um numero')

'''

def leiaInt(n):
    ok = False
    while ok == False:
        try:
            n = int(input('Digite um número: '))
        except (ValueError, TypeError):
            print('\033[0;31mVocê só pode digitar um número (ex: 1, 13, 56).\033m')
        else:
            print(f'Você digitou {n}')
            ok = True
        if ok:
            break
    print('Obrigado por usar o programa!')

leiaInt(n=None)