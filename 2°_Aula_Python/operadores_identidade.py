# ==========================================
# OPERADORES DE IDENTIDADE EM PYTHON
# ==========================================
# Comparam se dois objetos são o MESMO OBJETO (mesma referência de memória)
# NÃO comparam o conteúdo, mas a identidade

# 1. OPERADOR IS
print("=" * 50)
print("1. OPERADOR IS")
print("=" * 50)
print("Verifica se dois objetos são o MESMO OBJETO")
print("Compara o endereço de memória (id)")
print()

# Exemplo 1: Mesma variável
a = 10
b = a

print(f"a = {a}")
print(f"b = a")
print(f"a is b: {a is b}")  # True (apontam para o mesmo objeto)
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print()

# Exemplo 2: Valores iguais mas objetos diferentes
x = [1, 2, 3]
y = [1, 2, 3]

print(f"x = {x}")
print(f"y = {y}")
print(f"x == y: {x == y}")  # True (conteúdo igual)
print(f"x is y: {x is y}")  # False (objetos diferentes)
print(f"id(x): {id(x)}")
print(f"id(y): {id(y)}")
print()

# Exemplo 3: Atribuição de lista
lista1 = [1, 2, 3]
lista2 = lista1  # Aponta para o MESMO objeto

print(f"lista1 = {lista1}")
print(f"lista2 = lista1")
print(f"lista1 == lista2: {lista1 == lista2}")  # True
print(f"lista1 is lista2: {lista1 is lista2}")  # True (mesmo objeto)
print(f"id(lista1): {id(lista1)}")
print(f"id(lista2): {id(lista2)}")
print()

# Modificar lista1 também afeta lista2
lista1.append(4)
print(f"Após lista1.append(4):")
print(f"lista1: {lista1}")
print(f"lista2: {lista2}")  # Também foi modificada!
print()

# ==========================================
# 2. OPERADOR IS NOT
# ==========================================
print("=" * 50)
print("2. OPERADOR IS NOT")
print("=" * 50)
print("Verifica se dois objetos NÃO são o MESMO OBJETO")
print()

# Exemplo 1: Objetos diferentes
lista_a = [1, 2, 3]
lista_b = [1, 2, 3]

print(f"lista_a = {lista_a}")
print(f"lista_b = {lista_b}")
print(f"lista_a is not lista_b: {lista_a is not lista_b}")  # True
print()

# Exemplo 2: Mesmo objeto
lista_c = [1, 2, 3]
lista_d = lista_c

print(f"lista_c = {lista_c}")
print(f"lista_d = lista_c")
print(f"lista_c is not lista_d: {lista_c is not lista_d}")  # False
print()

# ==========================================
# DIFERENÇA: IS vs ==
# ==========================================
print("=" * 50)
print("DIFERENÇA: IS vs ==")
print("=" * 50)
print("== : Compara CONTEÚDO")
print("is : Compara IDENTIDADE (referência de memória)")
print()

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a")
print()

print(f"a == b: {a == b}")  # True (mesmo conteúdo)
print(f"a is b: {a is b}")  # False (objetos diferentes)
print()

print(f"a == c: {a == c}")  # True (mesmo conteúdo)
print(f"a is c: {a is c}")  # True (mesmo objeto)
print()

# ==========================================
# IDENTIDADE COM NONE
# ==========================================
print("=" * 50)
print("IDENTIDADE COM NONE")
print("=" * 50)
print("None é um objeto especial em Python")
print("Sempre use 'is None' e 'is not None'")
print()

# Exemplo 1: Comparar com None
valor = None

print(f"valor = {valor}")
print(f"valor is None: {valor is None}")  # True
print(f"valor is not None: {valor is not None}")  # False
print()

# Exemplo 2: Variável com valor
resultado = 42

print(f"resultado = {resultado}")
print(f"resultado is None: {resultado is None}")  # False
print(f"resultado is not None: {resultado is not None}")  # True
print()

# Exemplo 3: Função que pode retornar None
def buscar_valor(existe=False):
    if existe:
        return "Encontrado"
    return None

resultado1 = buscar_valor(True)
resultado2 = buscar_valor(False)

print(f"resultado1 = {resultado1}")
print(f"resultado1 is None: {resultado1 is None}")  # False
print()

print(f"resultado2 = {resultado2}")
print(f"resultado2 is None: {resultado2 is None}")  # True
print()

# ==========================================
# IDENTIDADE COM TRUE E FALSE
# ==========================================
print("=" * 50)
print("IDENTIDADE COM TRUE E FALSE")
print("=" * 50)
print("Cuidado: use == para comparar booleanos")
print("Use 'is' apenas se souber o que está fazendo")
print()

valor = True

print(f"valor = {valor}")
print(f"valor is True: {valor is True}")  # True
print(f"valor == True: {valor == True}")  # True
print()

# Mas para valores truthy/falsy, use ==
numero = 1

print(f"numero = {numero}")
print(f"numero is True: {numero is True}")  # False (não é o objeto True)
print(f"numero == True: {numero == True}")  # True (valor equivalente)
print()

