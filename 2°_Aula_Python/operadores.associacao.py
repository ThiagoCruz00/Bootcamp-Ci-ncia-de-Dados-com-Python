# ==========================================
# OPERADORES DE ASSOCIAÇÃO EM PYTHON
# ==========================================
# Verificam se um valor existe em uma sequência

# 1. OPERADOR IN
print("=" * 50)
print("1. OPERADOR IN")
print("=" * 50)
print("Verifica se um valor EXISTE em uma sequência")
print()

# Exemplo 1: Lista
frutas = ["maçã", "banana", "laranja", "uva"]

print(f"frutas = {frutas}")
print()

valor = "maçã"
resultado = valor in frutas
print(f"'{valor}' in frutas: {resultado}")  # True

valor = "melancia"
resultado = valor in frutas
print(f"'{valor}' in frutas: {resultado}")  # False
print()

# Exemplo 2: String
palavra = "Python"

print(f"palavra = '{palavra}'")
print()

letra = "P"
resultado = letra in palavra
print(f"'{letra}' in '{palavra}': {resultado}")  # True

letra = "Z"
resultado = letra in palavra
print(f"'{letra}' in '{palavra}': {resultado}")  # False

substring = "Pyt"
resultado = substring in palavra
print(f"'{substring}' in '{palavra}': {resultado}")  # True
print()

# Exemplo 3: Tupla
cores = ("vermelho", "verde", "azul", "amarelo")

print(f"cores = {cores}")
print()

cor = "verde"
resultado = cor in cores
print(f"'{cor}' in cores: {resultado}")  # True

cor = "rosa"
resultado = cor in cores
print(f"'{cor}' in cores: {resultado}")  # False
print()

# Exemplo 4: Dicionário
pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}

print(f"pessoa = {pessoa}")
print()

chave = "nome"
resultado = chave in pessoa
print(f"'{chave}' in pessoa: {resultado}")  # True (verifica chaves)

chave = "João"
resultado = chave in pessoa
print(f"'{chave}' in pessoa: {resultado}")  # False (João é valor, não chave)
print()

# Exemplo 5: Conjunto (set)
numeros = {1, 2, 3, 4, 5}

print(f"numeros = {numeros}")
print()

numero = 3
resultado = numero in numeros
print(f"{numero} in numeros: {resultado}")  # True

numero = 10
resultado = numero in numeros
print(f"{numero} in numeros: {resultado}")  # False
print()

# Exemplo 6: Intervalo (range)
faixa = range(1, 11)

print(f"faixa = range(1, 11)")
print()

numero = 5
resultado = numero in faixa
print(f"{numero} in range(1, 11): {resultado}")  # True

numero = 15
resultado = numero in faixa
print(f"{numero} in range(1, 11): {resultado}")  # False
print()

# ==========================================
# 2. OPERADOR NOT IN
# ==========================================
print("=" * 50)
print("2. OPERADOR NOT IN")
print("=" * 50)
print("Verifica se um valor NÃO EXISTE em uma sequência")
print()

# Exemplo 1: Lista
letras = ["a", "e", "i", "o", "u"]

print(f"letras = {letras}")
print()

letra = "b"
resultado = letra not in letras
print(f"'{letra}' not in letras: {resultado}")  # True

letra = "a"
resultado = letra not in letras
print(f"'{letra}' not in letras: {resultado}")  # False
print()

# Exemplo 2: String
texto = "programação"

print(f"texto = '{texto}'")
print()

caractere = "x"
resultado = caractere not in texto
print(f"'{caractere}' not in '{texto}': {resultado}")  # True

caractere = "p"
resultado = caractere not in texto
print(f"'{caractere}' not in '{texto}': {resultado}")  # False
print()

# Exemplo 3: Número em lista
numeros = [10, 20, 30, 40, 50]

print(f"numeros = {numeros}")
print()

numero = 35
resultado = numero not in numeros
print(f"{numero} not in numeros: {resultado}")  # True

numero = 30
resultado = numero not in numeros
print(f"{numero} not in numeros: {resultado}")  # False
print()

# ==========================================
# OPERADORES IN/NOT IN EM ESTRUTURAS CONDICIONAIS
# ==========================================
print("=" * 50)
print("OPERADORES IN/NOT IN EM ESTRUTURAS CONDICIONAIS")
print("=" * 50)

