# ===== CONJUNTOS (SETS) EM PYTHON =====

print("=" * 70)
print("CONJUNTOS (SETS) EM PYTHON")
print("=" * 70)

# ===== 1. O QUE SÃO CONJUNTOS? =====
print("\n1. O QUE SÃO CONJUNTOS?")
print("-" * 70)
print("Conjuntos são coleções de elementos ÚNICOS e SEM ORDEM")
print("Sintaxe: {elemento1, elemento2, ...}")
print("Características:")
print("  • Elementos únicos (sem duplicatas)")
print("  • Sem ordem definida")
print("  • Mutável (pode adicionar e remover)")
print("  • Muito eficiente para buscas")
print("  • Elementos devem ser imutáveis (não podem ser listas ou dicionários)\n")


# ===== 2. CRIANDO CONJUNTOS =====
print("2. CRIANDO CONJUNTOS")
print("-" * 70)

# Conjunto vazio (atenção: {} cria dicionário, não conjunto!)
conjunto_vazio = set()
print(f"Conjunto vazio: {conjunto_vazio}")
print(f"Tipo: {type(conjunto_vazio)}\n")

# Conjunto com elementos
conjunto_numeros = {1, 2, 3, 4, 5}
print(f"Conjunto de números: {conjunto_numeros}")
print(f"Tipo: {type(conjunto_numeros)}")

# Conjunto com strings
conjunto_frutas = {"maçã", "banana", "laranja", "uva"}
print(f"Conjunto de frutas: {conjunto_frutas}")

# Conjunto misto
conjunto_misto = {1, "texto", 3.14, True}
print(f"Conjunto misto: {conjunto_misto}")

# Conjuntos removem duplicatas automaticamente
conjunto_duplicatas = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(f"\nConjunto com duplicatas {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}:")
print(f"Resultado: {conjunto_duplicatas} (duplicatas removidas)")

# Converter lista para conjunto
lista = [1, 2, 2, 3, 3, 4, 5, 5]
conjunto_de_lista = set(lista)
print(f"\nLista: {lista}")
print(f"Convertida para conjunto: {conjunto_de_lista}")

# Converter string para conjunto
conjunto_de_string = set("PYTHON")
print(f"\nString: 'PYTHON'")
print(f"Convertida para conjunto: {conjunto_de_string}")

# Usar range
conjunto_de_range = set(range(1, 6))
print(f"\nrange(1, 6) convertido para conjunto: {conjunto_de_range}")


# ===== 3. ADICIONANDO ELEMENTOS =====
print("\n3. ADICIONANDO ELEMENTOS")
print("-" * 70)

conjunto = {1, 2, 3}
print(f"Conjunto inicial: {conjunto}")

# Adicionar um elemento com add()
conjunto.add(4)
print(f"Após add(4): {conjunto}")

conjunto.add(5)
print(f"Após add(5): {conjunto}")

# Tentar adicionar duplicata (não muda o conjunto)
conjunto.add(3)
print(f"Após add(3) (já existe): {conjunto}")

# Adicionar múltiplos elementos com update()
conjunto.update([6, 7, 8])
print(f"Após update([6, 7, 8]): {conjunto}")

# Update com string (cada caractere vira elemento)
conjunto_letras = {"a", "b"}
conjunto_letras.update("cde")
print(f"\nConjunto: {conjunto_letras}")
print(f"Após update('cde'): {conjunto_letras}")

# Update com outro conjunto
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
conjunto_a.update(conjunto_b)
print(f"\nConjunto A: {1, 2, 3}")
print(f"Conjunto B: {3, 4, 5}")
print(f"Após A.update(B): {conjunto_a}")


# ===== 4. REMOVENDO ELEMENTOS =====
print("\n4. REMOVENDO ELEMENTOS")
print("-" * 70)

# Método remove() - gera erro se não existe
conjunto = {1, 2, 3, 4, 5}
print(f"Conjunto inicial: {conjunto}")

conjunto.remove(3)
print(f"Após remove(3): {conjunto}")

