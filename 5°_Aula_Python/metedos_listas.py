# ===== MÉTODOS DA CLASSE LIST EM PYTHON =====

print("=" * 70)
print("MÉTODOS DA CLASSE LIST")
print("=" * 70)

# ===== 1. MÉTODO append() =====
print("\n1. MÉTODO append()")
print("-" * 70)
print("Sintaxe: lista.append(elemento)")
print("Função: Adiciona um elemento no final da lista")
print("Retorna: None (modifica a lista original)\n")

lista = [1, 2, 3]
print(f"Lista inicial: {lista}")

lista.append(4)
print(f"Após append(4): {lista}")

lista.append(5)
print(f"Após append(5): {lista}")

# Adicionar diferentes tipos
lista.append("texto")
print(f"Após append('texto'): {lista}")

lista.append([10, 20])
print(f"Após append([10, 20]): {lista}")


# ===== 2. MÉTODO extend() =====
print("\n2. MÉTODO extend()")
print("-" * 70)
print("Sintaxe: lista.extend(iterável)")
print("Função: Adiciona todos os elementos de um iterável na lista")
print("Retorna: None (modifica a lista original)\n")

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

lista1.extend(lista2)
print(f"Após lista1.extend(lista2): {lista1}")

# Extend com string (cada caractere é um elemento)
lista1.extend("ABC")
print(f"Após lista1.extend('ABC'): {lista1}")

# Extend com tuple
lista1.extend((7, 8, 9))
print(f"Após lista1.extend((7, 8, 9)): {lista1}")


# ===== 3. MÉTODO insert() =====
print("\n3. MÉTODO insert()")
print("-" * 70)
print("Sintaxe: lista.insert(índice, elemento)")
print("Função: Insere um elemento em uma posição específica")
print("Retorna: None (modifica a lista original)\n")

lista = ['a', 'b', 'd', 'e']
print(f"Lista inicial: {lista}")

lista.insert(2, 'c')
print(f"Após insert(2, 'c'): {lista}")

lista.insert(0, 'Z')
print(f"Após insert(0, 'Z'): {lista}")

lista.insert(100, 'final')
print(f"Após insert(100, 'final'): {lista}")

lista.insert(-1, 'antes_do_final')
print(f"Após insert(-1, 'antes_do_final'): {lista}")


# ===== 4. MÉTODO remove() =====
print("\n4. MÉTODO remove()")
print("-" * 70)
print("Sintaxe: lista.remove(elemento)")
print("Função: Remove a primeira ocorrência de um elemento")
print("Retorna: None (modifica a lista original)")
print("Erro: Gera ValueError se elemento não existe\n")

lista = [1, 2, 3, 2, 4, 2, 5]
print(f"Lista inicial: {lista}")

lista.remove(2)
print(f"Após remove(2): {lista} (remove apenas a primeira ocorrência)")

lista.remove(5)
print(f"Após remove(5): {lista}")

# Remover com verificação
lista = ['maçã', 'banana', 'laranja', 'banana']
print(f"\nLista de frutas: {lista}")
if 'banana' in lista:
    lista.remove('banana')
print(f"Após remover 'banana': {lista}")

# Tratamento de erro
print("\nTentando remover elemento que não existe:")
try:
    lista.remove('abacaxi')
except ValueError as e:
    print(f"Erro: {e}")


# ===== 5. MÉTODO pop() =====
print("\n5. MÉTODO pop()")
print("-" * 70)
print("Sintaxe: lista.pop(índice)")
print("Função: Remove e retorna elemento em um índice (padrão: último)")
print("Retorna: O elemento removido")
print("Erro: Gera IndexError se lista vazia ou índice inválido\n")

lista = [10, 20, 30, 40, 50]
print(f"Lista inicial: {lista}")

elemento = lista.pop()
print(f"pop() removeu: {elemento}, lista agora: {lista}")

elemento = lista.pop(0)
print(f"pop(0) removeu: {elemento}, lista agora: {lista}")

elemento = lista.pop(1)
print(f"pop(1) removeu: {elemento}, lista agora: {lista}")

elemento = lista.pop(-1)
print(f"pop(-1) removeu: {elemento}, lista agora: {lista}")

