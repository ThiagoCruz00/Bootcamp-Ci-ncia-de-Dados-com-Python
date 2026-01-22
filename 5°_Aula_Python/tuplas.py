# ===== TUPLAS EM PYTHON =====

print("=" * 70)
print("TUPLAS EM PYTHON")
print("=" * 70)

# ===== 1. O QUE SÃO TUPLAS? =====
print("\n1. O QUE SÃO TUPLAS?")
print("-" * 70)
print("Tuplas são sequências de elementos imutáveis (não podem ser modificadas)")
print("Sintaxe: (elemento1, elemento2, ...)")
print("Parecem listas, mas usam parênteses ( ) em vez de colchetes [ ]")
print("Uma vez criadas, não podem ser alteradas, adicionadas ou removidas.\n")


# ===== 2. CRIANDO TUPLAS =====
print("2. CRIANDO TUPLAS")
print("-" * 70)

# Tupla vazia
tupla_vazia = ()
print(f"Tupla vazia: {tupla_vazia}")
print(f"Tipo: {type(tupla_vazia)}")

# Tupla com um elemento (atenção: precisa de vírgula)
tupla_um = (1,)
print(f"\nTupla com um elemento: {tupla_um}")
print(f"Tipo: {type(tupla_um)}")

# Sem a vírgula seria apenas um número em parênteses
nao_tupla = (1)
print(f"\n(1) sem vírgula: {nao_tupla} - Tipo: {type(nao_tupla)}")

# Tupla com números
tupla_numeros = (1, 2, 3, 4, 5)
print(f"\nTupla de números: {tupla_numeros}")

# Tupla com strings
tupla_frutas = ("maçã", "banana", "laranja", "uva")
print(f"Tupla de frutas: {tupla_frutas}")

# Tupla mista
tupla_mista = (42, "Python", 3.14, True, None)
print(f"Tupla mista: {tupla_mista}")

# Tupla aninhada
tupla_aninhada = ((1, 2), (3, 4), (5, 6))
print(f"Tupla aninhada: {tupla_aninhada}")

# Tupla sem parênteses (Python entende como tupla se houver vírgula)
tupla_sem_parenteses = 10, 20, 30
print(f"Tupla sem parênteses: {tupla_sem_parenteses}")
print(f"Tipo: {type(tupla_sem_parenteses)}")

# Convertendo lista para tupla
lista = [1, 2, 3, 4, 5]
tupla_de_lista = tuple(lista)
print(f"\nLista convertida para tupla: {tupla_de_lista}")

# Convertendo string para tupla (cada caractere vira elemento)
tupla_de_string = tuple("ABC")
print(f"String 'ABC' convertida para tupla: {tupla_de_string}")

# Usando função tuple()
tupla_com_funcao = tuple(range(1, 6))
print(f"Tupla com range: {tupla_com_funcao}")


# ===== 3. ACESSANDO ELEMENTOS =====
print("\n3. ACESSANDO ELEMENTOS")
print("-" * 70)

numeros = (10, 20, 30, 40, 50, 60, 70)
print(f"Tupla: {numeros}")
print(f"Índices:  0,  1,  2,  3,  4,  5,  6")

# Índices positivos
print(f"\nÍndices positivos:")
print(f"numeros[0] = {numeros[0]}")
print(f"numeros[1] = {numeros[1]}")
print(f"numeros[6] = {numeros[6]}")

# Índices negativos
print(f"\nÍndices negativos:")
print(f"Índices:  -7, -6, -5, -4, -3, -2, -1")
print(f"numeros[-1] = {numeros[-1]} (último elemento)")
print(f"numeros[-2] = {numeros[-2]} (penúltimo)")
print(f"numeros[-7] = {numeros[-7]} (primeiro)")

# Tamanho
print(f"\nTamanho da tupla: {len(numeros)}")


# ===== 4. FATIAMENTO (SLICING) =====
print("\n4. FATIAMENTO (SLICING)")
print("-" * 70)

letras = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
print(f"Tupla: {letras}")

print(f"\nFatiamento [inicio:fim]:")
print(f"letras[0:3] = {letras[0:3]}")
print(f"letras[2:5] = {letras[2:5]}")
print(f"letras[1:6] = {letras[1:6]}")

print(f"\nFatiamento com omissão:")
print(f"letras[:3] = {letras[:3]}")
print(f"letras[3:] = {letras[3:]}")
print(f"letras[:] = {letras[:]}")

print(f"\nFatiamento com passo:")
print(f"letras[::2] = {letras[::2]} (cada 2)")
print(f"letras[1::2] = {letras[1::2]} (começa em 1, cada 2)")

