# ===== LISTAS: CRIAÇÃO E ACESSO AOS DADOS =====

print("=" * 60)
print("CRIAÇÃO E ACESSO A DADOS EM LISTAS")
print("=" * 60)

# ===== 1. DIFERENTES FORMAS DE CRIAR LISTAS =====
print("\n1. DIFERENTES FORMAS DE CRIAR LISTAS")
print("-" * 60)

# Forma 1: Com colchetes e elementos
lista_numeros = [1, 2, 3, 4, 5]
print(f"Lista de números: {lista_numeros}")

# Forma 2: Lista vazia
lista_vazia = []
print(f"Lista vazia: {lista_vazia}")

# Forma 3: Com função list()
lista_com_funcao = list(range(1, 6))
print(f"Lista com range: {lista_com_funcao}")

# Forma 4: Com diferentes tipos de dados
lista_mista = [42, "Python", 3.14, True, None]
print(f"Lista mista (int, str, float, bool, None): {lista_mista}")

# Forma 5: Lista de strings
lista_frutas = ["maçã", "banana", "laranja", "morango", "uva"]
print(f"Lista de frutas: {lista_frutas}")

# Forma 6: Lista aninhada (lista dentro de lista)
lista_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Lista aninhada: {lista_matriz}")

# Forma 7: Usando list comprehension
lista_quadrados = [x**2 for x in range(1, 6)]
print(f"Lista com compreensão: {lista_quadrados}")


# ===== 2. ACESSAR ELEMENTOS INDIVIDUAIS =====
print("\n2. ACESSAR ELEMENTOS INDIVIDUAIS")
print("-" * 60)

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"Lista: {numeros}")
print(f"Índices:  0,  1,  2,  3,  4,  5,  6,  7,  8")

# Acessar com índices positivos
print(f"\nÍndices POSITIVOS (começam do 0):")
print(f"numeros[0] = {numeros[0]} (primeiro elemento)")
print(f"numeros[1] = {numeros[1]} (segundo elemento)")
print(f"numeros[4] = {numeros[4]} (quinto elemento)")
print(f"numeros[8] = {numeros[8]} (último elemento)")

# Acessar com índices negativos
print(f"\nÍndices NEGATIVOS (começam do -1):")
print(f"Índices:  -9, -8, -7, -6, -5, -4, -3, -2, -1")
print(f"numeros[-1] = {numeros[-1]} (último elemento)")
print(f"numeros[-2] = {numeros[-2]} (penúltimo elemento)")
print(f"numeros[-3] = {numeros[-3]} (antepenúltimo elemento)")
print(f"numeros[-9] = {numeros[-9]} (primeiro elemento)")


# ===== 3. TAMANHO DA LISTA =====
print("\n3. TAMANHO DA LISTA")
print("-" * 60)

frutas = ["maçã", "banana", "laranja"]
print(f"Lista: {frutas}")
print(f"Quantidade de elementos: {len(frutas)}")

lista_vazia = []
print(f"\nLista vazia: {lista_vazia}")
print(f"Quantidade de elementos: {len(lista_vazia)}")


# ===== 4. FATIAMENTO (SLICING) =====
print("\n4. FATIAMENTO (SLICING)")
print("-" * 60)

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(f"Lista original: {letras}")
print(f"Índices:        0   1   2   3   4   5   6")

print(f"\nFatiamento [inicio:fim]:")
print(f"letras[0:3] = {letras[0:3]} (do índice 0 ao 2, não inclui 3)")
print(f"letras[2:5] = {letras[2:5]} (do índice 2 ao 4, não inclui 5)")
print(f"letras[1:6] = {letras[1:6]} (do índice 1 ao 5, não inclui 6)")

print(f"\nFatiamento [inicio:fim:passo]:")
print(f"letras[0:7:2] = {letras[0:7:2]} (cada 2 posições)")
print(f"letras[0:7:3] = {letras[0:7:3]} (cada 3 posições)")
print(f"letras[1:6:2] = {letras[1:6:2]} (começa em 1, cada 2)")

print(f"\nFatiamento com omissão:")
print(f"letras[:3] = {letras[:3]} (começo até índice 2)")
print(f"letras[3:] = {letras[3:]} (índice 3 até o final)")
print(f"letras[:] = {letras[:]} (toda a lista)")

print(f"\nFatiamento invertido:")
print(f"letras[::-1] = {letras[::-1]} (lista invertida)")
print(f"letras[6:0:-1] = {letras[6:0:-1]} (de trás para frente)")


# ===== 5. ACESSAR MÚLTIPLOS ELEMENTOS =====
print("\n5. ACESSAR MÚLTIPLOS ELEMENTOS")
print("-" * 60)

numeros = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"Lista: {numeros}")

# Vários elementos consecutivos
print(f"\nElementos consecutivos:")
print(f"numeros[1:4] = {numeros[1:4]}")
print(f"numeros[5:8] = {numeros[5:8]}")

# Pegar elementos de trás para frente
print(f"\nElementos de trás para frente:")
print(f"numeros[-3:] = {numeros[-3:]} (últimos 3 elementos)")
print(f"numeros[-5:-2] = {numeros[-5:-2]} (do -5 ao -3)")

# Pegar elementos alternados
print(f"\nElementos alternados:")
print(f"numeros[::2] = {numeros[::2]} (pares)")
print(f"numeros[1::2] = {numeros[1::2]} (ímpares)")


