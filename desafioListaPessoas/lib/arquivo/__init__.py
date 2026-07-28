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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
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
            print(f'{nome} foi adicionado!')
        a.close()