print("\nTentando remover elemento que não existe:")
try:
    conjunto.remove(10)
except KeyError:
    print(f"Erro: 10 não está no conjunto")

# Método discard() - não gera erro se não existe
conjunto = {1, 2, 3, 4, 5}
print(f"\nConjunto: {conjunto}")

conjunto.discard(3)
print(f"Após discard(3): {conjunto}")

conjunto.discard(10)
print(f"Após discard(10) (não existe): {conjunto}")

# Método pop() - remove e retorna um elemento aleatório
conjunto = {1, 2, 3, 4, 5}
print(f"\nConjunto: {conjunto}")

elemento = conjunto.pop()
print(f"pop() removeu: {elemento}, conjunto agora: {conjunto}")

# Método clear() - remove todos os elementos
conjunto = {1, 2, 3, 4, 5}
print(f"\nConjunto: {conjunto}")

conjunto.clear()
print(f"Após clear(): {conjunto}")


# ===== 5. ACESSAR ELEMENTOS =====
print("\n5. ACESSAR ELEMENTOS")
print("-" * 70)

conjunto = {10, 20, 30, 40, 50}
print(f"Conjunto: {conjunto}")

# Verificar existência
print(f"\n20 in conjunto: {20 in conjunto}")
print(f"100 in conjunto: {100 in conjunto}")

print(f"\n100 not in conjunto: {100 not in conjunto}")
print(f"20 not in conjunto: {20 not in conjunto}")

# Tamanho
print(f"\nTamanho: {len(conjunto)}")

# Iterar sobre conjunto
print(f"\nIterando sobre o conjunto:")
for elemento in conjunto:
    print(f"  {elemento}")

# Não há índices em conjuntos
print("\nNota: Conjuntos não têm índices (sem ordem!)")
print("Não pode fazer conjunto[0]")


# ===== 6. OPERAÇÕES MATEMÁTICAS COM CONJUNTOS =====
print("\n6. OPERAÇÕES MATEMÁTICAS COM CONJUNTOS")
print("-" * 70)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"Conjunto A: {a}")
print(f"Conjunto B: {b}\n")

# UNIÃO: elementos de A E B
uniao = a | b
print(f"União (A | B): {uniao}")
uniao_metodo = a.union(b)
print(f"Union com método: {uniao_metodo}")

# INTERSECÇÃO: elementos que estão EM AMBOS
interseccao = a & b
print(f"\nInterseção (A & B): {interseccao}")
interseccao_metodo = a.intersection(b)
print(f"Intersection com método: {interseccao_metodo}")

# DIFERENÇA: elementos de A que NÃO estão em B
diferenca = a - b
print(f"\nDiferença (A - B): {diferenca}")
diferenca_metodo = a.difference(b)
print(f"Difference com método: {diferenca_metodo}")

# DIFERENÇA SIMÉTRICA: elementos que estão EM UM OU NO OUTRO, mas não em ambos
diff_simetrica = a ^ b
print(f"\nDiferença Simétrica (A ^ B): {diff_simetrica}")
diff_simetrica_metodo = a.symmetric_difference(b)
print(f"Symmetric difference com método: {diff_simetrica_metodo}")

# Exemplo visual
print("\n--- Exemplo Visual ---")
print(f"A: {a}")
print(f"B: {b}")
print(f"A ∪ B (União): {a | b}")
print(f"A ∩ B (Intersecção): {a & b}")
print(f"A - B (Diferença): {a - b}")
print(f"B - A (Diferença): {b - a}")
print(f"A Δ B (Diferença Simétrica): {a ^ b}")


# ===== 7. OPERAÇÕES DE COMPARAÇÃO =====
print("\n7. OPERAÇÕES DE COMPARAÇÃO")
print("-" * 70)

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {1, 2, 3}
d = {4, 5, 6}

print(f"A: {a}")
print(f"B: {b}")
print(f"C: {c}")
print(f"D: {d}\n")

# Igualdade
print(f"A == C: {a == c}")
print(f"A == B: {a == b}")

