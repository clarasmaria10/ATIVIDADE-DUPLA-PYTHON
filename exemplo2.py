import os
os.system('cls')

numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

print("\nOrdem original:")
for num in numeros:
    print(num, end=" ")

print("\n\nOrdem inversa:")
for num in reversed(numeros):
    print(num, end=" ")
print()

print('\nFeito por: Camilla Bastos')
print('R.A.: 026.082364')