# Usar pop em uma pilha (stack)
print("\nExemplo de Pilha (Stack):")
pilha = []
pilha.append('primeiro')
pilha.append('segundo')
pilha.append('terceiro')
print(f"Pilha: {pilha}")
print(f"Removido (pop): {pilha.pop()}")
print(f"Pilha após pop: {pilha}")


# ===== 6. MÉTODO clear() =====
print("\n6. MÉTODO clear()")
print("-" * 70)
print("Sintaxe: lista.clear()")
print("Função: Remove todos os elementos da lista")
print("Retorna: None (modifica a lista original)\n")

lista = [1, 2, 3, 4, 5]
print(f"Lista inicial: {lista}")

lista.clear()
print(f"Após clear(): {lista}")

# Verificar se está vazia
print(f"Lista vazia? {len(lista) == 0}")


# ===== 7. MÉTODO index() =====
print("\n7. MÉTODO index()")
print("-" * 70)
print("Sintaxe: lista.index(elemento, início, fim)")
print("Função: Retorna o índice da primeira ocorrência")
print("Retorna: O índice (inteiro)")
print("Erro: Gera ValueError se elemento não existe\n")

lista = ['a', 'b', 'c', 'd', 'b', 'e']
print(f"Lista: {lista}")

indice = lista.index('b')
print(f"index('b'): {indice}")

indice = lista.index('d')
print(f"index('d'): {indice}")

# Buscar a partir de um índice
indice = lista.index('b', 2)
print(f"index('b', 2): {indice} (procura a partir do índice 2)")

# Buscar em um intervalo
indice = lista.index('b', 0, 5)
print(f"index('b', 0, 5): {indice} (procura entre índices 0 e 4)")

# Tratamento de erro
try:
    lista.index('z')
except ValueError:
    print("Erro: 'z' não encontrado na lista")


# ===== 8. MÉTODO count() =====
print("\n8. MÉTODO count()")
print("-" * 70)
print("Sintaxe: lista.count(elemento)")
print("Função: Conta quantas vezes um elemento aparece")
print("Retorna: O número de ocorrências (inteiro)\n")

lista = [1, 2, 2, 3, 2, 4, 2, 5]
print(f"Lista: {lista}")

contagem = lista.count(2)
print(f"count(2): {contagem}")

contagem = lista.count(1)
print(f"count(1): {contagem}")

contagem = lista.count(10)
print(f"count(10): {contagem} (elemento não existe)")

# Contar com strings
lista = ['maçã', 'banana', 'maçã', 'uva', 'maçã']
print(f"\nLista: {lista}")
print(f"count('maçã'): {lista.count('maçã')}")
print(f"count('banana'): {lista.count('banana')}")


# ===== 9. MÉTODO sort() =====
print("\n9. MÉTODO sort()")
print("-" * 70)
print("Sintaxe: lista.sort(reverse=False, key=None)")
print("Função: Ordena a lista (modifica original)")
print("Retorna: None\n")

# Ordenação básica
lista = [5, 2, 8, 1, 9, 3]
print(f"Lista original: {lista}")

lista.sort()
print(f"Após sort(): {lista}")

# Ordenação decrescente
lista = [5, 2, 8, 1, 9, 3]
lista.sort(reverse=True)
print(f"Após sort(reverse=True): {lista}")

# Ordenar strings
frutas = ['banana', 'maçã', 'uva', 'laranja']
print(f"\nFrutas: {frutas}")
frutas.sort()
print(f"Após sort(): {frutas}")

frutas.sort(reverse=True)
print(f"Após sort(reverse=True): {frutas}")

# Ordenar por critério customizado (por tamanho de string)
palavras = ['python', 'java', 'c', 'javascript', 'go']
print(f"\nPalavras: {palavras}")
palavras.sort(key=len)
print(f"Ordenado por tamanho: {palavras}")

# Ordenar lista de tuplas
pessoas = [('Maria', 30), ('João', 25), ('Pedro', 35)]
print(f"\nPessoas: {pessoas}")
pessoas.sort(key=lambda x: x[1])
print(f"Ordenado por idade: {pessoas}")