# Subconjunto (issubset)
print(f"\nA <= B (A é subconjunto de B): {a <= b}")
print(f"A <= C (A é subconjunto de C): {a <= c}")
print(f"B <= A (B é subconjunto de A): {b <= a}")

print(f"\nA.issubset(B): {a.issubset(b)}")
print(f"C.issubset(B): {c.issubset(b)}")

# Superconjunto (issuperset)
print(f"\nB >= A (B é superconjunto de A): {b >= a}")
print(f"C >= A (C é superconjunto de A): {c >= a}")

print(f"\nB.issuperset(A): {b.issuperset(a)}")
print(f"C.issuperset(A): {c.issuperset(a)}")

# Disjunto (isdisjoint)
print(f"\nA.isdisjoint(D) (A e D têm elementos em comum?): {a.isdisjoint(d)}")
print(f"A.isdisjoint(B) (A e B têm elementos em comum?): {a.isdisjoint(b)}")


# ===== 8. MODIFICAÇÕES DE CONJUNTOS =====
print("\n8. MODIFICAÇÕES DE CONJUNTOS")
print("-" * 70)

print("Operações que modificam o conjunto original:\n")

# intersection_update
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"A: {a}, B: {b}")
a.intersection_update(b)
print(f"Após A.intersection_update(B): {a}")

# difference_update
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"\nA: {a}, B: {b}")
a.difference_update(b)
print(f"Após A.difference_update(B): {a}")

# symmetric_difference_update
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"\nA: {a}, B: {b}")
a.symmetric_difference_update(b)
print(f"Após A.symmetric_difference_update(B): {a}")


# ===== 9. CÓPIA DE CONJUNTOS =====
print("\n9. CÓPIA DE CONJUNTOS")
print("-" * 70)

original = {1, 2, 3}
print(f"Original: {original}")

# Cópia com copy()
copia = original.copy()
copia.add(4)
print(f"Após copia.add(4):")
print(f"  Original: {original} (não modificada)")
print(f"  Cópia: {copia}")

# Referência vs Cópia
original = {1, 2, 3}
referencia = original
referencia.add(4)
print(f"\nApós referencia.add(4) (sem copy()):")
print(f"  Original: {original} (também foi modificada!)")


# ===== 10. FROZENSET (CONJUNTO IMUTÁVEL) =====
print("\n10. FROZENSET (CONJUNTO IMUTÁVEL)")
print("-" * 70)

# Frozenset não pode ser modificado
congelado = frozenset([1, 2, 3, 4])
print(f"Frozenset: {congelado}")
print(f"Tipo: {type(congelado)}")

# Tentar modificar gera erro
print("\nTentando adicionar elemento:")
try:
    congelado.add(5)
except AttributeError:
    print("Erro: frozenset não tem método add()")

# Frozenset pode ser usado como chave de dicionário
dicionario = {
    frozenset([1, 2]): "chave 1",
    frozenset([3, 4]): "chave 2"
}
print(f"\nDicionário com frozensets como chaves:")
print(f"  {dicionario}")

# Frozenset pode ser elemento de outro conjunto
conjunto_de_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"\nConjunto de frozensets: {conjunto_de_sets}")


# ===== 11. MÉTODOS ÚTEIS =====
print("\n11. MÉTODOS ÚTEIS")
print("-" * 70)

print("Resumo de métodos de Set:\n")

metodos = {
    "add(x)": "Adiciona x",
    "remove(x)": "Remove x (erro se não existe)",
    "discard(x)": "Remove x (sem erro)",
    "pop()": "Remove e retorna elemento aleatório",
    "clear()": "Remove todos",
    "copy()": "Cria cópia",
    "union(outro)": "União",
    "intersection(outro)": "Intersecção",
    "difference(outro)": "Diferença",
    "symmetric_difference(outro)": "Diferença simétrica",
    "issubset(outro)": "É subconjunto?",
    "issuperset(outro)": "É superconjunto?",
    "isdisjoint(outro)": "São disjuntos?"
}