# Exemplo 1: Verificar acesso
usuarios_autorizados = ["João", "Maria", "Pedro"]
usuario = "Maria"

print(f"usuarios_autorizados = {usuarios_autorizados}")
print(f"usuario = '{usuario}'")
print()

if usuario in usuarios_autorizados:
    print(f"✓ Bem-vindo, {usuario}!")
else:
    print(f"✗ Acesso negado para {usuario}")

print()

# Exemplo 2: Verificar produtos proibidos
produtos_proibidos = ["explosivos", "armas", "drogas"]
compra = "livro"

print(f"produtos_proibidos = {produtos_proibidos}")
print(f"compra = '{compra}'")
print()

if compra not in produtos_proibidos:
    print(f"✓ {compra.capitalize()} pode ser vendido")
else:
    print(f"✗ {compra.capitalize()} não pode ser vendido")

print()

# Exemplo 3: Verificar estação
estacoes_chuvosas = ["dezembro", "janeiro", "fevereiro"]
mes_atual = "julho"

print(f"estacoes_chuvosas = {estacoes_chuvosas}")
print(f"mes_atual = '{mes_atual}'")
print()

if mes_atual not in estacoes_chuvosas:
    print(f"Não está chovendo em {mes_atual}")
else:
    print(f"Está chovendo em {mes_atual}")

print()

# ==========================================
# OPERADORES IN/NOT IN COM LOOPS
# ==========================================
print("=" * 50)
print("OPERADORES IN/NOT IN COM LOOPS")
print("=" * 50)

# Exemplo 1: Verificar se algum valor existe
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
procurado = 7

print(f"numeros = {numeros}")
print(f"procurado = {procurado}")
print()

if procurado in numeros:
    print(f"✓ {procurado} foi encontrado!")
else:
    print(f"✗ {procurado} não foi encontrado")

print()

# Exemplo 2: Verificar valores não permitidos
entrada = "python 123"
caracteres_nao_permitidos = ["@", "#", "$", "%"]

print(f"entrada = '{entrada}'")
print(f"caracteres_nao_permitidos = {caracteres_nao_permitidos}")
print()

tem_caractere_invalido = False
for caractere in caracteres_nao_permitidos:
    if caractere in entrada:
        print(f"✗ Caractere '{caractere}' não permitido encontrado")
        tem_caractere_invalido = True

if not tem_caractere_invalido:
    print(f"✓ Entrada válida")

print()

# ==========================================
# OPERADORES IN/NOT IN COM DICIONÁRIOS
# ==========================================
print("=" * 50)
print("OPERADORES IN/NOT IN COM DICIONÁRIOS")
print("=" * 50)

aluno = {
    "nome": "Carlos",
    "matricula": 12345,
    "media": 8.5,
    "turma": "A"
}

print(f"aluno = {aluno}")
print()

# Verificar se chave existe
print("Verificando chaves:")
chave = "nome"
print(f"'{chave}' in aluno: {chave in aluno}")  # True

chave = "nota"
print(f"'{chave}' in aluno: {chave in aluno}")  # False

print()

# Obter valor com verificação
print("Acessando valores com segurança:")

if "media" in aluno:
    print(f"Média: {aluno['media']}")
else:
    print("Chave 'media' não encontrada")

if "fone" in aluno:
    print(f"Telefone: {aluno['fone']}")
else:
    print("Chave 'fone' não encontrada")

print()

# ==========================================
# DIFERENÇA: IN PARA LISTAS vs IN PARA DICIONÁRIOS
# ==========================================
print("=" * 50)
print("IN PARA LISTAS vs IN PARA DICIONÁRIOS")
print("=" * 50)

# Lista - verifica valores
lista = [1, 2, 3]
print(f"lista = {lista}")
print(f"2 in lista: {2 in lista}")  # True (verifica valor)
print()

# Dicionário - verifica chaves por padrão
dicio = {1: "um", 2: "dois", 3: "três"}
print(f"dicio = {dicio}")
print(f"2 in dicio: {2 in dicio}")  # True (verifica chave)
print(f"'dois' in dicio: {'dois' in dicio}")  # False (não verifica valor)
print()

# Para verificar valores no dicionário
print("Para verificar valores em dicionário:")
print(f"'dois' in dicio.values(): {'dois' in dicio.values()}")  # True
print()

