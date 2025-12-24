# Unpacking Operator (*)
# O operador de desempacotamento (*) em Python é usado para desempacotar iteráveis, como listas ou tuplas,
# em elementos individuais. Ele pode ser usado em várias situações, como na passagem de argumentos para
# funções, na criação de listas ou na impressão de valores.
# Exemplo de uso do operador de desempacotamento (*)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Sem *
print(n)        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Com *
print(*n)       # 1 2 3 4 5 6 7 8 9 0

# Em funções
def soma(a, b, c):
    return a + b + c

numeros = [1, 2, 3]
soma(*numeros)  # igual a soma(1, 2, 3)

# Em listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
completa = [*lista1, *lista2]  # [1, 2, 3, 4, 5, 6]

# Em dicionários
dict1 = {"a": 1}
dict2 = {"b": 2}
junto = {**dict1, **dict2}  # {"a": 1, "b": 2}