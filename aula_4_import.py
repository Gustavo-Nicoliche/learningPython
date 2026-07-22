### CHUTE O NÚMERO

# Escreva um programa que, ao iniciar, gere um valor aleatório de 1 a 10 e permita
# que o usuário chute n[umeros até acertar o valor gerado.

# O programa deve informar se o chute foi maior, menor ou igual ao valor aleatório
# gerado no início.

'''
Usando método 5Q:
1. Quais são os dados de entrada necessários?
- o sistema pede um número

2. O que devo fazer com estes dados?
verificar se equivale ao número gerado

3. Quais são as restrições deste problema?
- deve ser um número de 1 a 10

4. Qual é o resultado esperado?
- se acertar, printará " número exato!"
- se errar, deverá permitir tentar outra vez

5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
O sistema gera um número
Pede que o usuário tente acertar
verifica se o usuário acertou
    Se sim, informa o acerto
    Se não, permite tentar novamente.

'''
import random

numero = random.randint(1, 10)

tentativa = ''
while tentativa != numero:
    tentativa = int(input('Digite o seu palpite de 1 a 10.'))
    if tentativa != numero:
        print('Digite novamente.')
    else:
        print('Você acertou')
