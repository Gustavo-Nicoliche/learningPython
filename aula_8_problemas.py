def line():
    print("~" * 45)

def separar():
    print(' ')
    print(" -=- " * 10)
    print(' ')

# DESAFIO 01

''' Enunciado

Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
pessoa tem voto negado, opcional ou obrigatório nas eleições

'''

''' Usando método 5Q:
1. Quais são as entradas de dados?
- ano de nascimento

2. O que devo fazer com esses dados?
- calcular idade
- verificar se o voto é obrigatorio, opcional ou negado

3. Quais são as restrições?
- deve se usar método return

4. Qual será o resultado?
- após o cálculo, o programa principal deverá apenas chamar a função
que dará o resultado

5. Qual é o passo a passo?
- Criar função voto()
- Definir parâmetro anoNasc
- Definir variavel idade
- Calcular idade comparando ao ano atual
- iniciar variavel voto
- Usar condicional IF para definir se o voto receberá negado, opcional ou obrigatório
- retornar voto

'''

def voto(anoNasc):
    idade = 2026 - anoNasc
    
    if idade < 18:
        voto = "negado"
    elif idade < 60:
        voto = "obrigatório"
    else:
        voto = "opcional"
    return voto

anoNasc = 2027
line()
while anoNasc > 2026: 
    anoNasc = int(input('Digite seu ano de nascimento: '))
line()
print(f'Nas eleições de 2026, seu voto é {voto(anoNasc)}')
line()

separar()

# DESAFIO 02

''' Enunciado

Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular
o segundo chamado show, que será um valor lógico(opcional) indicando se será
mostrado ou não na tela o processo de cálculo do fatorial.
'''

'''Usando método 5Q
1. Quais são os dados de entrada?
- número
- sim / não para lógica SHOW

2. O que devo fazer com esses dados?
- Calcular fatorial do número
- Mostrar ou não o cálculo conforme a resposta do usuário.

3. Quais são as restrições?
- Deve ser um número inteiro
- Deve-se usar método return
- O usuário precisa escolher se quer ou não ver o cálculo

4. Qual será o resultado?
- o resultado do fatorial, mostrando ou não o cálculo

5. Qual é o passo a passo?
- criar função fatorial()
- definir parâmetro numero e show
- criar variável que receberá o resultado do fatorial
- criar variável para iterar
- criar FOR com RANGE para calcular fatorial
- criar variável para opção mostrar ou não o cálculo
- criar IF para printar na tela conforme escolha do usuário.
- Programa principal:
- pedir número
- perguntar se quer ver o cálculo.

'''

def fatorial(numero, show):
    f = 1
    for contador in range(numero, 0, -1):
        if show == "sim":
            print(contador, end='')
            if contador > 1:
                print(' X ', end='')
            else:
                print(' = ', end ='')
        f *= contador
    return f
    


line()
numero = int(input('Digite um número para calcular fatorial: '))
show = input('Você deseja ver o cálculo? sim/nao: ')
print('Obrigado pela resposta!')
line()
print(f'{fatorial(numero, show)}')
line()


separar()

# DESAFIO 03

''' Enunciado

Faça um programa que tenha uma função chamada ficha(), que recena dois parâmetros
opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

''' Usando método 5Q:

1. Quais são os dados de entrada?
2. O que devo fazer com esses dados?
3. Quais são as restrições?
4. Qual será o resultado?
5. QUal é o passo a passo?
'''

def ficha(jogador, gols=0):
    print('   FICHA DO JOGADOR ')
    print('#------------------#')
    print('# JOGADOR:')
    print(f'# {jogador}')
    print('#')
    print('# MARCOU:')
    print(f'# {gols} gols')
    print('#------------------#')

informar = "sim"
while informar != "nao":
    jogador = input('Informe o nome do jogador: ')
    gols = int(input(f'Quantos gols {jogador} marcou?'))
    ficha(jogador, gols)
    informar = input('Deseja fazer uma nova ficha? sim/nao: ')

