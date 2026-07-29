# Declaração de classe  -> melhorado

class Aluno:
    """ docstring
    Essa classe cria um Aluno, que é uma pessoa que tem nome e idade.
    Para criar um novo aluno use:

    variável = Aluno(nome, idade)
    """

    def __init__(self, n = 'vazio', i = 0): # método construtor
        #Atributos de instância
        self.nome = n
        self.idade = i

    # métodos de instância
    def aniversario(self):
        self.idade = self.idade + 1
        print(f'Agora {self.nome} tem {self.idade} anos de idade!')
        # ou self.idade += 1

    ''' substituido pela __str__
    def mensagem(self):
        return f'{self.nome} é um(a) Aluno(a) e tem {self.idade} anos de idade.'
    '''

    def __str__(self):  #Dunder Method que originalmente mostra o endereço na memória
        return f'{self.nome} é um(a) Aluno(a) e tem {self.idade} anos de idade.'

    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}.'


# Declaração de objetos
print('')
print('')
a1 = Aluno(n='Gustavo', i=25)    
print(a1)

a2 = Aluno('Lily', 21) # Não é necessário citar a variável, apenas o valor atribuído.
print(a2)

a3 = Aluno()
print(a3)

print('-' * 20)
print(f'{a1.nome} e {a2.nome} fizeram aniversário.')
print('-' * 20)

a1.aniversario()
a2.aniversario()

print('')
print(a1.__dict__) # Dunder Attribute que traz os atributos em forma de dicionario
print(a1.__getstate__()) # Dunder Method com a mesma funcionalidade de __dict__
print(a1.__class__) # Dunder Attribute que mostra a classe do objeto

