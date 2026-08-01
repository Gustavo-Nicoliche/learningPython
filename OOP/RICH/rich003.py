from rich import print
from rich.table import Table
from rich.panel import Panel

titulo = Panel('[blue]Bem-vindo ao mercadinho![/blue] :vulcan_salute:', width=40, style="yellow")

tabela = Table(title = 'TABELA DE PREÇOS')

tabela.add_column('Nome', justify='center', style="blue")
tabela.add_column('Preço', justify='center', style="green")
tabela.add_row('Lápis', 'R$1.00')
tabela.add_row('Borracha', 'R$0.75')

print(titulo)
print(tabela)