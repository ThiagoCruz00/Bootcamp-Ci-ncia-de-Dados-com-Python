# ==========================================
# ESTRUTURAS DE REPETIÇÃO EM PYTHON
# ==========================================

# ==========================================
# 1. FOR - LOOP COM LISTAS
# ==========================================
print("=" * 50)
print("1. FOR - LOOP COM LISTAS")
print("=" * 50)

# Exemplo 1: Iteração simples
print("Exemplo 1: Iteração simples")
frutas = ["maçã", "banana", "laranja", "uva"]

for fruta in frutas:
    print(f"Fruta: {fruta}")

print()

# Exemplo 2: Acessar índice e valor
print("Exemplo 2: Acessar índice e valor com enumerate")
numeros = [10, 20, 30, 40]

for indice, numero in enumerate(numeros):
    print(f"Índice {indice}: {numero}")

print()

# Exemplo 3: Iteração com strings
print("Exemplo 3: Iteração com strings")
palavra = "Python"

for letra in palavra:
    print(f"Letra: {letra}")

print()

# Exemplo 4: Iteração com tupla
print("Exemplo 4: Iteração com tupla")
coordenadas = (10, 20, 30)

for valor in coordenadas:
    print(f"Valor: {valor}")

print()

# ==========================================
# 2. FOR - LOOP COM RANGE
# ==========================================
print("=" * 50)
print("2. FOR - LOOP COM RANGE")
print("=" * 50)

# Exemplo 1: Range básico (começa em 0)
print("Exemplo 1: range(5) - de 0 a 4")

for i in range(5):
    print(i, end=" ")
print("\n")

# Exemplo 2: Range com início e fim
print("Exemplo 2: range(1, 6) - de 1 a 5")

for i in range(1, 6):
    print(i, end=" ")
print("\n")

# Exemplo 3: Range com passo
print("Exemplo 3: range(0, 10, 2) - passo de 2")

for i in range(0, 10, 2):
    print(i, end=" ")
print("\n")

# Exemplo 4: Range com passo negativo
print("Exemplo 4: range(10, 0, -1) - contagem regressiva")

for i in range(10, 0, -1):
    print(i, end=" ")
print("\n\n")

# Exemplo 5: Tabuada usando range
print("Exemplo 5: Tabuada do 5")

for i in range(1, 11):
    resultado = 5 * i
    print(f"5 × {i} = {resultado}")

print()

# ==========================================
# 3. FOR - LOOPS ANINHADOS
# ==========================================
print("=" * 50)
print("3. FOR - LOOPS ANINHADOS")
print("=" * 50)

# Exemplo 1: Matriz (loops duplos)
print("Exemplo 1: Matriz 3x3")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in matriz:
    for valor in linha:
        print(valor, end=" ")
    print()

print()

# Exemplo 2: Tabuada completa
print("Exemplo 2: Tabuada completa")

for i in range(1, 4):
    print(f"Tabuada do {i}:")
    for j in range(1, 6):
        print(f"  {i} × {j} = {i * j}")
    print()

# Exemplo 3: Padrão de estrelas
print("Exemplo 3: Padrão de estrelas (triângulo)")

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

print()

# ==========================================
# 4. FOR - LOOP COM ZIP
# ==========================================
print("=" * 50)
print("4. FOR - LOOP COM ZIP")
print("=" * 50)

# Exemplo 1: Percorrer duas listas simultaneamente
print("Exemplo 1: Percorrer duas listas")
nomes = ["João", "Maria", "Pedro"]
idades = [25, 30, 28]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")

print()

# Exemplo 2: Percorrer três listas
print("Exemplo 2: Percorrer três listas")
nomes = ["João", "Maria", "Pedro"]
idades = [25, 30, 28]
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]

for nome, idade, cidade in zip(nomes, idades, cidades):
    print(f"{nome}, {idade} anos, de {cidade}")

print()

# ==========================================
# 5. FOR - LOOP COM DICIONÁRIO
# ==========================================
print("=" * 50)
print("5. FOR - LOOP COM DICIONÁRIO")
print("=" * 50)

# Exemplo 1: Iteração com chaves
print("Exemplo 1: Iteração com chaves")
pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}

for chave in pessoa:
    print(f"Chave: {chave}")

print()

# Exemplo 2: Iteração com valores
print("Exemplo 2: Iteração com valores")

