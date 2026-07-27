from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # write text
        a.close()
    except:
        header('Houve um erro na criação do arquivo!')
    else:
        header(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        header('Erro ao ler o arquivo')
    else:
        header('LISTA DE PESSOAS ')
        print(a.read())
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        header('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            header('Houve um erro na escritura dos dados')
        else:
            header('Nome adicionado')
        a.close()