print(f"\nFatiamento invertido:")
print(f"letras[::-1] = {letras[::-1]}")


# ===== 5. VERIFICAR EXISTÊNCIA =====
print("\n5. VERIFICAR EXISTÊNCIA")
print("-" * 70)

cores = ("vermelho", "azul", "verde", "amarelo")
print(f"Tupla: {cores}")

print(f"\nUsando operador 'in':")
print(f"'azul' in cores: {'azul' in cores}")
print(f"'preto' in cores: {'preto' in cores}")
print(f"'verde' in cores: {'verde' in cores}")

print(f"\nUsando operador 'not in':")
print(f"'laranja' not in cores: {'laranja' not in cores}")
print(f"'vermelho' not in cores: {'vermelho' not in cores}")


# ===== 6. MÉTODOS DE TUPLAS =====
print("\n6. MÉTODOS DE TUPLAS")
print("-" * 70)
print("Tuplas têm apenas 2 métodos (não podem modificar):\n")

# Método index()
tupla = (1, 2, 3, 2, 4, 2, 5)
print(f"Tupla: {tupla}")

indice = tupla.index(2)
print(f"index(2): {indice} (primeira ocorrência)")

indice = tupla.index(5)
print(f"index(5): {indice}")

# Tratamento de erro
try:
    tupla.index(10)
except ValueError:
    print(f"Erro: 10 não está na tupla")

# Método count()
contagem = tupla.count(2)
print(f"\ncount(2): {contagem} (aparece {contagem} vezes)")

contagem = tupla.count(1)
print(f"count(1): {contagem}")

contagem = tupla.count(10)
print(f"count(10): {contagem} (não existe)")


# ===== 7. DESEMPACOTAMENTO DE TUPLAS =====
print("\n7. DESEMPACOTAMENTO DE TUPLAS")
print("-" * 70)

# Desempacotamento simples
tupla = (10, 20, 30)
print(f"Tupla: {tupla}")

a, b, c = tupla
print(f"Após a, b, c = tupla:")
print(f"  a = {a}")
print(f"  b = {b}")
print(f"  c = {c}")

# Desempacotamento com variável "_" (ignora valor)
tupla = (1, 2, 3, 4, 5)
print(f"\nTupla: {tupla}")
a, _, c, _, e = tupla
print(f"a, _, c, _, e = tupla")
print(f"  a = {a}, c = {c}, e = {e}")

# Desempacotamento com "*"
tupla = (1, 2, 3, 4, 5, 6)
print(f"\nTupla: {tupla}")
primeiro, *meio, ultimo = tupla
print(f"primeiro, *meio, ultimo = tupla")
print(f"  primeiro = {primeiro}")
print(f"  meio = {meio}")
print(f"  ultimo = {ultimo}")

# Desempacotamento em loop
tuplas = [("João", 25), ("Maria", 30), ("Pedro", 22)]
print(f"\nTuplas de pessoas:")
for nome, idade in tuplas:
    print(f"  {nome}: {idade} anos")


# ===== 8. IMUTABILIDADE =====
print("\n8. IMUTABILIDADE - NÃO PODE MODIFICAR")
print("-" * 70)

tupla = (1, 2, 3, 4, 5)
print(f"Tupla original: {tupla}")

# Tentar modificar gera erro
print("\nTentando modificar tupla[0] = 100:")
try:
    tupla[0] = 100
except TypeError as e:
    print(f"Erro: {e}")

# Tentar adicionar gera erro
print("\nTentando usar append():")
try:
    tupla.append(6)
except AttributeError as e:
    print(f"Erro: tupla não tem método append()")

# Tentar remover gera erro
print("\nTentando usar remove():")
try:
    tupla.remove(1)
except AttributeError as e:
    print(f"Erro: tupla não tem método remove()")

print("\nMas se a tupla contiver lista, a lista pode ser modificada:")
tupla = (1, 2, [3, 4, 5])
print(f"Tupla: {tupla}")
tupla[2][0] = 999
print(f"Após tupla[2][0] = 999: {tupla}")
print("(O elemento lista dentro da tupla foi modificado!)")


# ===== 9. OPERAÇÕES COM TUPLAS =====
print("\n9. OPERAÇÕES COM TUPLAS")
print("-" * 70)

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print(f"Tupla 1: {tupla1}")
print(f"Tupla 2: {tupla2}")

# Concatenação
tupla3 = tupla1 + tupla2
print(f"\nConcatenação (tupla1 + tupla2): {tupla3}")

# Repetição
tupla4 = (0,) * 5
print(f"Repetição ((0,) * 5): {tupla4}")

# Comprimento
print(f"len(tupla1): {len(tupla1)}")