for valor in pessoa.values():
    print(f"Valor: {valor}")

print()

# Exemplo 3: Iteração com chave e valor
print("Exemplo 3: Iteração com chave e valor")

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

print()

# Exemplo 4: Dicionário com múltiplos registros
print("Exemplo 4: Dicionário com múltiplos registros")
alunos = {
    "João": {"nota": 8.5, "turma": "A"},
    "Maria": {"nota": 9.0, "turma": "B"},
    "Pedro": {"nota": 7.5, "turma": "A"}
}

for nome, dados in alunos.items():
    print(f"{nome}: Nota {dados['nota']}, Turma {dados['turma']}")

print()

# ==========================================
# 6. WHILE - LOOP COM CONDIÇÃO
# ==========================================
print("=" * 50)
print("6. WHILE - LOOP COM CONDIÇÃO")
print("=" * 50)

# Exemplo 1: While simples
print("Exemplo 1: While simples")
contador = 1

while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1

print()

# Exemplo 2: While com input
print("Exemplo 2: While com input (simulado)")
# senha = ""
# while senha != "1234":
#     senha = input("Digite a senha: ")
# print("Acesso concedido!")

# Simulado:
print("Exemplo simulado: Digite '1234' para acessar")
print("(Pulando input interativo)")

print()

# Exemplo 3: While com lista
print("Exemplo 3: While com lista")
lista = [10, 20, 30, 40, 50]
indice = 0

while indice < len(lista):
    print(f"Elemento: {lista[indice]}")
    indice += 1

print()

# Exemplo 4: While infinito com break
print("Exemplo 4: While com break (contagem até 3)")
contador = 0

while True:
    contador += 1
    print(f"Contador: {contador}")
    
    if contador == 3:
        print("Parando...")
        break

print()

# ==========================================
# 7. BREAK - SAIR DO LOOP
# ==========================================
print("=" * 50)
print("7. BREAK - SAIR DO LOOP")
print("=" * 50)

# Exemplo 1: Break em for
print("Exemplo 1: Break em for (procurar número)")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
procurado = 6

for numero in numeros:
    if numero == procurado:
        print(f"Número {procurado} encontrado!")
        break
    print(f"Verificando: {numero}")

print()

# Exemplo 2: Break em while
print("Exemplo 2: Break em while")
contador = 0

while True:
    contador += 1
    print(f"Tentativa {contador}")
    
    if contador == 3:
        print("Saindo do loop")
        break

print()

# Exemplo 3: Break em loop aninhado
print("Exemplo 3: Break em loop aninhado")

for i in range(1, 4):
    print(f"Linha {i}:")
    for j in range(1, 6):
        if j == 3:
            print("  Saindo da coluna")
            break
        print(f"  Coluna {j}")

print()

# ==========================================
# 8. CONTINUE - PULAR ITERAÇÃO
# ==========================================
print("=" * 50)
print("8. CONTINUE - PULAR ITERAÇÃO")
print("=" * 50)

# Exemplo 1: Continue com números pares
print("Exemplo 1: Continue - pular pares")

for numero in range(1, 11):
    if numero % 2 == 0:
        continue
    print(f"Número ímpar: {numero}")

print()

# Exemplo 2: Continue em while
print("Exemplo 2: Continue em while")
contador = 0

while contador < 5:
    contador += 1
    
    if contador == 3:
        print(f"  Pulando {contador}")
        continue
    
    print(f"Processando: {contador}")

print()

# Exemplo 3: Validação com continue
print("Exemplo 3: Validação com continue")
nomes = ["João", "", "Maria", "", "Pedro"]

for nome in nomes:
    if nome == "":
        continue
    print(f"Nome: {nome}")

print()

# ==========================================
# 9. ELSE COM LOOPS
# ==========================================
print("=" * 50)
print("9. ELSE COM LOOPS")
print("=" * 50)

# Exemplo 1: Else com for (não encontrou break)
print("Exemplo 1: Else com for (número não encontrado)")
numeros = [1, 2, 3, 4, 5]
procurado = 10

for numero in numeros:
    if numero == procurado:
        print(f"Encontrado: {procurado}")
        break
else:
    print(f"Número {procurado} não encontrado na lista")

print()

