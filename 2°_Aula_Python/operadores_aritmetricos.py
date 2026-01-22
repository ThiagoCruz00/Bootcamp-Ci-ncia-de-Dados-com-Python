# ==========================================
# OPERADORES ARITMÉTICOS EM PYTHON
# ==========================================

# 1. ADIÇÃO (+)
print("=" * 40)
print("1. ADIÇÃO (+)")
print("=" * 40)
a = 10
b = 5
resultado = a + b
print(f"{a} + {b} = {resultado}")
print()

# 2. SUBTRAÇÃO (-)
print("=" * 40)
print("2. SUBTRAÇÃO (-)")
print("=" * 40)
a = 10
b = 5
resultado = a - b
print(f"{a} - {b} = {resultado}")
print()

# 3. MULTIPLICAÇÃO (*)
print("=" * 40)
print("3. MULTIPLICAÇÃO (*)")
print("=" * 40)
a = 10
b = 5
resultado = a * b
print(f"{a} * {b} = {resultado}")
print()

# 4. DIVISÃO (/)
print("=" * 40)
print("4. DIVISÃO (/)")
print("=" * 40)
a = 10
b = 5
resultado = a / b
print(f"{a} / {b} = {resultado}")
print(f"Tipo do resultado: {type(resultado)}")  # Sempre retorna float
print()

# 5. DIVISÃO INTEIRA (//)
print("=" * 40)
print("5. DIVISÃO INTEIRA (//)")
print("=" * 40)
a = 10
b = 3
resultado = a // b
print(f"{a} // {b} = {resultado}")
print(f"Tipo do resultado: {type(resultado)}")  # Retorna int
print()

# 6. MÓDULO (%)
print("=" * 40)
print("6. MÓDULO (%)")
print("=" * 40)
print("Retorna o RESTO da divisão")
a = 10
b = 3
resultado = a % b
print(f"{a} % {b} = {resultado}")  # 10 dividido por 3 = 3 com resto 1
print()

# Exemplo: Verificar se número é par
numero = 10
if numero % 2 == 0:
    print(f"{numero} é PAR")
else:
    print(f"{numero} é ÍMPAR")
print()

# 7. POTÊNCIA (**)
print("=" * 40)
print("7. POTÊNCIA (**)")
print("=" * 40)
a = 2
b = 5
resultado = a ** b
print(f"{a} ** {b} = {resultado}")  # 2 elevado à 5ª potência
print()

# Exemplo: Raiz quadrada (elevado a 0.5)
numero = 16
resultado = numero ** 0.5
print(f"Raiz quadrada de {numero} = {resultado}")
print()

# ==========================================
# OPERAÇÕES COM NÚMEROS NEGATIVOS
# ==========================================
print("=" * 40)
print("OPERAÇÕES COM NÚMEROS NEGATIVOS")
print("=" * 40)
a = -10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print()

# ==========================================
# OPERAÇÕES COM NÚMEROS DECIMAIS
# ==========================================
print("=" * 40)
print("OPERAÇÕES COM NÚMEROS DECIMAIS")
print("=" * 40)
a = 10.5
b = 2.3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
print()

# ==========================================
# PRECEDÊNCIA DE OPERADORES
# ==========================================
print("=" * 40)
print("PRECEDÊNCIA DE OPERADORES")
print("=" * 40)
print("Ordem: **, *, /, //, %, +, -")
print()

# Sem parênteses
resultado = 2 + 3 * 4
print(f"2 + 3 * 4 = {resultado}")  # 14 (não 20)

# Com parênteses
resultado = (2 + 3) * 4
print(f"(2 + 3) * 4 = {resultado}")  # 20
print()

# ==========================================
# OPERADORES DE ATRIBUIÇÃO COMBINADOS
# ==========================================
print("=" * 40)
print("OPERADORES DE ATRIBUIÇÃO COMBINADOS")
print("=" * 40)
x = 10
print(f"x = {x}")

x += 5  # x = x + 5
print(f"x += 5 → x = {x}")

x -= 3  # x = x - 3
print(f"x -= 3 → x = {x}")

x *= 2  # x = x * 2
print(f"x *= 2 → x = {x}")

x /= 4  # x = x / 4
print(f"x /= 4 → x = {x}")

x //= 2  # x = x // 2
print(f"x //= 2 → x = {x}")

x %= 5  # x = x % 5
print(f"x %= 5 → x = {x}")

x **= 2  # x = x ** 2
print(f"x **= 2 → x = {x}")
