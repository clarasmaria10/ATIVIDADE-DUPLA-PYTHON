import os
os.system('cls || clear')

vetor_numeros = []
NUMEROS = 10
maior = 0

for i in range(NUMEROS):
    numero = float(input(f'Digite o {i+1}º número: '))
    vetor_numeros.append(numero)

for i in range(NUMEROS):
    if 10 < vetor_numeros[i]:
        maior += 1

soma = sum(vetor_numeros)

print(f'A soma dos números é: {soma}')
print(f'Quantidade de números maiores que 10: {maior}')

print('Feito por: Maria Clara')
print('R.A.: 026.085188')