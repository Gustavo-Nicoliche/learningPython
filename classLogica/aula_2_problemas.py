# PROBLEMA 1 -
# Escreva um programa que retorna o valor hora de um funcionário
# com base no seu salário mensal e horas trabalhadas por mês.

''' Usando metodo 5Q:
1. Quais são os dados de entrada?
-  Salário mensal do funcionário (float);
-  Horas trabalhadas por mês (float);
2. O que devo fazer com esses dados?
-  Calcular o valor hora;
3. Quais são as restrições desses dados?
-  Precisa ter um valor do salário mensal;
-  Precisa ter um valor de horas trabalhadas por mês;
4. Qual é o resultado esperado?
-  Exibir o valor hora da pessoa, com base no cálculo de valor hora;
5. Qual é a sequência de passos para chegar ao resultado esperado?

receber o salário mensal 
receber quantidade de horas trabalhadas
valor hora = salário mensal / horas trabalhadas
exibir valor hora
'''

'''
salario = float(input('Qual é o seu salário mensal? '))
horas = float(input('Quantas horas você trabalha por mês? '))
valor_hora = salario / horas
print(valor_hora)
'''


##########################################

#PROBLEMA 2 -
# Crie um programa que recebe dois valores e exibe qual é o maior entre eles.

''' Usando método 5Q:

1. Quais sáo os dados de entrada?
- o primeiro valor
- o segundo valor
2. O que devo fazer com esses dados?
- COmparar qual é o maior entre eles
3. Quais são as restrições desses dados?
- Preciso de um primeiro valor
- Preciso de um segundo valor
4. Qual é o resultado esperado?
- Exibir qual é o maior valor entre os dois
5. Qual é a sequência de passos para chegar ao resultado esperado?

receber o primeiro valor
receber o segundo valor
comparar se o primeiro valor é maior que o segundo
    se sim, exibir o primeiro valor
    se não, exibir o segundo valor
'''


'''
primeiro_valor = float(input('Digite o primeiro valor: ')) 
segundo_valor = float(input('Digite o segundo valor: '))

if primeiro_valor > segundo_valor:
    print(f'o maior valor é: {primeiro_valor}')
else:
    print(f'o maior valor é: {segundo_valor}')
'''

###########################################

# PROBLEMA 3 -
# Crie um programa que recebe um valor inteiro e exibe se ele é positivo, negativo ou neutro.

''' Usando método 5Q:

1. Quais são os dados de entrada?
- Um valor inteiro

2. O que devo fazer com esses dados?
- Verificar se o valor é positivo, negativo ou neutro

3. Quais são as restrições desses dados?
- O valor deve ser um número inteiro

4. Qual é o resultado esperado?
- Exibir se o valor é positivo, negativo ou neutro

5. Qual é a sequência de passos para chegar ao resultado esperado?
receber o valor inteiro
comparar se o valor é maior que 0
    se sim, exibir que o valor é positivo
comparar se o valor é menor que 0
    se sim, exibir que o valor é negativo
se não, exibir que o valor é neutro
'''


'''
valor = int(input('digite um valor inteiro:'))
if valor > 0:
    print('O valor digitado é positivo.')
elif valor < 0:
    print('O valor digitado é negativo.')
else:
    print('O valor digitado é neutro.')
'''


###############################################

# PROBLEMA 4 -
# crie um programa que recebe cinco valores dentro de uma lista e imprime somente os valores que sejam pares

''' Usando método 5Q:
1. Quais são os dados de entrada?
- Uma lista de cinco valores inteiros
2. O que devo fazer com esses dados?
- Verificar quais valores da lista são pares
3. Quais são as restrições desses dados?
- A lista deve conter exatamente cinco valores inteiros
4. Qual é o resultado esperado?
- Exibir somente os valores pares da lista
5. Qual é a sequência de passos para chegar ao resultado esperado?
receber cinco valores inteiros e armazenar em uma lista
percorrer a lista e verificar se cada valor é par
    se o valor for par, exibir o valor
'''


