# ==========================================
# OPERADORES DE ATRIBUIÇÃO EM PYTHON
# ==========================================

# 1. ATRIBUIÇÃO SIMPLES (=)
print("=" * 50)
print("1. ATRIBUIÇÃO SIMPLES (=)")
print("=" * 50)

x = 10
print(f"x = 10")
print(f"Valor de x: {x}")

nome = "João"
print(f"\nnome = 'João'")
print(f"Valor de nome: {nome}")

lista = [1, 2, 3]
print(f"\nlista = [1, 2, 3]")
print(f"Valor de lista: {lista}")

# Atribuição múltipla
a, b, c = 5, 10, 15
print(f"\na, b, c = 5, 10, 15")
print(f"a = {a}, b = {b}, c = {c}")
print()

# 2. ADIÇÃO E ATRIBUIÇÃO (+=)
print("=" * 50)
print("2. ADIÇÃO E ATRIBUIÇÃO (+=)")
print("=" * 50)

x = 10
print(f"x = {x}")
print(f"x += 5  →  x = x + 5")
x += 5
print(f"Novo valor de x: {x}")

texto = "Olá"
print(f"\ntexto = '{texto}'")
print(f"texto += ' Mundo'")
texto += " Mundo"
print(f"Novo valor de texto: '{texto}'")

lista = [1, 2, 3]
print(f"\nlista = {lista}")
print(f"lista += [4, 5]")
lista += [4, 5]
print(f"Nova lista: {lista}")
print()

# 3. SUBTRAÇÃO E ATRIBUIÇÃO (-=)
print("=" * 50)
print("3. SUBTRAÇÃO E ATRIBUIÇÃO (-=)")
print("=" * 50)

x = 20
print(f"x = {x}")
print(f"x -= 7  →  x = x - 7")
x -= 7
print(f"Novo valor de x: {x}")

contador = 100
print(f"\ncontador = {contador}")
contador -= 15
print(f"contador -= 15")
print(f"Novo contador: {contador}")
print()

# 4. MULTIPLICAÇÃO E ATRIBUIÇÃO (*=)
print("=" * 50)
print("4. MULTIPLICAÇÃO E ATRIBUIÇÃO (*=)")
print("=" * 50)

x = 5
print(f"x = {x}")
print(f"x *= 3  →  x = x * 3")
x *= 3
print(f"Novo valor de x: {x}")

preco = 100
print(f"\npreco = {preco}")
desconto_multiplicador = 0.8  # 80%
print(f"preco *= 0.8  (aplicar 20% de desconto)")
preco *= 0.8
print(f"Novo preço: {preco}")

texto = "Ha"
print(f"\ntexto = '{texto}'")
print(f"texto *= 3")
texto *= 3
print(f"Novo texto: '{texto}'")
print()

# 5. DIVISÃO E ATRIBUIÇÃO (/=)
print("=" * 50)
print("5. DIVISÃO E ATRIBUIÇÃO (/=)")
print("=" * 50)

x = 50
print(f"x = {x}")
print(f"x /= 2  →  x = x / 2")
x /= 2
print(f"Novo valor de x: {x}")
print(f"Tipo: {type(x)}")  # float

total = 100
print(f"\ntotal = {total}")
print(f"total /= 4  (dividir igualmente entre 4 pessoas)")
total /= 4
print(f"Cada pessoa recebe: {total}")
print()

# 6. DIVISÃO INTEIRA E ATRIBUIÇÃO (//=)
print("=" * 50)
print("6. DIVISÃO INTEIRA E ATRIBUIÇÃO (//=)")
print("=" * 50)

x = 50
print(f"x = {x}")
print(f"x //= 3  →  x = x // 3")
x //= 3
print(f"Novo valor de x: {x}")
print(f"Tipo: {type(x)}")  # int

maçãs = 23
pessoas = 5
print(f"\nmaçãs = {maçãs}")
print(f"pessoas = {pessoas}")
print(f"maçãs //= pessoas  (dividir inteiro)")
maçãs //= pessoas
print(f"Cada pessoa recebe: {maçãs} maçãs")
print()

# 7. MÓDULO E ATRIBUIÇÃO (%=)
print("=" * 50)
print("7. MÓDULO E ATRIBUIÇÃO (%=)")
print("=" * 50)

x = 17
print(f"x = {x}")
print(f"x %= 5  →  x = x % 5")
x %= 5
print(f"Novo valor de x: {x}")

numero = 100
print(f"\nnumero = {numero}")
print(f"numero %= 7  (resto da divisão)")
numero %= 7
print(f"Resto: {numero}")

# Exemplo prático: sistema de horas
horas = 25
print(f"\nhoras = {horas}")
print(f"horas %= 24  (converter para formato 24h)")
horas %= 24
print(f"Horas no formato 24h: {horas}")
print()

# 8. POTÊNCIA E ATRIBUIÇÃO (**=)
print("=" * 50)
print("8. POTÊNCIA E ATRIBUIÇÃO (**=)")
print("=" * 50)