# ==========================================
# ID() - FUNÇÃO PARA VER A IDENTIDADE
# ==========================================
print("=" * 50)
print("ID() - FUNÇÃO PARA VER A IDENTIDADE")
print("=" * 50)
print("Retorna o endereço de memória do objeto")
print()

a = "Python"
b = "Python"
c = a

print(f"a = 'Python'")
print(f"b = 'Python'")
print(f"c = a")
print()

print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")
print()

# Note: strings podem ser internalizadas
# Python otimiza strings iguais para ocuparem o mesmo espaço
print(f"a is b: {a is b}")  # Pode ser True (otimização)
print(f"a is c: {a is c}")  # True
print()

# Com listas (não são internalizadas)
lista_a = [1, 2]
lista_b = [1, 2]

print(f"lista_a = {lista_a}")
print(f"lista_b = {lista_b}")
print()

print(f"id(lista_a): {id(lista_a)}")
print(f"id(lista_b): {id(lista_b)}")
print(f"lista_a is lista_b: {lista_a is lista_b}")  # False
print()

# ==========================================
# IDENTIDADE COM DIFERENTES TIPOS
# ==========================================
print("=" * 50)
print("IDENTIDADE COM DIFERENTES TIPOS")
print("=" * 50)

# Tuplas
tupla_a = (1, 2, 3)
tupla_b = (1, 2, 3)

print(f"tupla_a = {tupla_a}")
print(f"tupla_b = {tupla_b}")
print(f"tupla_a == tupla_b: {tupla_a == tupla_b}")
print(f"tupla_a is tupla_b: {tupla_a is tupla_b}")  # Pode ser True (otimização)
print()

# Dicionários
dict_a = {"nome": "João", "idade": 25}
dict_b = {"nome": "João", "idade": 25}

print(f"dict_a = {dict_a}")
print(f"dict_b = {dict_b}")
print(f"dict_a == dict_b: {dict_a == dict_b}")
print(f"dict_a is dict_b: {dict_a is dict_b}")  # False
print()

# Conjuntos
set_a = {1, 2, 3}
set_b = {1, 2, 3}

print(f"set_a = {set_a}")
print(f"set_b = {set_b}")
print(f"set_a == set_b: {set_a == set_b}")
print(f"set_a is set_b: {set_a is set_b}")  # False
print()

# ==========================================
# CACHE DE PEQUENOS INTEIROS
# ==========================================
print("=" * 50)
print("CACHE DE PEQUENOS INTEIROS")
print("=" * 50)
print("Python faz cache de inteiros de -5 a 256 para otimização")
print()

# Inteiros pequenos (cache)
a = 10
b = 10

print(f"a = 10")
print(f"b = 10")
print(f"a is b: {a is b}")  # True (ambos estão em cache)
print()

# Inteiros grandes (sem cache)
x = 1000
y = 1000

print(f"x = 1000")
print(f"y = 1000")
print(f"x is y: {x is y}")  # Pode ser False (não estão em cache)
print()

# Criar inteiros dinamicamente
x = 1000
y = int("1000")

print(f"x = 1000")
print(f"y = int('1000')")
print(f"x is y: {x is y}")  # Pode ser False
print()

# ==========================================
# EXEMPLOS PRÁTICOS
# ==========================================
print("=" * 50)
print("EXEMPLOS PRÁTICOS")
print("=" * 50)

# Exemplo 1: Verificar se variável é None
def processar_dados(dados):
    if dados is None:
        print("Nenhum dado fornecido")
        return
    print(f"Processando: {dados}")

processar_dados(None)
processar_dados([1, 2, 3])
print()

# Exemplo 2: Modificações de referência
original = [1, 2, 3]
copia = original

print(f"original = {original}")
print(f"copia = original")
print(f"original is copia: {original is copia}")

copia.append(4)
print(f"\nApós copia.append(4):")
print(f"original: {original}")
print(f"copia: {copia}")
print()

# Exemplo 3: Usar copy() para verdadeira cópia
from copy import copy

original = [1, 2, 3]
copia_verdadeira = copy(original)

print(f"original = {original}")
print(f"copia_verdadeira = copy(original)")
print(f"original is copia_verdadeira: {original is copia_verdadeira}")

copia_verdadeira.append(4)
print(f"\nApós copia_verdadeira.append(4):")
print(f"original: {original}")
print(f"copia_verdadeira: {copia_verdadeira}")
print()

# ==========================================
# RESUMO DOS OPERADORES DE IDENTIDADE
# ==========================================
print("=" * 50)
print("RESUMO DOS OPERADORES DE IDENTIDADE")
print("=" * 50)
print("""
is : Verifica se dois objetos são o MESMO OBJETO
     Compara endereço de memória (id)
     Retorna True se forem a mesma referência

is not : Verifica se dois objetos NÃO são o MESMO OBJETO
         Retorna True se forem referências diferentes

IMPORTANTE:
- Use '==' para comparar CONTEÚDO
- Use 'is' para comparar IDENTIDADE (referência)
- Sempre use 'is None' e 'is not None'
- Evite 'is' para comparar números e strings
- Lembre-se: None é um objeto único em Python

EXEMPLO:
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a == b  # True (mesmo conteúdo)
a is b  # False (objetos diferentes)
a is c  # True (mesma referência)
""")
