# EXERCÍCIO FUNÇÃO
def separar():
    print('#' * 80)

#EXERCICIO 1

''' Enunciado
Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento, em metros) e mostre a área do terreno
'''

''' USANDO MÉTODO 5Q:
1. Quais são as entradas de dados:
- largura, comprimento
2. O que devo fazer com esses dados:
- inserir na função que calcula a area
3. Quais são as restrições do programa:
- deve ser usada função
- resultado deve ser exibido em metros
4. Qual o resultado a ser exibido:
- A área do terreno.
5. Qual é o passo a passo:

Definir uma função que calcule a área do terreno
Definir o parâmetro
Pedir ao usuário a Largura (m)
Pedir ao usuário o Comprimento (m)
chamar a função área
Exibir o resultado.

'''

def area(l, c):
    a = l * c
    print(f'A área de um terreno que tem {l}m por {c}m tem {a}m².')


l = int(input('Digite a largura do terreno(m): '))
c = int(input('Digite o comprimento do terreno(m): '))

area(l, c)

separar()

# EXERCICIO 2

''' Enunciado
Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''

''' USANDO MÉTODO 5Q:
1. Quais são as entradas de dados:
- mensagem
2. O que devo fazer com esses dados:
- inserir na função que imprime uma linha de margem com tamanho adaptável
a cada mensagen
3. Quais são as restrições do programa:
- Cada margem deve ter 2 espaços para trás e 2 espaços para frente
4. Qual o resultado a ser exibido:
- A mensagem com margens de acordo com o tamanho da mensagem.
5. Qual é o passo a passo:

Definir uma função que receba o tamanho da mensagem o imprima uma linha
Definir o parâmetro
Pedir ao usuário a mensagem
chamar a função escreva()
Exibir o resultado.
'''

def escreva(msg1, msg2):
    tam1 = len(msg1)
    tam2 = len(msg2)
    print('-' * (tam1 + 4))
    print(f'  {msg1}  ')
    print('-' * (tam1 + 4))
    print(' ')
    print('-' * (tam2 + 4))
    print(f'  {msg2}  ')
    print('-' * (tam2 + 4))


msg1 = input('Digite uma mensagem: ')
msg2 = input('Digite outra mensagem diferente: ')

escreva(msg1, msg2)

separar()
########################################################################

# EXERCÍCIO 3

''' Enunciado
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo, e realize a contagem.

O programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1;
b) De 10 até 0, de 2 em 2;
c) Uma contagem personalizada.
'''

''' USANDO MÉTODO 5Q:
1. Quais são as entradas de dados:
- Número de início da contagem;
- Número de fim da contagem;
- O passo da contagem;

2. O que devo fazer com esses dados:
- inserir na função contador() que executará a contagem;

3. Quais são as restrições do programa?
- Deve fazer a contagem já definida e realizar a contagem conforme o pedido do usuário

4. Qual o resultado a ser exibido:
- As duas contagens anteriores e contagem que o usuário pedir;

5. Qual é o passo a passo:

Definir uma função que receba os parametros inicio, fim e passo
Pedir ao usuário o número de início, fim e o passo da contagem.
chamar a função contador()
Exibir o resultado.
'''

def line():
    print('-=' * 30)

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    if passo > 0:
        fim += 1
    else:
        fim -= 1

    line()
    print(f'Contagem de {inicio} a {fim} de {passo} em {passo} : ', end='')
    for numeral in range(inicio, fim, passo):
        print(numeral, end =' ')
    print(' ')
    
    
contador(1, 10, 1)
contador(10, 1, -2)
line()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

separar()
######################################################################

# EXERCÍCIO 4

''' Enunciado
Calcule o fatorial de um número com uma função fatorial() que tenha retorno
e imprima na tela no programa principal.
'''

''' Usando método 5Q:

1. Quais são as entradas de dados?
- numero

2. O que devo fazer com esses dados?
- inserir na função fatorial() que calcula o fatorial do numero recebido

3. Quais são as restrições?
- Deve-se usar return no fim da função


4. Qual deve ser o resultado?
- imrpimir o resultado do fatorial no programa principal

5. Qual é o passo a passo?
- criar a função fatorial()
- dar o parâmetro
- iniciar uma variável de iteração
- definir o laço FOR com método RANGE
- retornar o resultado em uma variável
imprimir no programa principal o resultado.
'''

def fatorial(num=1):
    f = 1
    for contador in range(num, 0, -1):
        f *= contador
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(3)
f2 = fatorial(2)
f3 = fatorial(1)

print(f'Os resultados são {f1}, {f2} e {f3}')