# Multiplicação de tupla com tupla2
tupla5 = tupla1 * 2
print(f"Repetição (tupla1 * 2): {tupla5}")


# ===== 10. TUPLAS vs LISTAS =====
print("\n10. TUPLAS vs LISTAS")
print("-" * 70)

print("\nLISTA:")
lista = [1, 2, 3]
print(f"  Lista: {lista}")
print(f"  Tipo: {type(lista)}")
print(f"  Mutável: Sim (pode modificar, adicionar, remover)")
print(f"  Sintaxe: [ ]")
print(f"  Uso: Quando dados podem mudar")

print("\nTUPLA:")
tupla = (1, 2, 3)
print(f"  Tupla: {tupla}")
print(f"  Tipo: {type(tupla)}")
print(f"  Mutável: Não (não pode modificar, adicionar, remover)")
print(f"  Sintaxe: ( )")
print(f"  Uso: Quando dados não devem mudar (segurança, performance)")

print("\nComparação de performance:")
print("  Tuplas são mais rápidas que listas")
print("  Tuplas usam menos memória")
print("  Tuplas podem ser usadas como chaves de dicionário (listas não podem)")


# ===== 11. TUPLAS COMO CHAVES DE DICIONÁRIO =====
print("\n11. TUPLAS COMO CHAVES DE DICIONÁRIO")
print("-" * 70)

# Dicionário com tuplas como chaves
coordenadas = {
    (0, 0): "origem",
    (1, 0): "eixo X",
    (0, 1): "eixo Y",
    (1, 1): "quadrante 1"
}
print("Dicionário com coordenadas (tuplas como chaves):")
for chave, valor in coordenadas.items():
    print(f"  {chave}: {valor}")

print(f"\ncoordenadas[(1, 1)]: {coordenadas[(1, 1)]}")

# Tentar usar lista como chave gera erro
print("\nTentando usar lista como chave de dicionário:")
try:
    dicionario = {[1, 2]: "valor"}
except TypeError as e:
    print(f"Erro: {e}")
print("(Listas não podem ser chaves porque são mutáveis)")


# ===== 12. FUNÇÕES COM TUPLAS =====
print("\n12. FUNÇÕES COM TUPLAS")
print("-" * 70)

print("\nFunção retornando múltiplos valores (tupla):")
def calcular(a, b):
    soma = a + b
    produto = a * b
    diferenca = a - b
    return soma, produto, diferenca

resultado = calcular(10, 3)
print(f"calcular(10, 3) retorna: {resultado}")

s, p, d = calcular(10, 3)
print(f"Desempacotando: soma={s}, produto={p}, diferença={d}")

print("\nFunção aceitando argumentos em tupla (unpacking):")
def apresentar(*dados):
    print(f"  Dados recebidos: {dados}")
    for i, dado in enumerate(dados):
        print(f"    Argumento {i}: {dado}")

apresentar("João", 25, "São Paulo")


# ===== 13. EXERCÍCIO PRÁTICO =====
print("\n13. EXERCÍCIO PRÁTICO")
print("-" * 70)

print("\nRegistro de alunos:")
alunos = (
    ("João", 25, "Engenharia"),
    ("Maria", 23, "Medicina"),
    ("Pedro", 24, "Direito"),
    ("Ana", 22, "Arquitetura")
)

print("Alunos cadastrados:")
for nome, idade, curso in alunos:
    print(f"  {nome}: {idade} anos - {curso}")

print(f"\nTotal de alunos: {len(alunos)}")
print(f"Primeiro aluno: {alunos[0][0]}")
print(f"Último aluno: {alunos[-1][0]}")

print("\nIdades dos alunos:")
idades = tuple(aluno[1] for aluno in alunos)
print(f"  {idades}")
print(f"  Idade mínima: {min(idades)}")
print(f"  Idade máxima: {max(idades)}")
print(f"  Idade média: {sum(idades) / len(idades):.1f}")


# ===== 14. QUANDO USAR TUPLAS =====
print("\n14. QUANDO USAR TUPLAS")
print("-" * 70)

print("\nUse TUPLA quando:")
print("  ✓ Dados não devem mudar (proteção contra modificação)")
print("  ✓ Precisa de chave em dicionário")
print("  ✓ Quer melhor performance (tuplas são mais rápidas)")
print("  ✓ Quer menos consumo de memória")
print("  ✓ Retornar múltiplos valores de função")
print("  ✓ Usar como elementos de um conjunto (set)")

print("\nUse LISTA quando:")
print("  ✓ Dados precisam mudar (adicionar, remover, modificar)")
print("  ✓ Precisa de métodos como append(), remove(), sort()")
print("  ✓ Quer mais flexibilidade")

print("\n" + "=" * 70)
