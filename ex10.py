import os
os.system('cls || clear')

QUANTIDADE = 5
vetor_idades = []
maioridade = 0

while True:
    for i in range(QUANTIDADE):
        idade = int(input(f'Digite a idade da {i+1}ª pessoa: '))
        if 0 <= idade <= 120:
            vetor_idades.append(idade)
            if idade >= 18:
                maioridade += 1
        else:
            print('Idade inválida. Digite uma idade entre 0 e 120.')
            break

    if len(vetor_idades) == QUANTIDADE:
        break

maior_idade = max(vetor_idades)
menor_idade = min(vetor_idades)

print(f'Maior idade: {maior_idade}')
print(f'Menor idade: {menor_idade}')
print(f'Número de pessoas com idade maior ou igual a 18 anos: {maioridade}')

print('\nFeito por: Maria Clara')
print('R.A.: 026.085188')