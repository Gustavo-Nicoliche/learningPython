### FATORIAL DE UM NÚMERO

# Criar um programa que receba um número e imprima o seu fatorial.

'''
Usando método 5Q:

1. Quais são os dados de entrada?
- um número inteiro
2. O que devo fazzer com esses dados?
- Calcular o fatorial do número
3. Quais são as restrições desses dados?
- O número deve ser inteiro e positivo
4. Qual é o resultado esperado?
- O fatorial do número digitado
5. QUal é a sequência de passos para chegar ao resultado esperado?
- receber o número inteiro e positivo
- Inicializar uma variavel fatorial com o valor 1
- Criar um laço de repetição que vai de 1 até o número digitado
- Multiplicar a variável fatorial pelo valor do contador do laço a cada iteração
- Exibir o valor da variável fatorial.

'''
numero = 0
while numero <= 0 and type(numero) != int:
    numero = int(input('Digite um número inteiro e positivo: '))

fatorial = 1
for fator in range(1, numero + 1):
    fatorial = fatorial * fator
print(f'O fatorial de {numero} é: {fatorial}')