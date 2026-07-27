# FUNÇÃO INTERNA help()

''' Para detectar funcionalidade do item:

Atribui-se o item como parâmetro:
help(print)

'''
help(print)

''' Resultado no terminal:

Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
        string inserted between values, default a space.
    end
        string appended after the last value, default a newline.
    file
        a file-like object (stream); defaults to the current sys.stdout.
    flush
        whether to forcibly flush the stream.

'''

''' Outra opção:

usar o "__doc__":
print(input.__doc__)

se fosse no método help:
help(input)

'''

''' DOCSTRINGS, para usar help() em funcoes criadas:

Ao criar uma função com def, se usar help() ele não dará explicações pois não é um método nativo.
Então usa-se, na linha abaixo da linha contendo DEF, a DOCSTRINGS, representada por 3 aspas duplas:

"""

"""
Ao utilizar Docstrings,  cita-se os parâmetros da função e explica ao usuário.
Deve ser feito manualmente
'''

def somar(a, b, c):
    """
    -> Faz uma contagem e mostra na tela.
    :param a: primeiro valor;
    :param b: segundo valor;
    :param c: terceiro valor.
    """

    s = a + b + c
    print(f'A soma vale{s}')


somar(2, 3, 5)

help(somar)