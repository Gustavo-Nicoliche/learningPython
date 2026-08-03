''' ENUNCIADO
Crie uma classe Churrasco, onde seja possível informar quantas pessoas vão participar
e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por
pessoa. Considere o consumo padrão: 400g por pessoa, e o preço 82,40/kg.
'''
from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class Churrasco:
    def __init__(self, titulo, numPessoas):
        self.titulo = titulo
        self.numPessoas = numPessoas

    def comprarCarne(self):
        quantCarne = (self.numPessoas * 400) / 1000 #mostra quantidade de carne total do churrasco
        kgCarne = 82.40
        contaFinal = kgCarne * quantCarne
        precoIndividual = contaFinal / self.numPessoas

        conteudo = f"Comprando carne para [green]{self.titulo}[/] com [yellow]{self.numPessoas}[/] convidados.\n"
        conteudo += f"Cada participante come em média 0.4kg de carne.\nA carne custa [red]R$82.40[/] o Kg.\n"
        conteudo += f"É necessário comprar [blue]{quantCarne}Kg[/] de carne.\n"
        conteudo += f"O custo total será de [green]R${contaFinal:.2f}[/].\n"
        conteudo += f"Cada pessoa pagará [yellow]R${precoIndividual}[/] para participar."

        painel = Panel(f"{conteudo}", width = 55, title = f"{self.titulo}")

        return painel    


        

churras = Churrasco('churras', 15)
print(churras.comprarCarne())