# ==========================================
# DESEMPENHO: IN COM DIFERENTES ESTRUTURAS
# ==========================================
print("=" * 50)
print("DESEMPENHO COM DIFERENTES ESTRUTURAS")
print("=" * 50)

# Listas são lentas para verificar associação
lista = list(range(1, 1000000))
valor = 999999

print(f"Lista com 999.999 elementos")
print(f"{valor} in lista: {valor in lista}")
print()

# Conjuntos são rápidos para verificar associação
conjunto = set(range(1, 1000000))
valor = 999999

print(f"Conjunto com 999.999 elementos")
print(f"{valor} in conjunto: {valor in conjunto}")
print()

print("Dica: Use SET para grandes coleções quando precisar fazer")
print("      verificações frequentes com 'in'")
print()

# ==========================================
# EXEMPLOS PRÁTICOS COMPLETOS
# ==========================================
print("=" * 50)
print("EXEMPLOS PRÁTICOS COMPLETOS")
print("=" * 50)

# Exemplo 1: Sistema de validação de email
print("\nExemplo 1: Validação de domínio de email")
dominios_permitidos = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
email = "usuario@gmail.com"

dominio = email.split("@")[1]
print(f"email = '{email}'")
print(f"dominios_permitidos = {dominios_permitidos}")

if dominio in dominios_permitidos:
    print(f"✓ Domínio '{dominio}' permitido")
else:
    print(f"✗ Domínio '{dominio}' não permitido")

print()

# Exemplo 2: Verificar disponibilidade
print("Exemplo 2: Verificar disponibilidade de nome de usuário")
usuarios_ocupados = ["admin", "root", "user", "test"]
novo_usuario = "python_dev"

print(f"usuarios_ocupados = {usuarios_ocupados}")
print(f"novo_usuario = '{novo_usuario}'")

if novo_usuario not in usuarios_ocupados:
    print(f"✓ '{novo_usuario}' está disponível")
else:
    print(f"✗ '{novo_usuario}' já está em uso")

print()

# Exemplo 3: Filtrar dados
print("Exemplo 3: Filtrar dados inválidos")
dados = ["João Silva", "Maria@123", "Pedro.Costa", "Ana#Santos"]
caracteres_invalidos = ["@", "#", "$", "%"]

print(f"dados = {dados}")
print(f"caracteres_invalidos = {caracteres_invalidos}")
print()

dados_validos = []
for nome in dados:
    eh_valido = True
    for char in caracteres_invalidos:
        if char in nome:
            eh_valido = False
            break
    if eh_valido:
        dados_validos.append(nome)

print("Dados válidos:")
for nome in dados_validos:
    print(f"  ✓ {nome}")

print()

# Exemplo 4: Verificar permissões
print("Exemplo 4: Sistema de permissões")
usuario_permissoes = {
    "João": ["ler", "escrever"],
    "Maria": ["ler", "escrever", "deletar"],
    "Pedro": ["ler"]
}

print(f"usuario_permissoes = {usuario_permissoes}")
print()

usuario = "Maria"
acao = "deletar"

if usuario in usuario_permissoes:
    if acao in usuario_permissoes[usuario]:
        print(f"✓ {usuario} pode '{acao}'")
    else:
        print(f"✗ {usuario} não pode '{acao}'")
else:
    print(f"✗ Usuário '{usuario}' não encontrado")

print()

# ==========================================
# RESUMO DOS OPERADORES DE ASSOCIAÇÃO
# ==========================================
print("=" * 50)
print("RESUMO DOS OPERADORES DE ASSOCIAÇÃO")
print("=" * 50)
print("""
in : Verifica se um valor EXISTE em uma sequência
     Retorna True se o valor for encontrado
     Funciona com: listas, tuplas, strings, conjuntos, dicionários, ranges

not in : Verifica se um valor NÃO EXISTE em uma sequência
         Retorna True se o valor não for encontrado

EXEMPLOS:
- 5 in [1, 2, 3, 4, 5]  →  True
- "a" in "python"  →  False
- "nome" in {"nome": "João", "idade": 25}  →  True
- 10 not in range(1, 10)  →  True

DICAS:
1. Use 'in' para verificar existência antes de acessar
2. Para dicionários, 'in' verifica CHAVES por padrão
3. Use SET em vez de LIST para grandes coleções
   quando fazer verificações frequentes com 'in'
4. Combine com 'if' para estruturas condicionais
""")
