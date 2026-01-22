# ==========================================
# OPERADORES LÓGICOS EM PYTHON
# ==========================================
# Usam valores booleanos (True/False)

# 1. OPERADOR AND (E)
print("=" * 50)
print("1. OPERADOR AND (E)")
print("=" * 50)
print("Retorna True se TODAS as condições forem verdadeiras")
print()

# Exemplo 1: Verificar maioridade e ter habilitação
idade = 25
tem_habilitacao = True

print(f"idade = {idade}")
print(f"tem_habilitacao = {tem_habilitacao}")
print()

resultado = idade >= 18 and tem_habilitacao
print(f"(idade >= 18) and tem_habilitacao: {resultado}")  # True
print("Pode dirigir!")
print()

# Exemplo 2: Ambas falsas
idade = 16
tem_habilitacao = False

print(f"idade = {idade}")
print(f"tem_habilitacao = {tem_habilitacao}")
print()

resultado = idade >= 18 and tem_habilitacao
print(f"(idade >= 18) and tem_habilitacao: {resultado}")  # False
print()

# Exemplo 3: Uma verdadeira, uma falsa
idade = 25
tem_habilitacao = False

print(f"idade = {idade}")
print(f"tem_habilitacao = {tem_habilitacao}")
print()

resultado = idade >= 18 and tem_habilitacao
print(f"(idade >= 18) and tem_habilitacao: {resultado}")  # False
print()

# Tabela verdade do AND
print("=" * 50)
print("TABELA VERDADE - AND")
print("=" * 50)
print(f"True  and True  = {True and True}")    # True
print(f"True  and False = {True and False}")   # False
print(f"False and True  = {False and True}")   # False
print(f"False and False = {False and False}")  # False
print()

# 2. OPERADOR OR (OU)
print("=" * 50)
print("2. OPERADOR OR (OU)")
print("=" * 50)
print("Retorna True se PELO MENOS UMA condição for verdadeira")
print()

# Exemplo 1: Pode entrar na festa
eh_maior_idade = True
eh_acompanhado = False

print(f"eh_maior_idade = {eh_maior_idade}")
print(f"eh_acompanhado = {eh_acompanhado}")
print()

resultado = eh_maior_idade or eh_acompanhado
print(f"eh_maior_idade or eh_acompanhado: {resultado}")  # True
print("Pode entrar!")
print()

# Exemplo 2: Ambas verdadeiras
eh_maior_idade = True
eh_acompanhado = True

print(f"eh_maior_idade = {eh_maior_idade}")
print(f"eh_acompanhado = {eh_acompanhado}")
print()

resultado = eh_maior_idade or eh_acompanhado
print(f"eh_maior_idade or eh_acompanhado: {resultado}")  # True
print("Pode entrar!")
print()

# Exemplo 3: Nenhuma verdadeira
eh_maior_idade = False
eh_acompanhado = False

print(f"eh_maior_idade = {eh_maior_idade}")
print(f"eh_acompanhado = {eh_acompanhado}")
print()

resultado = eh_maior_idade or eh_acompanhado
print(f"eh_maior_idade or eh_acompanhado: {resultado}")  # False
print("Não pode entrar!")
print()

# Tabela verdade do OR
print("=" * 50)
print("TABELA VERDADE - OR")
print("=" * 50)
print(f"True  or True  = {True or True}")    # True
print(f"True  or False = {True or False}")   # True
print(f"False or True  = {False or True}")   # True
print(f"False or False = {False or False}")  # False
print()

# 3. OPERADOR NOT (NÃO)
print("=" * 50)
print("3. OPERADOR NOT (NÃO)")
print("=" * 50)
print("Inverte o valor booleano (True → False, False → True)")
print()

# Exemplo 1: Negar True
verdadeiro = True
print(f"verdadeiro = {verdadeiro}")
print(f"not verdadeiro: {not verdadeiro}")  # False
print()

# Exemplo 2: Negar False
falso = False
print(f"falso = {falso}")
print(f"not falso: {not falso}")  # True
print()

# Exemplo 3: Verificar se NÃO é dia de semana
dia = "segunda"
eh_fim_de_semana = dia in ["sábado", "domingo"]

print(f"dia = '{dia}'")
print(f"eh_fim_de_semana = {eh_fim_de_semana}")
print(f"not eh_fim_de_semana: {not eh_fim_de_semana}")  # True
print("É dia de semana!")
print()

# Tabela verdade do NOT
print("=" * 50)
print("TABELA VERDADE - NOT")
print("=" * 50)
print(f"not True  = {not True}")    # False
print(f"not False = {not False}")   # True
print()

# ==========================================
# COMBINANDO OPERADORES LÓGICOS
# ==========================================
print("=" * 50)
print("COMBINANDO OPERADORES LÓGICOS")
print("=" * 50)

# AND com OR
idade = 20
tem_documento = True
eh_estudante = True

print(f"idade = {idade}")
print(f"tem_documento = {tem_documento}")
print(f"eh_estudante = {eh_estudante}")
print()

resultado = (idade >= 18 and tem_documento) or eh_estudante
print(f"(idade >= 18 and tem_documento) or eh_estudante: {resultado}")
print()

# Precedência: NOT > AND > OR
a = True
b = False
c = True

print(f"a = {a}, b = {b}, c = {c}")
print()

resultado = not a or b and c
print(f"not a or b and c: {resultado}")
# Equivalente a: (not a) or (b and c)
# = False or (False and True)
# = False or False
# = False
print()

