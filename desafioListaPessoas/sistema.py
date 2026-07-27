from lib.interface import *
from lib.arquivo import * 
from time import sleep

arq = 'listaPessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:   
    resposta = menu(['Ver pessoas cadastradas', 'Cadastradar pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        header('NOVO  CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        header('Saindo do sistema... Até logo!')
        break
    else:
        print('Erro! Digite uma opção válida!')
    sleep(1)