x = 2
print(f"x = {x}")
print(f"x **= 5  →  x = x ** 5")
x **= 5
print(f"Novo valor de x: {x}")

numero = 3
print(f"\nnumero = {numero}")
print(f"numero **= 3  (elevar ao cubo)")
numero **= 3
print(f"Novo valor: {numero}")
print()

# ==========================================
# OPERADORES DE ATRIBUIÇÃO BITWISE
# ==========================================
print("=" * 50)
print("OPERADORES DE ATRIBUIÇÃO BITWISE")
print("=" * 50)

# 9. AND BITWISE E ATRIBUIÇÃO (&=)
print("\n9. AND BITWISE E ATRIBUIÇÃO (&=)")
x = 12  # 1100 em binário
print(f"x = {x} (binário: {bin(x)})")
print(f"x &= 10  →  x = x & 10")
print(f"10 em binário: {bin(10)}")
x &= 10  # 1010
print(f"Novo valor de x: {x}")
print(f"Binário: {bin(x)}")
print()

# 10. OR BITWISE E ATRIBUIÇÃO (|=)
print("=" * 50)
print("10. OR BITWISE E ATRIBUIÇÃO (|=)")
x = 12  # 1100
print(f"x = {x} (binário: {bin(x)})")
print(f"x |= 10  →  x = x | 10")
print(f"10 em binário: {bin(10)}")
x |= 10  # 1110
print(f"Novo valor de x: {x}")
print(f"Binário: {bin(x)}")
print()

# 11. XOR BITWISE E ATRIBUIÇÃO (^=)
print("=" * 50)
print("11. XOR BITWISE E ATRIBUIÇÃO (^=)")
x = 12  # 1100
print(f"x = {x} (binário: {bin(x)})")
print(f"x ^= 10  →  x = x ^ 10")
print(f"10 em binário: {bin(10)}")
x ^= 10  # 0110
print(f"Novo valor de x: {x}")
print(f"Binário: {bin(x)}")
print()

# 12. DESLOCAMENTO À DIREITA E ATRIBUIÇÃO (>>=)
print("=" * 50)
print("12. DESLOCAMENTO À DIREITA E ATRIBUIÇÃO (>>=)")
x = 16  # 10000
print(f"x = {x} (binário: {bin(x)})")
print(f"x >>= 2  (deslocar 2 posições à direita)")
print(f"Equivalente a dividir por 2^2 = 4")
x >>= 2
print(f"Novo valor de x: {x}")
print(f"Binário: {bin(x)}")
print()

# 13. DESLOCAMENTO À ESQUERDA E ATRIBUIÇÃO (<<=)
print("=" * 50)
print("13. DESLOCAMENTO À ESQUERDA E ATRIBUIÇÃO (<<=)")
x = 5  # 101
print(f"x = {x} (binário: {bin(x)})")
print(f"x <<= 2  (deslocar 2 posições à esquerda)")
print(f"Equivalente a multiplicar por 2^2 = 4")
x <<= 2
print(f"Novo valor de x: {x}")
print(f"Binário: {bin(x)}")
print()

# ==========================================
# COMPARAÇÃO: COM E SEM OPERADORES
# ==========================================
print("=" * 50)
print("COMPARAÇÃO: COM E SEM OPERADORES")
print("=" * 50)

print("\nSEM operadores de atribuição:")
x = 10
x = x + 5
print(f"x = x + 5  →  x = {x}")

print("\nCOM operadores de atribuição:")
x = 10
x += 5
print(f"x += 5  →  x = {x}")

print("\n(Resultado igual, mas com operadores é mais conciso)")
print()

# ==========================================
# EXEMPLO PRÁTICO: CONTADOR
# ==========================================
print("=" * 50)
print("EXEMPLO PRÁTICO: CONTADOR")
print("=" * 50)

contador = 0
print(f"Iniciando contador: {contador}")

print("\nAcrescentando 1 cinco vezes:")
for i in range(5):
    contador += 1
    print(f"Iteração {i+1}: contador = {contador}")

print(f"\nValor final: {contador}")
print()

# ==========================================
# RESUMO DE TODOS OS OPERADORES
# ==========================================
print("=" * 50)
print("RESUMO DE TODOS OS OPERADORES DE ATRIBUIÇÃO")
print("=" * 50)
print("""
ARITMÉTICOS:
=   : Atribuição simples
+=  : Adição e atribuição
-=  : Subtração e atribuição
*=  : Multiplicação e atribuição
/=  : Divisão e atribuição
//= : Divisão inteira e atribuição
%=  : Módulo e atribuição
**= : Potência e atribuição

BITWISE:
&=  : AND bit a bit e atribuição
|=  : OR bit a bit e atribuição
^=  : XOR bit a bit e atribuição
>>=  : Deslocamento à direita e atribuição
<<=  : Deslocamento à esquerda e atribuição
""")
