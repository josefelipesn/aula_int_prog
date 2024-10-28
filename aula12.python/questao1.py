vet = []

for i in range(10):
    numero = int(input(f'Digite o número {i + 1}: '))
    vet.append(numero)

repetidos = {}

for i in range(len(vet)):
    if vet[i] in repetidos:
        repetidos[vet[i]].append(i)
    else:
        repetidos[vet[i]] = [i]

print("Números repetidos e suas posições:")
for numero, posicoes in repetidos.items():
    if len(posicoes) > 1:
        print(f'O número {numero} está repetido nas posições: {", ".join(map(str, posicoes))}')
