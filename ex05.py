import os
os.system('cls')

vetor_notas = []
print("Digite as 5 notas da turma:")
for i in range(5):
    nota = float(input(f"Nota {i + 1}: "))
    vetor_notas.append(nota)

media = sum(vetor_notas) / len(vetor_notas)

acima_da_media = 0
for nota in vetor_notas:
    if nota > media:
        acima_da_media += 1

print("\n--- RESULTADOS ---")
print(f"Notas digitadas: {vetor_notas}")
print(f"Média da turma: {media:.2f}")
print(f"Quantidade de notas acima da média: {acima_da_media}")

print('\nFeito por: Camilla Bastos')
print('R.A.: 026.082364')