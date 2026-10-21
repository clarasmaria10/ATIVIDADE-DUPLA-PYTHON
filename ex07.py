import os
os.system('cls')

vetor_original = []
print("Digite 10 números inteiros:")
for i in range(10):
    numero = int(input(f"Número {i + 1}: "))
    vetor_original.append(numero)

vetor_positivos = []
for numero in vetor_original:
    if numero > 0:
        vetor_positivos.append(numero)

print("\n--- RESULTADOS ---")
print(f"Vetor com os números positivos: {vetor_positivos}")
print(f"Quantidade de elementos copiados: {len(vetor_positivos)}")

print('\nFeito por: Camilla Bastos')
print('R.A.: 026.082364')