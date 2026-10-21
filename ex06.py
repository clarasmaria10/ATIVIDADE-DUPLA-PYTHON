import os
os.system('cls || clear')

vetor_A = []
vetor_B = []
QUANTIDADE = 5

for i in range(QUANTIDADE):
    numero = float(input(f'Digite o {i+1}º número para o vetor A: '))
    vetor_A.append(numero)

os.system('cls || clear')

for i in range(QUANTIDADE):
    numero = float(input(f'Digite o {i+1}º número para o vetor B: '))
    vetor_B.append(numero)

vetor_C = []
for i in range(QUANTIDADE):
    vetor_C.append(vetor_A[i] + vetor_B[i])

print('Vetor A:', end=' ')
for item in vetor_A:
    print(item, end=' ')
print()
print('Vetor B:', end=' ')
for item in vetor_B:
    print(item, end=' ')
print()
print('Vetor C (soma dos elementos correspondentes):', end=' ')
for item in vetor_C:
    print(item, end=' ')
print()

print('Feito por: Maria Clara')
print('R.A.: 026.085188')