'''
valores = [0] * 5 # criou uma lista com 5 posições definidas, todas com valor 0.
for valor in range(5):
    valores[valor] = int(input(f'Digite o {valor + 1}º valor: '))

print('Valores pares digitados:')

for valor in valores:
    if valor % 2 == 0:
        print(valor)
'''


###############################################

# PROBLEMA 5 -
# Crie um problema que verifica se todas as senhas digitadas por usuários são válidas.
# As senhas precisam ter no mínimo 8 caracteres, uma letra maiúscula e um número.

''' Usando método 5Q:

1. Quais são os dados de entrada?
- Senhas digitadas pelos usuários
2. O que devo fazer com esses dados?
- Verificar se as senhas são válidas de acordo com os critérios estabelecidos
3. Quais são as restrições desses dados?
- As senhas devem ter no mínimo 8 caracteres
- As senhas devem conter pelo menos uma letra maiúscula
- As senhas devem conter pelo menos um número
4. Qual é o resultado esperado?
- Exibir se cada senha digitada é válida ou inválida
5. Qual é a sequência de passos para chegar ao resultado esperado?

receber a senha digitada.
Verificar se a senha tem no mínimo 8 caracteres
Se a senha informada tiver no mínimo 8 caracteres, permitir acesso
Se a condição não for atendida, exibir que a senha é inválida 
'''


'''
senhas = [None] * 5 # lista para armazenar as senhas digitadas
for senha in range(5):
    senhas[senha] = input('Digite uma senha: ')

for senha in senhas:
    if len(senha) >= 8:
        print(f'A senha {senha} é válida.')
    else:
        print(f'A senha {senha} é inválida. Ela deve ter no mínimo 8 caracteres.')
'''

####################################################################

# PROBLEMA 6 -
# Crie um gerenciador de login simples, com o máximo de 3 tentativas.
# Teremos um único usuário(gustavo) e senha(12345) permitidos:
# Se errar as 3 tentativas o programa deve exibir " Aguarde 30 minutos para tentar novamente"
# Se o usuário acertar o login antes disso, exibir "Bem-vindo ao sistema"

''' Usando método 5Q:

1. Quais são os dados de entrada?
- Nome de usuário digitado
- Senha digitada
2. O que devo fazer com esses dados?
- Verificar se o nome de usuário e a senha correspondem aos valores permitidos
3. Quais são as restrições desses dados?
- O nome de usuário deve ser "gustavo"
- A senha deve ser "12345"
4. Qual é o resultado esperado?
- Exibir "Bem-vindo ao sistema" se o login for bem-sucedido
- Exibir "Aguarde 30 minutos para tentar novamente" se o usuário errar as 3 tentativas
5. Qual é a sequência de passos para chegar ao resultado esperado?

receber o nome do usuário
receber a senha
verificar se o nome e senha estão corretos
    se sim, exibir "Bem-vindo ao sistema"
    se não, permitir mais 2 tentativas
    se errar as 3 tentativas, exibir "Aguarde 30 minutos para tentar novamente"
'''


'''
usuario = ''
senha = ''
tentativas = 0

while (usuario != 'gustavo' or senha != '12345') and tentativas < 3:
    usuario = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')
    tentativas += 1

if usuario == 'gustavo' and senha == '12345':
    print('Bem-vindo ao sistema')
else:
    print('Aguarde 30 minutos para tentar novamente')
'''


########################################################

# PROBLEMA 7 -
# Crie um programa que, dada uma lista de salários, calcule o total pago a todos os funcionarios

''' Usando método 5Q:

1. Quais são os dados de entrada?
- Uma lista de salários
2. O que devo fazer com estes dados?
- Somar um com o outro até finalizar a lista de salários
3. Quais são as restrições do problema
- Precisamos de uma lista com no mínimo 2 salários
4. Qual é o resultado esperado?
- Exibir a soma de todos os salários
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?

Receber uma lista de salários
Somar cada valor da lista até obter o total
Exibir o total gasto com os pagamentos
'''

'''
salarios = [2500, 3350, 4200, 4000, 5000]
total_salarios = 0
for salario in salarios:
    total_salarios = total_salarios + salario

print(total_salarios)
'''