''' ENUNCIADO
Crie uma classe  Caneta, que simula o funcionamento de uma caneta colorida,
podendo escrever frases na cor relativa.
'''
from rich import print
 
class Caneta:
    def __init__(self, cor, tampa = True):
        self.cor = cor
        self.tampa = tampa

    def destampar(self):
        self.tampa = False

    def escrever(self, letras):
        if self.tampa == True:
            print(f'[red]A caneta {self.cor} está tampada![/]')
        elif self.cor == "vermelha":
            print(f'[red]{letras}[/]')
        elif self.cor == "azul":
            print(f'[blue]{letras}[/]')
        elif self.cor == "verde":
            print(f'[green]{letras}[/]')
        elif self.cor == "amarela":
            print(f'[yellow]{letras}[/]')

        return 0

canetaAmarela = Caneta("amarela")
canetaVermelha = Caneta("vermelha")
canetaAmarela.destampar()
canetaVermelha.destampar()

canetaAmarela.escrever("Olá Python! Criamos uma caneta amarela!")
canetaVermelha.escrever("Digitando de caneta vermelha!")