# Exemplo 2: Else com for (encontrou break)
print("Exemplo 2: Else com for (número encontrado)")
numeros = [1, 2, 3, 4, 5]
procurado = 3

for numero in numeros:
    if numero == procurado:
        print(f"Encontrado: {procurado}")
        break
else:
    print(f"Número {procurado} não encontrado na lista")

print()

# Exemplo 3: Else com while
print("Exemplo 3: Else com while")
contador = 1

while contador <= 3:
    print(f"Contador: {contador}")
    contador += 1
else:
    print("While terminado normalmente (sem break)")

print()

# ==========================================
# 10. COMPREENSÃO DE LISTAS
# ==========================================
print("=" * 50)
print("10. COMPREENSÃO DE LISTAS")
print("=" * 50)

# Exemplo 1: Compreensão simples
print("Exemplo 1: Compreensão simples (quadrados)")
numeros = [1, 2, 3, 4, 5]
quadrados = [n ** 2 for n in numeros]
print(f"Números: {numeros}")
print(f"Quadrados: {quadrados}")

print()

# Exemplo 2: Compreensão com condição
print("Exemplo 2: Compreensão com condição (pares)")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n for n in numeros if n % 2 == 0]
print(f"Números: {numeros}")
print(f"Pares: {pares}")

print()

# Exemplo 3: Compreensão com transformação e condição
print("Exemplo 3: Compreensão com transformação e condição")
numeros = [1, 2, 3, 4, 5]
dobrados_pares = [n * 2 for n in numeros if n % 2 == 0]
print(f"Números: {numeros}")
print(f"Dobrados (pares): {dobrados_pares}")

print()

# Exemplo 4: Compreensão de strings
print("Exemplo 4: Compreensão com strings")
palavras = ["python", "java", "javascript"]
maiusculas = [p.upper() for p in palavras]
print(f"Palavras: {palavras}")
print(f"Maiúsculas: {maiusculas}")

print()

# Exemplo 5: Compreensão com múltiplos loops
print("Exemplo 5: Compreensão com múltiplos loops")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
elementos = [valor for linha in matriz for valor in linha]
print(f"Matriz: {matriz}")
print(f"Elementos: {elementos}")

print()

# ==========================================
# 11. COMPREENSÃO DE DICIONÁRIOS
# ==========================================
print("=" * 50)
print("11. COMPREENSÃO DE DICIONÁRIOS")
print("=" * 50)

# Exemplo 1: Dicionário de quadrados
print("Exemplo 1: Dicionário de quadrados")
numeros = [1, 2, 3, 4, 5]
quadrados_dict = {n: n ** 2 for n in numeros}
print(f"Números: {numeros}")
print(f"Dict: {quadrados_dict}")

print()

# Exemplo 2: Inverter dicionário
print("Exemplo 2: Inverter dicionário (chave <-> valor)")
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Invertido: {invertido}")

print()

# ==========================================
# 12. COMPREENSÃO DE CONJUNTOS
# ==========================================
print("=" * 50)
print("12. COMPREENSÃO DE CONJUNTOS")
print("=" * 50)

# Exemplo 1: Conjunto de números únicos
print("Exemplo 1: Conjunto de números únicos")
numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unicos = {n for n in numeros}
print(f"Números: {numeros}")
print(f"Únicos: {unicos}")

print()

# Exemplo 2: Conjunto com condição
print("Exemplo 2: Conjunto com condição (pares)")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares_set = {n for n in numeros if n % 2 == 0}
print(f"Números: {numeros}")
print(f"Pares: {pares_set}")

print()

# ==========================================
# 13. EXEMPLOS PRÁTICOS COMPLETOS
# ==========================================
print("=" * 50)
print("13. EXEMPLOS PRÁTICOS COMPLETOS")
print("=" * 50)

# Exemplo 1: Calcular soma de uma lista
print("\nExemplo 1: Calcular soma")
print("-" * 40)
numeros = [10, 20, 30, 40, 50]
soma = 0

for numero in numeros:
    soma += numero

print(f"Números: {numeros}")
print(f"Soma: {soma}")

print()

# Exemplo 2: Encontrar maior valor
print("Exemplo 2: Encontrar maior valor")
print("-" * 40)
numeros = [45, 23, 89, 12, 67, 34]
maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print(f"Números: {numeros}")
print(f"Maior: {maior}")

print()

