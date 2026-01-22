# ==========================================
# OPERADORES DE COMPARAÇÃO EM PYTHON
# ==========================================
# Retornam True ou False

# 1. IGUALDADE (==)
print("=" * 50)
print("1. IGUALDADE (==)")
print("=" * 50)
a = 10
b = 10
c = 5

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print()

resultado = a == b
print(f"a == b: {resultado}")  # True

resultado = a == c
print(f"a == c: {resultado}")  # False

# Comparação com strings
nome1 = "João"
nome2 = "João"
nome3 = "Maria"

print(f"\nString: '{nome1}' == '{nome2}': {nome1 == nome2}")  # True
print(f"String: '{nome1}' == '{nome3}': {nome1 == nome3}")  # False
print()

# 2. DESIGUALDADE (!=)
print("=" * 50)
print("2. DESIGUALDADE (!=)")
print("=" * 50)
a = 10
b = 5

print(f"a = {a}")
print(f"b = {b}")
print()

resultado = a != b
print(f"a != b: {resultado}")  # True

resultado = a != 10
print(f"a != 10: {resultado}")  # False

print(f"\n'João' != 'Maria': {'João' != 'Maria'}")  # True
print(f"'João' != 'João': {'João' != 'João'}")  # False
print()

# 3. MAIOR QUE (>)
print("=" * 50)
print("3. MAIOR QUE (>)")
print("=" * 50)
a = 15
b = 10

print(f"a = {a}")
print(f"b = {b}")
print()

resultado = a > b
print(f"a > b: {resultado}")  # True

resultado = b > a
print(f"b > a: {resultado}")  # False

resultado = a > a
print(f"a > a: {resultado}")  # False

# Exemplo: Verificar se é maior de idade
idade = 20
print(f"\nIdade: {idade}")
print(f"Maior de 18 anos? {idade > 18}")  # True
print()

# 4. MENOR QUE (<)
print("=" * 50)
print("4. MENOR QUE (<)")
print("=" * 50)
a = 5
b = 10

print(f"a = {a}")
print(f"b = {b}")
print()

resultado = a < b
print(f"a < b: {resultado}")  # True

resultado = b < a
print(f"b < a: {resultado}")  # False

resultado = a < a
print(f"a < a: {resultado}")  # False

# Exemplo: Verificar se é menor de 30
idade = 25
print(f"\nIdade: {idade}")
print(f"Menor de 30 anos? {idade < 30}")  # True
print()

# 5. MAIOR OU IGUAL (>=)
print("=" * 50)
print("5. MAIOR OU IGUAL (>=)")
print("=" * 50)
a = 10
b = 5
c = 10

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print()

resultado = a >= b
print(f"a >= b: {resultado}")  # True

resultado = a >= c
print(f"a >= c: {resultado}")  # True

resultado = b >= a
print(f"b >= a: {resultado}")  # False

# Exemplo: Nota mínima
nota = 7
print(f"\nNota: {nota}")
print(f"Passou? (nota >= 7): {nota >= 7}")  # True
print()

# 6. MENOR OU IGUAL (<=)
print("=" * 50)
print("6. MENOR OU IGUAL (<=)")
print("=" * 50)
a = 5
b = 10
c = 5

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print()

resultado = a <= b
print(f"a <= b: {resultado}")  # True

resultado = a <= c
print(f"a <= c: {resultado}")  # True

resultado = b <= a
print(f"b <= a: {resultado}")  # False

# Exemplo: Limite de altura
altura = 1.75
print(f"\nAltura: {altura}m")
print(f"Dentro do limite (altura <= 1.80)? {altura <= 1.80}")  # True
print()

# ==========================================
# COMPARAÇÕES ENCADEADAS
# ==========================================
print("=" * 50)
print("COMPARAÇÕES ENCADEADAS")
print("=" * 50)

# Python permite comparar múltiplos valores
a = 5
b = 10
c = 15

# a < b < c
resultado = a < b < c
print(f"a = {a}, b = {b}, c = {c}")
print(f"a < b < c: {resultado}")  # True

# a < b >= c
resultado = a < b >= c
print(f"a < b >= c: {resultado}")  # False

# 0 < número < 10
numero = 7
print(f"\nnumero = {numero}")
print(f"0 < numero < 10: {0 < numero < 10}")  # True

numero = 15
print(f"numero = {numero}")
print(f"0 < numero < 10: {0 < numero < 10}")  # False
print()

# ==========================================
# COMPARAÇÕES COM DIFERENTES TIPOS
# ==========================================
print("=" * 50)
print("COMPARAÇÕES COM DIFERENTES TIPOS")
print("=" * 50)

# int vs float
print(f"10 == 10.0: {10 == 10.0}")  # True
print(f"10 > 9.5: {10 > 9.5}")  # True
print()

# Strings não são números
print(f"'10' == 10: {'10' == 10}")  # False
print(f"'10' > '5': {'10' > '5'}")  # False (comparação alfabética)
print(f"'5' > 'a': {'5' > 'a'}")  # False (ASCII)
print()

# ==========================================
# USANDO EM ESTRUTURAS CONDICIONAIS
# ==========================================
print("=" * 50)
print("USANDO EM ESTRUTURAS CONDICIONAIS")
print("=" * 50)

idade = 18
print(f"Idade: {idade}")

if idade >= 18:
    print("É maior de idade")
else:
    print("É menor de idade")

print()

nota = 6
print(f"Nota: {nota}")

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

print()

# ==========================================
# NEGAÇÃO COM 'not'
# ==========================================
print("=" * 50)
print("NEGAÇÃO COM 'not'")
print("=" * 50)

a = 10
b = 5

print(f"a = {a}, b = {b}")
print(f"a > b: {a > b}")  # True
print(f"not (a > b): {not (a > b)}")  # False

print(f"\na == b: {a == b}")  # False
print(f"not (a == b): {not (a == b)}")  # True

# Exemplo prático
idade = 25
print(f"\nIdade: {idade}")
print(f"Não é maior de idade: {not (idade >= 18)}")  # False
print()

# ==========================================
# COMPARAÇÕES COM LISTAS
# ==========================================
print("=" * 50)
print("COMPARAÇÕES COM LISTAS")
print("=" * 50)

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = [1, 2, 4]

print(f"lista1 = {lista1}")
print(f"lista2 = {lista2}")
print(f"lista3 = {lista3}")
print()

print(f"lista1 == lista2: {lista1 == lista2}")  # True (mesmo conteúdo)
print(f"lista1 == lista3: {lista1 == lista3}")  # False (conteúdo diferente)
print(f"lista1 != lista3: {lista1 != lista3}")  # True
print()

# ==========================================
# RESUMO DOS OPERADORES
# ==========================================
print("=" * 50)
print("RESUMO DOS OPERADORES DE COMPARAÇÃO")
print("=" * 50)
print("""
==  : Igual a
!=  : Não igual a
>   : Maior que
<   : Menor que
>=  : Maior ou igual a
<=  : Menor ou igual a

Retornam sempre True ou False
""")
