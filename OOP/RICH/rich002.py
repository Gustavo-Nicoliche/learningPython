from rich import print
from rich.panel import Panel

caixa = Panel('[red]Esse aqui é um painel de exemplo[/red]', title = "Mensagem", style = "blue")

print(caixa)

# buscado no terminal: python3 -m rich.emoji
texto = Panel(':vulcan_salute: [green]Hello World![/green] :vulcan_salute:', title = "Aula de PYthon", style = "yellow", width = 22)

print(texto)