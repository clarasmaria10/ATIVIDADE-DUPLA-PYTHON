import os
os.system('cls || clear')

vetor_numeros = []
QUANTIDADE = 6

for i in range(QUANTIDADE):
    numero = int(input(f'Digite o {i+1}º número: '))
    vetor_numeros.append(numero)

print('\nVetor original:', *vetor_numeros)

for i in range(QUANTIDADE):
    if vetor_numeros[i] % 2 == 0:
        vetor_numeros[i] = 0
    else:
        vetor_numeros[i] = 1

print('Vetor modificado:', *vetor_numeros)

print('\nFeito por: Camilla Bastos')
print('R.A.: 026.082364')