# Exemplo 3: Contar ocorrências
print("Exemplo 3: Contar ocorrências de um caractere")
print("-" * 40)
texto = "Python"
caractere = "p"
contagem = 0

for letra in texto.lower():
    if letra == caractere:
        contagem += 1

print(f"Texto: {texto}")
print(f"Caractere: {caractere}")
print(f"Ocorrências: {contagem}")

print()

# Exemplo 4: Gerar lista de números pares
print("Exemplo 4: Gerar lista de números pares")
print("-" * 40)
pares = [n for n in range(1, 21) if n % 2 == 0]
print(f"Números pares de 1 a 20: {pares}")

print()

# Exemplo 5: Filtrar alunos aprovados
print("Exemplo 5: Filtrar alunos aprovados")
print("-" * 40)
alunos = {
    "João": 8.5,
    "Maria": 9.0,
    "Pedro": 6.5,
    "Ana": 7.5,
    "Carlos": 5.0
}

aprovados = [nome for nome, nota in alunos.items() if nota >= 7]
reprovados = [nome for nome, nota in alunos.items() if nota < 7]

print("Alunos e notas:")
for nome, nota in alunos.items():
    print(f"  {nome}: {nota}")

print(f"\nAprovados: {aprovados}")
print(f"Reprovados: {reprovados}")

print()

# Exemplo 6: Processar linhas de um arquivo (simulado)
print("Exemplo 6: Processar dados (simulado)")
print("-" * 40)
dados = [
    "nome,idade,cidade",
    "João,25,São Paulo",
    "Maria,30,Rio de Janeiro",
    "Pedro,28,Belo Horizonte"
]

print("Processando dados:")
for indice, linha in enumerate(dados):
    if indice == 0:
        print(f"Cabeçalho: {linha}")
    else:
        partes = linha.split(",")
        nome, idade, cidade = partes
        print(f"  {nome} ({idade} anos) de {cidade}")

print()

# ==========================================
# 14. BOAS PRÁTICAS
# ==========================================
print("=" * 50)
print("14. BOAS PRÁTICAS")
print("=" * 50)
print("""
RECOMENDAÇÕES:

1. PREFIRA FOR em vez de WHILE quando possível
   - FOR é mais seguro (não risco de loop infinito)
   - FOR é mais legível

2. USE COMPREENSÕES para transformações simples
   - ✓ pares = [n for n in nums if n % 2 == 0]
   - ✗ pares = []
     for n in nums:
         if n % 2 == 0:
             pares.append(n)

3. USE ENUMERATE quando precisar do índice
   - ✓ for indice, valor in enumerate(lista):
   - ✗ for i in range(len(lista)):
          valor = lista[i]

4. USE ZIP para iterar múltiplas listas
   - ✓ for nome, idade in zip(nomes, idades):
   - ✗ for i in range(len(nomes)):
          nome = nomes[i]
          idade = idades[i]

5. EVITE LOOPS ANINHADOS muito profundos
   - Refatore em funções separadas

6. USE BREAK e CONTINUE com moderação
   - Podem dificultar compreensão do código

7. PREFIRA COMPREENSÕES a loops para listas
   - Mais rápido e mais Pythônico

8. NOMEAR VARIÁVEIS DE LOOP claramente
   - ✓ for livro in livros:
   - ✗ for l in livros:
""")

print()

# ==========================================
# RESUMO
# ==========================================
print("=" * 50)
print("RESUMO DE ESTRUTURAS DE REPETIÇÃO")
print("=" * 50)
print("""
FOR:
- Percorrer listas, tuplas, strings, dicionários
- for item in colecao:
- for indice, item in enumerate(colecao):
- for item1, item2 in zip(colecao1, colecao2):

WHILE:
- Repetir enquanto condição é verdadeira
- while condicao:

BREAK:
- Sair do loop imediatamente
- break

CONTINUE:
- Pular para próxima iteração
- continue

ELSE:
- Executar se loop terminar sem break
- for/while ... else:

COMPREENSÕES:
- [expr for item in colecao]
- [expr for item in colecao if condicao]
- {chave: valor for item in colecao}
- {expr for item in colecao}

DICAS:
- FOR é preferível a WHILE
- Use compreensões para transformações simples
- Combine com enumerate, zip, filter, map
- Mantenha loops simples e legíveis
""")
