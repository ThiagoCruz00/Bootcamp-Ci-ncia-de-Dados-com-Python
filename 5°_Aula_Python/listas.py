# ===== EXEMPLOS DE LISTAS EM PYTHON =====

# 1. CRIANDO LISTAS
print("=== 1. CRIANDO LISTAS ===\n")

# Lista vazia
lista_vazia = []
print(f"Lista vazia: {lista_vazia}")

# Lista com números
numeros = [1, 2, 3, 4, 5]
print(f"Lista de números: {numeros}")

# Lista com strings
frutas = ["maçã", "banana", "laranja", "uva"]
print(f"Lista de frutas: {frutas}")

# Lista mista (diferentes tipos)
lista_mista = [1, "Python", 3.14, True, None]
print(f"Lista mista: {lista_mista}")

# Lista aninhada (lista dentro de lista)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matriz: {matriz}\n")


# 2. ACESSANDO ELEMENTOS
print("=== 2. ACESSANDO ELEMENTOS ===\n")

numeros = [10, 20, 30, 40, 50]
print(f"Lista: {numeros}")
print(f"Primeiro elemento (índice 0): {numeros[0]}")
print(f"Segundo elemento (índice 1): {numeros[1]}")
print(f"Último elemento (índice -1): {numeros[-1]}")
print(f"Penúltimo elemento (índice -2): {numeros[-2]}\n")


# 3. FATIAMENTO (SLICING)
print("=== 3. FATIAMENTO (SLICING) ===\n")

frutas = ["maçã", "banana", "laranja", "uva", "morango"]
print(f"Lista completa: {frutas}")
print(f"Do índice 0 até 2: {frutas[0:3]}")
print(f"Do índice 1 até o final: {frutas[1:]}")
print(f"Do início até o índice 3: {frutas[:3]}")
print(f"Toda a lista: {frutas[:]}")
print(f"De trás para frente (invertida): {frutas[::-1]}\n")


# 4. MODIFICANDO LISTAS
print("=== 4. MODIFICANDO LISTAS ===\n")

numeros = [1, 2, 3, 4, 5]
print(f"Lista original: {numeros}")

# Alterando um elemento
numeros[0] = 100
print(f"Depois de trocar o primeiro elemento: {numeros}")

# Alterando um intervalo
numeros[1:3] = [20, 30]
print(f"Depois de trocar elementos no intervalo [1:3]: {numeros}\n")


# 5. ADICIONANDO ELEMENTOS
print("=== 5. ADICIONANDO ELEMENTOS ===\n")

lista = [1, 2, 3]
print(f"Lista original: {lista}")

# Adicionar no final (append)
lista.append(4)
print(f"Depois de append(4): {lista}")

# Inserir em uma posição específica (insert)
lista.insert(1, 1.5)
print(f"Depois de insert(1, 1.5): {lista}")

# Estender lista com múltiplos elementos (extend)
lista.extend([5, 6, 7])
print(f"Depois de extend([5, 6, 7]): {lista}\n")


# 6. REMOVENDO ELEMENTOS
print("=== 6. REMOVENDO ELEMENTOS ===\n")

lista = [1, 2, 3, 4, 5, 3]
print(f"Lista original: {lista}")

# Remover um valor específico (remove)
lista.remove(3)
print(f"Depois de remove(3): {lista}")

# Remover o último elemento (pop)
ultimo = lista.pop()
print(f"Removido: {ultimo}, Lista agora: {lista}")

# Remover em um índice específico (pop)
elemento = lista.pop(1)
print(f"Removido o índice 1: {elemento}, Lista agora: {lista}")

# Limpar toda a lista (clear)
lista_temp = [10, 20, 30]
lista_temp.clear()
print(f"Lista após clear(): {lista_temp}\n")


# 7. PROCURANDO E CONTANDO
print("=== 7. PROCURANDO E CONTANDO ===\n")

numeros = [1, 2, 3, 4, 5, 3, 2, 1]
print(f"Lista: {numeros}")

# Encontrar o índice de um elemento (index)
indice = numeros.index(3)
print(f"Índice do primeiro 3: {indice}")

# Contar quantas vezes um elemento aparece (count)
contagem = numeros.count(3)
print(f"Quantidade de 3s na lista: {contagem}")

# Verificar se um elemento está na lista (in)
print(f"O número 4 está na lista? {4 in numeros}")
print(f"O número 10 está na lista? {10 in numeros}\n")


