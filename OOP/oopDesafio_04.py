''' ENUNCIADO
Crie a classe LIvro, que vai simular a passagem de páginas de um livro, considerando
também se o usuário chegou ao fim da leitura.
'''

class Livro:
    def __init__(self, titulo, numPaginas):
        self.titulo = titulo
        self.numPaginas = numPaginas

    def proxPagina(self):
        paginaAtual = 1
        print(f'Você está na página {paginaAtual}')
        while paginaAtual < self.numPaginas:
            comando = input('Para avançar a página digite "p". ')
            if comando == "p":
                paginaAtual += 1
                print(f'Página atual: {paginaAtual}')
        print('Você chegou ao fim do livro!')



l1 = Livro('Harry Potter', 10)
l1.proxPagina()