for metodo, descricao in metodos.items():
    print(f"  {metodo:30} → {descricao}")


# ===== 12. EXERCÍCIO PRÁTICO 1 =====
print("\n12. EXERCÍCIO PRÁTICO 1: REMOVER DUPLICATAS")
print("-" * 70)

lista_com_duplicatas = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]
print(f"Lista com duplicatas: {lista_com_duplicatas}")

# Remover duplicatas convertendo para set e depois para lista
lista_sem_duplicatas = list(set(lista_com_duplicatas))
print(f"Após remover duplicatas: {lista_sem_duplicatas}")

# Para manter a ordem original, usar método diferente
lista_sem_duplicatas_ordem = []
visto = set()
for numero in lista_com_duplicatas:
    if numero not in visto:
        lista_sem_duplicatas_ordem.append(numero)
        visto.add(numero)
print(f"Mantendo ordem original: {lista_sem_duplicatas_ordem}")


# ===== 13. EXERCÍCIO PRÁTICO 2 =====
print("\n13. EXERCÍCIO PRÁTICO 2: ENCONTRAR NÚMEROS COMUNS")
print("-" * 70)

lista_a = [1, 2, 3, 4, 5, 6]
lista_b = [4, 5, 6, 7, 8, 9]
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")

conjunto_a = set(lista_a)
conjunto_b = set(lista_b)

comuns = conjunto_a & conjunto_b
print(f"Números comuns: {comuns}")

# Usando intersection
comuns_metodo = conjunto_a.intersection(conjunto_b)
print(f"Usando intersection(): {comuns_metodo}")


# ===== 14. EXERCÍCIO PRÁTICO 3 =====
print("\n14. EXERCÍCIO PRÁTICO 3: ANÁLISE DE DADOS")
print("-" * 70)

# Diferentes grupos de alunos
alunos_turma_a = {"João", "Maria", "Pedro", "Ana", "Lucas"}
alunos_turma_b = {"Maria", "Ana", "Felipe", "Beatriz"}
alunos_turma_c = {"Pedro", "Lucas", "Felipe", "Gabriel"}

print(f"Turma A: {alunos_turma_a}")
print(f"Turma B: {alunos_turma_b}")
print(f"Turma C: {alunos_turma_c}\n")

# Alunos em todas as turmas
em_todas = alunos_turma_a & alunos_turma_b & alunos_turma_c
print(f"Alunos em TODAS as turmas: {em_todas if em_todas else 'Nenhum'}")

# Alunos em pelo menos uma turma
em_alguma = alunos_turma_a | alunos_turma_b | alunos_turma_c
print(f"Alunos em ALGUMA turma: {em_alguma}")

# Alunos apenas em A
so_em_a = alunos_turma_a - alunos_turma_b - alunos_turma_c
print(f"Alunos APENAS em A: {so_em_a if so_em_a else 'Nenhum'}")

# Alunos em A e B, mas não em C
a_e_b_nao_c = (alunos_turma_a & alunos_turma_b) - alunos_turma_c
print(f"Alunos em A e B, mas NÃO em C: {a_e_b_nao_c if a_e_b_nao_c else 'Nenhum'}")


# ===== 15. QUANDO USAR CONJUNTOS =====
print("\n15. QUANDO USAR CONJUNTOS")
print("-" * 70)

print("\nUse CONJUNTO quando:")
print("  ✓ Precisa de elementos únicos (sem duplicatas)")
print("  ✓ Ordem não importa")
print("  ✓ Quer fazer operações matemáticas (união, intersecção, etc)")
print("  ✓ Quer verificar existência de elemento (muito rápido!)")
print("  ✓ Quer remover duplicatas de uma lista")

print("\nNÃO use CONJUNTO quando:")
print("  ✗ Ordem é importante")
print("  ✗ Precisa acessar elementos por índice")
print("  ✗ Precisa de duplicatas")
print("  ✗ Precisa de elementos mutáveis (listas, dicionários)")

print("\n" + "=" * 70)
