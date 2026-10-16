import os
os.system('cls || clear')

vetor_temp = []
DIA_SEMANA = 7

print('== TEMPERATURA DA SEMANA ==')
for i in range(DIA_SEMANA):
    temp = float(input(f'Digite a {i+1}ª temperatura: '))
    vetor_temp.append(temp)

os.system('cls || clear')

# CALCULOS
media = sum(vetor_temp) / DIA_SEMANA
maior = max(vetor_temp)
menor = min(vetor_temp)

# RESULTADOS
print('== RESULTADOS ==')
print(f'Média da semana: {media:.2f}')
print(f'Maior temperatura: {maior:.2f}')
print(f'Menor temperatura: {menor:.2f}')


print('Feito por: Maria Clara')
print('R.A.: 026.085188')