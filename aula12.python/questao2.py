import random

# Criação da matriz A
A = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

# Soma de todos os valores da matriz A
soma = sum(sum(linha) for linha in A)
print("Soma de todos os valores da matriz A:", soma)

# Criação da matriz B
B = [[valor * 3 for valor in linha] for linha in A]

# Imprimindo a matriz B (opcional)
print("Matriz B:")
for linha in B:
    print(linha)
