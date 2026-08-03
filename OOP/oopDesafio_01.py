''' ENUNCIADO
Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também um método
que mostra uma etiqueta de preço.
'''

from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

''' Como eu havia feito:
class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def verPreço(self):
        etiqueta = Panel(f'[blue]{self.nome}[/] :right_arrow: [green]R${self.preço}[/]', style='yellow', title='Mercado Assembly', width=30)
        print(etiqueta)
'''

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def verPreco(self):
        conteudo = f"[blue]{self.nome.center(30, ' ')}[/]"
        conteudo += f"{'-' * 30}"
        conteudo += f"[green]{self.preco.center(30, '.')}[/]"
        etiqueta = Panel(f'{conteudo}', style='yellow', title='Mercado Assembly', width=34)
        print(etiqueta)


banana = Produto('Banana', '2.50(kg)')
maca = Produto('Maçã', '3.00(kg)')

banana.verPreco()
maca.verPreco()
