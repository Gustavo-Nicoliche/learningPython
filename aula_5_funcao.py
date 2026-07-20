# CRIANDO FUNÇÕES

''' Conceito
Podemos definir uma função com comandos criados iniciando com "def":

def mostraLinha():
    print('----------------------------------')

Sempre que a função mostraLInha() for chamada, p programa apresentará o conteúdo
contido na função, sendo '--------------------------------------'

Uma forma mais fácil de colocar um caractere repetido é:
    print('-' * 30)

'''

def lin():
    print('-' * 5)

print('Olá Mundo')
lin()
print('Acima tem uma função')
lin()

''' Outro exemplo
Outro exemplo é atribuir parâmetros para a função, simplifiando ainda mais seu uso:

Vamos supor que se queira usar uma função para exibir um título, formatado com as
linhas em cima e em baixo:

"def titulo" criará a função e "(txt)" é o parâmetro exemplo.
Dentro da função coloca-se então as linhas e entre elas o parâmetro, pois o conteúdo
do parâmetro ainda será definido.
'''

def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

'''
E assim logo depois pode-se adicionar o conteúdo a ser exibido:
'''

titulo('   ESTUDANDO PYTHON    ')

titulo('    HELLO WORLD    ')

'''
Para facilitar a leitura na execução do programa, vamos criar uma linha com uma função
'''
def separar():
    print(' ')
    print('#' * 70)
    print(' ')


separar()
########################################################################
'''
Criando uma função para efetuar uma soma após receber parâmetros adequados
'''

def soma(a, b):
    s = a + b
    lin()
    print(s)
    lin()


soma(4, 6)
soma(1, 4)
soma(9, 90)

''' Boa prtática
É uma boa prática recolher a função, dessa forma mostra-se que ela está
ali, mas oculta-se seu conteúdo.
'''

separar()
########################################################################
 
# EMPACOTANDO VALORES

''' Empacotamento
Nesse exemplo, usa-se  "*" para fazer com que o programa possa receber
diversas quantidades distinhas de parâmetros, no caso de uma soma.
Independente de quantos números forem escritos, o programa concluirá a soma.

Observa-se que no exemplo abaixo serão usadas tuplas, e não listas.
'''

def contador(* num):
    for valor in num:
        print(f'{valor} ', end='') #END='' faz com que o print() não quebre linha
    print('Mostrados')


contador(2, 1, 4)
contador(3, 6)
contador(6, 79, 2, 12)


separar()
##########################################################################
'''
Agora usando listas, será criado um programa no qual todos os valores de uma lista
serão multiplicados por 2.

Para isso, define-se uma posição 0 para que a iteração seja feita do começo da lista,
e usa-se o "len()" para fazer com que a iteração pare no último espaço da lista.

'''

def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [7, 3, 6, 9, 0]
dobra(valores)
print(valores)


separar()
########################################################################

'''
SOMAR
'''
def somar(* numeros): # criou a função e nomeou o parâmetro
    resultado = 0     # iniciou a variável do resultado para ir recebendo as somas
    for numero in numeros:   # criou o FOR com o iterador NUMERO que rodará pelos parametros, independente de quantidade
        resultado += numero  # adiciona gradativamente cada item do parâmetro dado
    print(f' Somando os valores {valores},  temos {resultado}') # apresenta o resultado


somar(4, 5)
somar(6, 2, 7)
somar(5, 8, 50, 3)


separar()
# PARÂMETROS OPCIONAIS

def calcular(a, b, c):
    s = a + b + c
    print(f'A soma vale{s}')


calcular(2, 3, 5)

''' Explicação:

Na função acima, pede-se 3 parâmetros e entrega-se 3 parâmetros na execução.
Mas se passarmos um parâmetro a menos, não funcionará:

calcular(2, 3)

Para evitar esse erro, atribui-se um valor previamente ao parâmetro:

"def calcular(a, b, c=0)"

ou

"def calcular(a=0, b=0 ,c=0)
'''

separar()

# RETURN

''' RETURN

Para "concatenar a informação" em uma linha somente, se fizermos trÊs chamadas, por
exemplo, de uma função que efetue uma conta, precisamos usar o RETURN.

Ele faz o armazenamento, em outra variável, do valor atribuído à variável que recebe
o produto da multiplicação:

'''

def multiplique(a=0, b=0, c=0):
    p = a * b * c
    return p

produto1 = multiplique(5, 3, 2)
produto2 = multiplique(10, 4, 5)
produto3 = multiplique(1, 4, 6)

print(f' Os resiltados foram {produto1}, {produto2} e {produto3}')

''' Explicação:
Nesse caso, usar return para capturar o resultado de a*b*c e armazenar
em variáveis globais.
'''