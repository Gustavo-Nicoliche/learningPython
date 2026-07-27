''' Explicação:

Quando se escreve um programa pode-se encontrar erros facilmente.
Se digitar: "primt('oi')"
O erro é de digitação, de sintaxe. Se o método não for escrito corretamente
ele não funciona.
Mas se ao inves de uma string for uma variável, como em:

"print(x)"

O erro será de significado, de semântica. Pois para que o programa imprima o valor
de uma variável, ela deve ter um valor, e não somente ter sido definida.
Se rodar o programa, o terminal dirá:

"NameError: name 'x' is not defined"

E isso é chamado de EXCEPTION. Ou exceção.
O Programa foi escrito corretamente em questões de sintaxe, mas semanticamente há
uma falha que o código não aponta na tela.

# Outro exemplo:

"n = int(input('numero: ')) <- se digitar um número 8
print(n)"                   <- ele imprime o número 8

Mas se o usuário digitar "oito" ou "um", que é um valor do tipo 'string', o programa
apontará:

"ValueError: invalid litaral for int() with base 10: 'oito'"

O programa esperava um valor INT e não um valor STRING.

# Outro exemplo:

a = int(input('digite um numero: ')) <- pede-se um número para dividir
b = int(input('digite um numero: ')) <- pede-se um divisor
r = a / b                            <- atribui-se os valores na conta
print(f'o resultado é: {r})          <- imprime o resultado.

Se na linha que pede o valor de "b" o usuário entrar com um número 0, o programa
apontará:

"ZeroDivisionError: division by zero"

Pois na matemática não se divide por zero.
'''

# O TRATAMENTO DE EXCEÇÕES:

''' Estrutura:

Try:
    #comandos que podem apresentar problemas.
except:
    #falha

'''

# EXEMPLO:

try:
    a = int(input('digite um numero: '))
    b = int(input('digite um numero: '))
    r = a / b
except:
    print('Tivemos um problema. Você não pode dividir nada por zero!')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre!')

'''Explicação

Nesse naso acima, ao incluir "except:" o erro que o python acusaria no terminal
é escrito pelo desenvolvedor e substuído pelo mesmo. O erro foi tratado de forma
generalizada, mas é possível tratar cada tipo de erro particularmente, incluindo
a EXCEPTION e tratando cada exception individualmente, usando quandos EXCEPTs
forem necessários.

Também é possível mostrar qual foi o erro apontado pelo python ao usar Exception
ao lado de except, seguido de "as erro". Então cita-se a classe, a causa, o atributo, etc.

'''

try:
    a = int(input('digite um numero: '))
    b = int(input('digite um numero: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados digitados.')
except ZeroDivisionError:
    print('Não é possível dividir por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}.')
else:
    print(f'O resultado é {r}')
finally:
    print('Programa encerrado. Muito obrigado!')