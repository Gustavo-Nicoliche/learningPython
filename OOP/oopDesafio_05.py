''' ENUNCIADO
Crie a classe Gamer, onde podemos cadastrar noome, nick e jogos favoritos de uma
pessoa. Crie também um étodo que permita mostrar a ficha desse gamer.
'''
from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick, jogosFavoritos = 'nenhum'):
        self.nome = nome
        self.nick = nick
        self.favoritos = jogosFavoritos

    def adicionarJogos(self):
        jogosFavoritos = []
        while True:
            jogo = input('Adicione um jogo favorito à sua lista, ou digite "sair": ')
            if jogo.lower() == "sair":
                break
            jogosFavoritos.append(jogo)
        self.favoritos = jogosFavoritos

    def exibirFicha(self):
        conteudo = f'[green]Player {self.nick}[/]\n'
        conteudo += ' \n'
        conteudo += '[blue]LISTA DE JOGOS FAVORITOS[/]\n'
        conteudo += f'\n'.join(self.favoritos)
        conteudo += ' \n'
        conteudo += '[blue]FIM DA LISTA[/]\n'
        conteudo += ' \n'
        conteudo += ':fireworks: Muito obrigado por jogar com a gente! :fireworks:'
        ficha = Panel(conteudo, width=80, style="yellow", title="FICHA DO JOGADOR")
        print(ficha)


# PROGRAMA
conteudoInicio = ':game_die: [green]Bem-vindo ao PLAY CENTER PYGAMES!!![/] :joystick:\n'
conteudoInicio += ' \n'
conteudoInicio += ':computer_disk: [blue]Vamos começar criando seu perfil.\n:computer_disk: No espaço abaixo informe seu [yellow]Nome[/] e seu [yellow]Nickname[/]:[/]\n'
inicio = Panel(conteudoInicio, width = 80, style = "blue", title="PYGAMES")
print(inicio)

nome = input('Nome: ')
nick = input('Nickname: ')
player1 = Gamer(nome, nick)

conteudoHome = f'[green] Seja bem-vindo, [yellow]{nome}[/]![/]\n'
conteudoHome += f'[blue] Seu nick para compartilhar com outros players é: [yellow]{nick}[/].[/]\n'
conteudoHome += f'[blue] Gostaria de adicionar jogos favoritos à sua lista? s/n [/]'
home = Panel(conteudoHome.center(90), width = 80, style = "blue", title="PYGAMES")
print(home)

resposta = input('Resposta s/n: ')
if resposta == "s":
    player1.adicionarJogos()

player1.exibirFicha()