# 8. ITERANDO SOBRE LISTAS
print("=== 8. ITERANDO SOBRE LISTAS ===\n")

frutas = ["maçã", "banana", "laranja"]
print(f"Lista: {frutas}\n")

# For simples
print("Iteração simples:")
for fruta in frutas:
    print(f"  - {fruta}")

# For com índice
print("\nIteração com índice:")
for i, fruta in enumerate(frutas):
    print(f"  {i}: {fruta}")

# For com range
print("\nUsando range:")
for i in range(len(frutas)):
    print(f"  {i}: {frutas[i]}\n")


# 9. OPERAÇÕES COM LISTAS
print("=== 9. OPERAÇÕES COM LISTAS ===\n")

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

# Concatenação
lista3 = lista1 + lista2
print(f"Concatenação (lista1 + lista2): {lista3}")

# Repetição
lista4 = [0] * 3
print(f"Repetição ([0] * 3): {lista4}")

# Comprimento
print(f"Comprimento da lista1: {len(lista1)}\n")


# 10. ORDENAÇÃO E REVERSÃO
print("=== 10. ORDENAÇÃO E REVERSÃO ===\n")

numeros = [5, 2, 8, 1, 9, 3]
print(f"Lista original: {numeros}")

# Ordenação (sort) - modifica a lista
numeros_copia = numeros.copy()
numeros_copia.sort()
print(f"Após sort(): {numeros_copia}")

# Ordenação decrescente
numeros_copia = numeros.copy()
numeros_copia.sort(reverse=True)
print(f"Após sort(reverse=True): {numeros_copia}")

# Ordenação com sorted() - retorna nova lista
nova_lista = sorted(numeros)
print(f"sorted(numeros): {nova_lista}")
print(f"Lista original (não modificada): {numeros}")

# Reversão (reverse) - modifica a lista
numeros_copia = numeros.copy()
numeros_copia.reverse()
print(f"Após reverse(): {numeros_copia}")

# Reversão com slicing
print(f"Com slicing [::-1]: {numeros[::-1]}\n")


# 11. CÓPIA DE LISTAS
print("=== 11. CÓPIA DE LISTAS ===\n")

original = [1, 2, 3]
print(f"Lista original: {original}")

# Cópia rasa (shallow copy)
copia = original.copy()
copia[0] = 100
print(f"Após modificar a cópia: Original={original}, Cópia={copia}")

# Referência (não é cópia)
referencia = original
referencia[0] = 999
print(f"Referência modificada: Original={original} (também foi modificada!)\n")


# 12. MÉTODOS ÚTEIS
print("=== 12. MÉTODOS ÚTEIS ===\n")

# Min e max
numeros = [5, 2, 8, 1, 9, 3]
print(f"Lista: {numeros}")
print(f"Valor mínimo: {min(numeros)}")
print(f"Valor máximo: {max(numeros)}")
print(f"Soma: {sum(numeros)}")

# any e all
lista_bool = [True, True, True]
lista_bool2 = [True, False, True]
print(f"\nLista 1: {lista_bool} - all: {all(lista_bool)}, any: {any(lista_bool)}")
print(f"Lista 2: {lista_bool2} - all: {all(lista_bool2)}, any: {any(lista_bool2)}\n")


# 13. COMPREENSÃO DE LISTA (List Comprehension)
print("=== 13. COMPREENSÃO DE LISTA ===\n")

# Quadrado dos números
numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros]
print(f"Números: {numeros}")
print(f"Quadrados: {quadrados}")

# Filtrando pares
pares = [x for x in numeros if x % 2 == 0]
print(f"Números pares: {pares}")

# Transformando strings
palavras = ["python", "lista", "código"]
maiusculas = [palavra.upper() for palavra in palavras]
print(f"Palavras originais: {palavras}")
print(f"Maiúsculas: {maiusculas}\n")


# 14. EXERCÍCIO PRÁTICO
print("=== 14. EXERCÍCIO PRÁTICO ===\n")

# Criar uma lista de notas e calcular média
notas = [8.5, 7.0, 9.5, 6.0, 8.0]
print(f"Notas: {notas}")
print(f"Média: {sum(notas) / len(notas):.2f}")
print(f"Nota mais alta: {max(notas)}")
print(f"Nota mais baixa: {min(notas)}")
print(f"Quantidade de notas: {len(notas)}")

# Notas aprovadas (>= 7)
aprovadas = [nota for nota in notas if nota >= 7]
print(f"Notas aprovadas (>= 7): {aprovadas}\n")
