import os
os.system('cls || clear')

vetor_funcionarios = []
QUANTIDADE = 5
vetor_salarios = []
maior_2mil = 0

for i in range(QUANTIDADE):
    nome = input(f'Digite o nome do {i+1}º funcionário: ')
    salario = float(input(f'Digite o salário do {i+1}º funcionário: '))
    vetor_funcionarios.append(nome)
    vetor_salarios.append(salario)

for salario in vetor_salarios:
    if salario > 2000:
        maior_2mil += 1

maior_salario = max(vetor_salarios)
indice_maior = vetor_salarios.index(maior_salario)
nome_maior_salario = vetor_funcionarios[indice_maior]

print(f'\nNúmero de funcionários com salário acima de R$ 2.000,00: {maior_2mil}')
print(f'Maior salário: R$ {maior_salario:.2f}')
print(f'Funcionário com maior salário: {nome_maior_salario}')

print('\nFeito por: Maria Clara')
print('R.A.: 026.085188')