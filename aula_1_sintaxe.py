# VARIÁVEIS

#inteiros 
idade = 15 #(int)
#float
nota = 7.5 #(float)
#string
frase = 'Hello World' #(str)
estudando = True #1(bool)

''' Escopo de variáveis
Quando se cria uma variável dentro de uma função, mesmo que ela tenha o mesmo nome
fora de uma função, e para ambas sejam atribuídos valores diferentes, ela pode ter
valores diferentes nos diferentes escopos:

def funcao(a, b)
    a = 10
    print(a)
    b = 5
    print(b)

a = 5
b = 10

-> nesse caso, "a" dentro da função vale 10, fora vale 5, e "b" dentro vale 5,
fora vale 10.
'''

# CONDICIONAIS - of elif else

trabalho_terminado = False
if trabalho_terminado == True:
    print('Parabéns, você terminou o trabalho!')
else:
    print('Você ainda não terminou o trabalho!')

estou_livre = input('Você está livre? (True/False) ')
if estou_livre == 'True':
    print('ok, você está livre!')
else:
    print('Você ainda não está livre!')

#lidando com mais que duas condições:

atrasos = int(input('Quantos atrasos você teve esse mês? '))
if atrasos >= 3:
    print('Você está suspenso!')
elif atrasos == 2: #usa-se elif para mais de duas condições
    print('Você está em alerta, mais uma falta e será suspenso!')
elif atrasos == 1:
    print('Você está em alerta, mais duas faltas e será suspenso!')
else: # finaliza-se sempre com else na última condição
    print('Você está em dia!')

# LAÇOS DE REPETIÇÃO - FOR

for item in range(3): #range nunca inclui o no último número, então nesse caso vai de 0 a 2
    print(item)

for item in range(1, 4): #nesse caso vai de 1 a 3
    print(item)

for item in range(1, 10, 2): #nesse caso vai de 1 a 9, pulando de 2 em 2
    print(item)



# LISTA DE NOMES

nomes = ['João', 'Maria', 'José', 'Ana']
for nome in nomes:
    print(nome)

dados = [12, 3.14, 'Hello', True]
for dado in dados:
    print(dado)

# LAÇOS DE REPETIÇÃO - WHILE

'''
Syntax:
while condição:
    bloco de código

Nesse caso, enquanto a condição for verdadeira, o bloco de código será executado. Quando a condição se tornar falsa, o laço será encerrado.

'''

tentativas = 0
while tentativas < 3:
    print('Tente novamente!')
    tentativas += 1 #incrementa o valor de tentativas em 1 a cada iteração do laço

senha = ''
while senha != '1234':
    senha = input('Digite a senha correta: ')
print('Bem-vindo ao sistema')

# contadores dentro do while

horario = 0 # contador de horas
while horario < 24:
    print(horario)
    horario = horario + 1
print('Fim do dia!')

#listas

precos = [20, 50, 100] #sendo 0, 1, 2
print(precos[2]) #nesse caso imprimirá o valor 100.

nomes = ['João', 'Maria', 'José', 'Ana']
print(nomes[0]) #imprime o primeiro elemento da lista.
print(nomes[-1]) #imprime o último elemento da lista.
print(nomes[1:3]) #imprime os elementos do índice 1 ao 2, ou seja, Maria e José.
print(nomes[:2]) #imprime os elementos do índice 0 ao 1, ou seja, João e Maria.
print(nomes.index('José')) #imprime o índice do elemento José, que é 2.

# Manipular - add novos itens

salarios = [2500, 500, 7000]
salario_usuario = float(input('Digite seu salário: '))
salarios.append(salario_usuario) #adiciona o salário digitado pelo usuário no final da lista de salários.
print(salarios)

# será impresso a lista de salários com o novo salario adicionado ao final da lista.