# ===== 6. VERIFICAR SE ELEMENTO EXISTE =====
print("\n6. VERIFICAR SE ELEMENTO EXISTE")
print("-" * 60)

cores = ["vermelho", "azul", "verde", "amarelo"]
print(f"Lista: {cores}")

print(f"\nUsando operador 'in':")
print(f"'azul' in cores: {'azul' in cores}")
print(f"'preto' in cores: {'preto' in cores}")
print(f"'verde' in cores: {'verde' in cores}")
print(f"'roxo' in cores: {'roxo' in cores}")

print(f"\nUsando operador 'not in':")
print(f"'preto' not in cores: {'preto' not in cores}")
print(f"'vermelho' not in cores: {'vermelho' not in cores}")


# ===== 7. ENCONTRAR POSIÇÃO DE UM ELEMENTO =====
print("\n7. ENCONTRAR POSIÇÃO DE UM ELEMENTO")
print("-" * 60)

paises = ["Brasil", "Portugal", "Espanha", "França", "Itália", "Brasil"]
print(f"Lista: {paises}")

# index() retorna o índice da primeira ocorrência
indice = paises.index("Brasil")
print(f"\npaises.index('Brasil') = {indice}")

indice = paises.index("Espanha")
print(f"paises.index('Espanha') = {indice}")

# Encontrar com search manual
print(f"\nBusca manual:")
elemento_procurado = "França"
if elemento_procurado in paises:
    posicao = paises.index(elemento_procurado)
    print(f"'{elemento_procurado}' encontrado na posição {posicao}")


# ===== 8. CONTAR OCORRÊNCIAS =====
print("\n8. CONTAR OCORRÊNCIAS")
print("-" * 60)

numeros = [1, 2, 3, 2, 4, 2, 5, 2, 6, 2]
print(f"Lista: {numeros}")

print(f"\nOcorrências do número 2: {numeros.count(2)}")
print(f"Ocorrências do número 1: {numeros.count(1)}")
print(f"Ocorrências do número 5: {numeros.count(5)}")
print(f"Ocorrências do número 10: {numeros.count(10)}")


# ===== 9. ACESSAR LISTA ANINHADA =====
print("\n9. ACESSAR LISTA ANINHADA")
print("-" * 60)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matriz: {matriz}")

print(f"\nAcessar linhas:")
print(f"matriz[0] = {matriz[0]} (primeira linha)")
print(f"matriz[1] = {matriz[1]} (segunda linha)")
print(f"matriz[2] = {matriz[2]} (terceira linha)")

print(f"\nAcessar elementos específicos:")
print(f"matriz[0][0] = {matriz[0][0]} (linha 0, coluna 0)")
print(f"matriz[0][2] = {matriz[0][2]} (linha 0, coluna 2)")
print(f"matriz[1][1] = {matriz[1][1]} (linha 1, coluna 1)")
print(f"matriz[2][2] = {matriz[2][2]} (linha 2, coluna 2)")

print(f"\nAcessar com índices negativos:")
print(f"matriz[-1] = {matriz[-1]} (última linha)")
print(f"matriz[-1][-1] = {matriz[-1][-1]} (último elemento da última linha)")


# ===== 10. MODIFICAR ELEMENTOS =====
print("\n10. MODIFICAR ELEMENTOS")
print("-" * 60)

lista = [10, 20, 30, 40, 50]
print(f"Lista original: {lista}")

# Modificar um elemento
lista[0] = 100
print(f"Após lista[0] = 100: {lista}")

# Modificar outro elemento
lista[2] = 300
print(f"Após lista[2] = 300: {lista}")

# Modificar com índice negativo
lista[-1] = 500
print(f"Após lista[-1] = 500: {lista}")

# Modificar um intervalo
lista_teste = ['a', 'b', 'c', 'd', 'e']
print(f"\nLista original: {lista_teste}")
lista_teste[1:3] = ['B', 'C']
print(f"Após lista_teste[1:3] = ['B', 'C']: {lista_teste}")


# ===== 11. PRATICAR COM EXEMPLOS =====
print("\n11. EXERCÍCIO PRÁTICO")
print("-" * 60)

# Exemplo 1: Acessar dados de uma lista de notas
notas = [8.5, 7.0, 9.5, 6.0, 8.0, 7.5]
print(f"Notas da turma: {notas}")
print(f"Primeira nota: {notas[0]}")
print(f"Última nota: {notas[-1]}")
print(f"Primeiras 3 notas: {notas[:3]}")
print(f"Últimas 2 notas: {notas[-2:]}")

# Exemplo 2: Trabalhar com informações de pessoas
pessoas = [
    ["João", 25, "São Paulo"],
    ["Maria", 30, "Rio de Janeiro"],
    ["Pedro", 22, "Belo Horizonte"]
]
print(f"\nPessoas:")
for i, pessoa in enumerate(pessoas):
    print(f"Pessoa {i}: {pessoa}")

print(f"\nAcesso aos dados:")
print(f"Primeira pessoa: {pessoas[0]}")
print(f"Nome da segunda pessoa: {pessoas[1][0]}")
print(f"Idade da terceira pessoa: {pessoas[2][1]}")
print(f"Cidade da primeira pessoa: {pessoas[0][2]}")

# Exemplo 3: Filtrar dados
print(f"\nFiltrar notas acima de 7.5:")
notas_altas = [nota for nota in notas if nota > 7.5]
print(f"Notas: {notas_altas}")

print("\n" + "=" * 60)
