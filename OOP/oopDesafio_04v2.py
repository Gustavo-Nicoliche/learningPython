''' ENUNCIADO
Crie a classe LIvro, que vai simular a passagem de páginas de um livro, considerando
também se o usuário chegou ao fim da leitura.
'''

from rich import print
from rich.panel import Panel
import time

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.paginaAtual = 1
        info = Panel(f':book: [blue] Você acabou de criar o livro [red]"{self.titulo}"[/], que tem [green]{self.paginas} páginas[/]. Você está na[/] [yellow]página 1[/]', width = 95)
        print(info)

    def fimDoLivro(self) -> bool:
        return True if self.paginaAtual == self.paginas else False

    def proximaPagina(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fimDoLivro():
                self.paginaAtual += 1
                print(f'Pág{self.paginaAtual}', end = ' ')
                time.sleep(0.2)
                cont += 1
        print(f'[blue]Você avançou {cont} páginas e está na[/] [yellow]página {self.paginaAtual}[/]')
        if self.fimDoLivro():
            print('[red]Você chegou ao final do livro[/]')


lilyBook = Livro('Livro da Lily', 120)
lilyBook.proximaPagina(5)
lilyBook.proximaPagina(200)