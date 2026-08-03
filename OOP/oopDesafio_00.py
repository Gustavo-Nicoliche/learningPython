''' ENUNCIADO 
Crie uma classe Funcionario, onde podemos cadastrar nome, setor e cargo.
Crie também um método que permita ao funcionário se apresentar.
'''
from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        print(f':waving_hand: Olá! Meu nome é [blue]{self.nome}[/]! Atualmente trabalho no setor de {self.setor} como {self.cargo}.')


gustavo = Funcionario('Gustavo', 'TI', 'analista de dados')

print(gustavo.apresentar())