# Com parênteses para deixar claro
resultado = (not a) or (b and c)
print(f"(not a) or (b and c): {resultado}")
print()

# ==========================================
# EXEMPLOS PRÁTICOS COM ESTRUTURAS CONDICIONAIS
# ==========================================
print("=" * 50)
print("EXEMPLOS PRÁTICOS COM ESTRUTURAS CONDICIONAIS")
print("=" * 50)

# Sistema de aprovação
nota = 7
presenca = 0.85  # 85%

print(f"\nNota: {nota}")
print(f"Presença: {presenca * 100}%")

if nota >= 7 and presenca >= 0.75:
    print("✓ Aprovado")
elif nota >= 7 or presenca >= 0.75:
    print("⚠ Em recuperação")
else:
    print("✗ Reprovado")

print()

# Sistema de aplicação para bolsa
renda = 1000
notas_boas = True

print(f"Renda familiar: R${renda}")
print(f"Notas boas: {notas_boas}")

if renda < 1500 and notas_boas:
    print("✓ Qualificado para bolsa")
else:
    print("✗ Não qualificado")

print()

# Acesso ao sistema
eh_admin = False
eh_desenvolvedor = True
senha_correta = True

print(f"É admin: {eh_admin}")
print(f"É desenvolvedor: {eh_desenvolvedor}")
print(f"Senha correta: {senha_correta}")

if (eh_admin or eh_desenvolvedor) and senha_correta:
    print("✓ Acesso concedido")
else:
    print("✗ Acesso negado")

print()

# ==========================================
# OPERADORES LÓGICOS COM COMPARAÇÕES
# ==========================================
print("=" * 50)
print("OPERADORES LÓGICOS COM COMPARAÇÕES")
print("=" * 50)

# Verificar intervalo
numero = 15

print(f"\nnumero = {numero}")
print(f"0 < numero < 20: {0 < numero < 20}")  # True
print(f"Equivalente a: (0 < numero) and (numero < 20)")
print(f"Resultado: {(0 < numero) and (numero < 20)}")
print()

# Verificar se está dentro ou fora de intervalos
idade = 30

print(f"idade = {idade}")
resultado = (idade < 13) or (idade >= 65)
print(f"É criança ou idoso? (idade < 13) or (idade >= 65): {resultado}")

if (idade < 13) or (idade >= 65):
    print("Desconto aplicável")
else:
    print("Sem desconto")

print()

# ==========================================
# SHORT-CIRCUIT EVALUATION
# ==========================================
print("=" * 50)
print("SHORT-CIRCUIT EVALUATION")
print("=" * 50)
print("""
Python avalia expressões lógicas de forma "preguiçosa":

AND: Se a primeira for False, não avalia a segunda
OR: Se a primeira for True, não avalia a segunda
""")

# Exemplo com AND
print("\nExemplo AND:")
resultado = False and print("Isto não será exibido")
print(f"False and ...: {resultado}")

resultado = True and print("Isto será exibido")
print(f"True and ...: {resultado}")

# Exemplo com OR
print("\nExemplo OR:")
resultado = True or print("Isto não será exibido")
print(f"True or ...: {resultado}")

resultado = False or print("Isto será exibido")
print(f"False or ...: {resultado}")

print()

# ==========================================
# VALORES TRUTHY E FALSY
# ==========================================
print("=" * 50)
print("VALORES TRUTHY E FALSY")
print("=" * 50)
print("""
Em Python, qualquer valor pode ser usado em contexto booleano:

FALSY (interpretados como False):
- False
- None
- 0 (zero numérico)
- "" (string vazia)
- [] (lista vazia)
- {} (dicionário vazio)
- () (tupla vazia)

TRUTHY (interpretados como True):
- Qualquer número diferente de 0
- Qualquer string não vazia
- Qualquer coleção não vazia
""")

print("\nExemplos:")

# String vazia vs não vazia
texto = ""
if texto:
    print(f"Texto '{texto}' é truthy")
else:
    print(f"Texto '{texto}' é falsy")

texto = "Python"
if texto:
    print(f"Texto '{texto}' é truthy")
else:
    print(f"Texto '{texto}' é falsy")

# Lista vazia vs não vazia
lista = []
if lista:
    print(f"Lista {lista} é truthy")
else:
    print(f"Lista {lista} é falsy")

lista = [1, 2, 3]
if lista:
    print(f"Lista {lista} é truthy")
else:
    print(f"Lista {lista} é falsy")

# Número zero vs não zero
numero = 0
if numero:
    print(f"Número {numero} é truthy")
else:
    print(f"Número {numero} é falsy")

numero = 42
if numero:
    print(f"Número {numero} é truthy")
else:
    print(f"Número {numero} é falsy")

print()

# ==========================================
# RESUMO DOS OPERADORES LÓGICOS
# ==========================================
print("=" * 50)
print("RESUMO DOS OPERADORES LÓGICOS")
print("=" * 50)
print("""
AND:
- Retorna True se TODAS as condições forem verdadeiras
- Sintaxe: condicao1 and condicao2
- Exemplo: idade >= 18 and tem_documento

OR:
- Retorna True se PELO MENOS UMA condição for verdadeira
- Sintaxe: condicao1 or condicao2
- Exemplo: eh_admin or eh_desenvolvedor

NOT:
- Inverte o valor booleano
- Sintaxe: not condicao
- Exemplo: not eh_final_de_semana

Precedência: NOT > AND > OR

Dica: Use parênteses para deixar expressões complexas claras!
""")
