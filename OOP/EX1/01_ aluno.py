# Declaração de classe

class Aluno:
    def __init__(self): # método construtor
        #Atributos de instância
        self.nome = ""
        self.idade = 0

    # métodos de instância
    def aniversário(self):
        self.idade = self.idade + 1
        # ou self.idade += 1

    def mensagem(self):
        return f'{self.nome} é um(a) Aluno(a) e tem {self.idade} anos de idade.'


# Declaração de objetos

a1 = Aluno()    # a1 é o Objeto
                # Aluno é a classe
                # () é a chamada do método construtor

a1.nome = 'Gustavo'  # a1 substitui o parâmetro self na instancia do atributo
a1.idade = 25
print(a1.mensagem())

a2 = Aluno()
a2.nome = 'Lily'
a2.idade = 21
print(a2.mensagem())

a3 = Aluno()
print(a3.mensagem())    # nesse caso printará nome vazio e idade zero, conforme
                        # definido nas linhas 6 e 7 deste arquivo.
                        # caso não for definido como ocorreu em a1 e a2