# ===== 10. MÉTODO reverse() =====
print("\n10. MÉTODO reverse()")
print("-" * 70)
print("Sintaxe: lista.reverse()")
print("Função: Inverte a ordem dos elementos")
print("Retorna: None (modifica a lista original)\n")

lista = [1, 2, 3, 4, 5]
print(f"Lista original: {lista}")

lista.reverse()
print(f"Após reverse(): {lista}")

# Reverter strings
nomes = ['Alice', 'Bob', 'Carol']
print(f"\nNomes: {nomes}")
nomes.reverse()
print(f"Após reverse(): {nomes}")

# Diferença entre reverse() e slicing [::-1]
lista = [1, 2, 3, 4, 5]
print(f"\nLista original: {lista}")
lista_invertida = lista[::-1]
print(f"Usando slicing [::-1]: {lista_invertida}")
print(f"Lista original (não modificada): {lista}")


# ===== 11. MÉTODO copy() =====
print("\n11. MÉTODO copy()")
print("-" * 70)
print("Sintaxe: lista.copy()")
print("Função: Cria uma cópia rasa (shallow copy) da lista")
print("Retorna: Uma nova lista com os mesmos elementos\n")

original = [1, 2, 3, 4, 5]
print(f"Lista original: {original}")

# Cópia
copia = original.copy()
print(f"Cópia: {copia}")

# Modificar cópia
copia[0] = 999
print(f"\nApós modificar cópia[0] = 999:")
print(f"Original: {original} (não modificada)")
print(f"Cópia: {copia}")

# Diferença entre = e copy()
print("\n--- Diferença entre = e copy() ---")
lista1 = [1, 2, 3]
lista2 = lista1  # Referência (não cópia)
lista3 = lista1.copy()  # Cópia

print(f"Lista1: {lista1}")
print(f"Lista2 (referência com =): {lista2}")
print(f"Lista3 (cópia com copy()): {lista3}")

lista1[0] = 999
print(f"\nApós lista1[0] = 999:")
print(f"Lista1: {lista1}")
print(f"Lista2: {lista2} (também mudou - é referência!)")
print(f"Lista3: {lista3} (não mudou - é cópia)")


# ===== 12. RESUMO E COMPARAÇÃO =====
print("\n12. RESUMO DE MÉTODOS")
print("-" * 70)

resumo = {
    'append()': 'Adiciona 1 elemento no final',
    'extend()': 'Adiciona múltiplos elementos',
    'insert()': 'Insere em posição específica',
    'remove()': 'Remove primeiro elemento de valor x',
    'pop()': 'Remove e retorna elemento',
    'clear()': 'Remove todos os elementos',
    'index()': 'Retorna índice do elemento',
    'count()': 'Conta ocorrências',
    'sort()': 'Ordena a lista',
    'reverse()': 'Inverte a ordem',
    'copy()': 'Cria cópia'
}

for metodo, descricao in resumo.items():
    print(f"{metodo:15} -> {descricao}")


# ===== 13. EXERCÍCIO PRÁTICO =====
print("\n13. EXERCÍCIO PRÁTICO")
print("-" * 70)

print("\nGerenciando lista de compras:")
lista_compras = []
print(f"Lista inicial: {lista_compras}")

# Adicionar itens
lista_compras.append("pão")
lista_compras.append("leite")
lista_compras.append("ovos")
print(f"Após adicionar 3 itens: {lista_compras}")

# Inserir item na posição específica
lista_compras.insert(1, "manteiga")
print(f"Após inserir 'manteiga' na posição 1: {lista_compras}")

# Adicionar vários itens
lista_compras.extend(["queijo", "sal", "açúcar"])
print(f"Após estender com 3 itens: {lista_compras}")

# Remover um item
lista_compras.remove("sal")
print(f"Após remover 'sal': {lista_compras}")

# Contar itens
print(f"Total de itens: {len(lista_compras)}")

# Ordenar
lista_compras.sort()
print(f"Lista ordenada: {lista_compras}")

# Contar ocorrência de um item
print(f"Quantidades de 'pão': {lista_compras.count('pão')}")

print("\n" + "=" * 70)
