# ==========================================
# MÉTODOS ÚTEIS DA CLASSE STRING EM PYTHON
# ==========================================

# ==========================================
# 1. MÉTODOS DE TRANSFORMAÇÃO
# ==========================================
print("=" * 50)
print("1. MÉTODOS DE TRANSFORMAÇÃO")
print("=" * 50)

# Exemplo 1: upper() - Converter para maiúscula
print("Exemplo 1: upper() - Converter para maiúscula")
texto = "python"
resultado = texto.upper()
print(f"Original: {texto}")
print(f"Resultado: {resultado}")
print()

# Exemplo 2: lower() - Converter para minúscula
print("Exemplo 2: lower() - Converter para minúscula")
texto = "PYTHON"
resultado = texto.lower()
print(f"Original: {texto}")
print(f"Resultado: {resultado}")
print()

# Exemplo 3: title() - Primeira letra de cada palavra maiúscula
print("Exemplo 3: title() - Primeira letra maiúscula")
texto = "olá mundo python"
resultado = texto.title()
print(f"Original: {texto}")
print(f"Resultado: {resultado}")
print()

# Exemplo 4: capitalize() - Primeira letra maiúscula, resto minúscula
print("Exemplo 4: capitalize() - Primeira letra maiúscula")
texto = "olá MUNDO"
resultado = texto.capitalize()
print(f"Original: {texto}")
print(f"Resultado: {resultado}")
print()

# Exemplo 5: swapcase() - Trocar maiúscula por minúscula
print("Exemplo 5: swapcase() - Inverter maiúscula/minúscula")
texto = "PytHon MunDo"
resultado = texto.swapcase()
print(f"Original: {texto}")
print(f"Resultado: {resultado}")
print()

# ==========================================
# 2. MÉTODOS DE BUSCA E VERIFICAÇÃO
# ==========================================
print("=" * 50)
print("2. MÉTODOS DE BUSCA E VERIFICAÇÃO")
print("=" * 50)

# Exemplo 1: find() - Encontrar posição (retorna -1 se não encontrar)
print("Exemplo 1: find() - Encontrar posição")
texto = "Python é incrível"
print(f"Texto: '{texto}'")
print(f"find('é'): {texto.find('é')}")
print(f"find('Python'): {texto.find('Python')}")
print(f"find('xyz'): {texto.find('xyz')}")  # Retorna -1
print()

# Exemplo 2: index() - Encontrar posição (levanta erro se não encontrar)
print("Exemplo 2: index() - Encontrar posição")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"index('P'): {texto.index('P')}")
print(f"index('o'): {texto.index('o')}")
# print(f"index('xyz'): {texto.index('xyz')}")  # Levanta ValueError
print()

# Exemplo 3: count() - Contar ocorrências
print("Exemplo 3: count() - Contar ocorrências")
texto = "banana"
print(f"Texto: '{texto}'")
print(f"count('a'): {texto.count('a')}")
print(f"count('n'): {texto.count('n')}")
print(f"count('z'): {texto.count('z')}")
print()

# Exemplo 4: startswith() - Verifica se começa com
print("Exemplo 4: startswith() - Verifica se começa com")
texto = "Python é incrível"
print(f"Texto: '{texto}'")
print(f"startswith('Python'): {texto.startswith('Python')}")
print(f"startswith('Java'): {texto.startswith('Java')}")
print()

# Exemplo 5: endswith() - Verifica se termina com
print("Exemplo 5: endswith() - Verifica se termina com")
texto = "arquivo.txt"
print(f"Texto: '{texto}'")
print(f"endswith('.txt'): {texto.endswith('.txt')}")
print(f"endswith('.py'): {texto.endswith('.py')}")
print()

# Exemplo 6: in - Operador de verificação
print("Exemplo 6: in - Operador de verificação")
texto = "Python é incrível"
print(f"Texto: '{texto}'")
print(f"'Python' in texto: {'Python' in texto}")
print(f"'Java' in texto: {'Java' in texto}")
print()

# ==========================================
# 3. MÉTODOS DE LIMPEZA
# ==========================================
print("=" * 50)
print("3. MÉTODOS DE LIMPEZA")
print("=" * 50)

# Exemplo 1: strip() - Remove espaços das extremidades
print("Exemplo 1: strip() - Remove espaços das extremidades")
texto = "  Python  "
print(f"Original: '{texto}'")
print(f"strip(): '{texto.strip()}'")
print()

# Exemplo 2: lstrip() - Remove espaços da esquerda
print("Exemplo 2: lstrip() - Remove espaços da esquerda")
texto = "  Python  "
print(f"Original: '{texto}'")
print(f"lstrip(): '{texto.lstrip()}'")
print()

# Exemplo 3: rstrip() - Remove espaços da direita
print("Exemplo 3: rstrip() - Remove espaços da direita")
texto = "  Python  "
print(f"Original: '{texto}'")
print(f"rstrip(): '{texto.rstrip()}'")
print()

# Exemplo 4: strip() com caracteres específicos
print("Exemplo 4: strip() com caracteres específicos")
texto = "###Python###"
print(f"Original: '{texto}'")
print(f"strip('#'): '{texto.strip('#')}'")
print()

# Exemplo 5: removeprefix() e removesuffix() (Python 3.9+)
print("Exemplo 5: removeprefix() e removesuffix()")
texto = "prefixo_Python_sufixo"
print(f"Original: '{texto}'")
try:
    print(f"removeprefix('prefixo_'): '{texto.removeprefix('prefixo_')}'")
    print(f"removesuffix('_sufixo'): '{texto.removesuffix('_sufixo')}'")
except AttributeError:
    print("removeprefix e removesuffix requerem Python 3.9+")
print()

# ==========================================
# 4. MÉTODOS DE SUBSTITUIÇÃO
# ==========================================
print("=" * 50)
print("4. MÉTODOS DE SUBSTITUIÇÃO")
print("=" * 50)

# Exemplo 1: replace() - Substituir ocorrências
print("Exemplo 1: replace() - Substituir ocorrências")
texto = "Python é incrível. Python é poderoso."
print(f"Original: '{texto}'")
resultado = texto.replace("Python", "JavaScript")
print(f"replace('Python', 'JavaScript'): '{resultado}'")
print()

# Exemplo 2: replace() com limite
print("Exemplo 2: replace() com limite de substituições")
texto = "Python Python Python"
print(f"Original: '{texto}'")
resultado = texto.replace("Python", "Java", 2)
print(f"replace('Python', 'Java', 2): '{resultado}'")
print()

# ==========================================
# 5. MÉTODOS DE DIVISÃO E JUNÇÃO
# ==========================================
print("=" * 50)
print("5. MÉTODOS DE DIVISÃO E JUNÇÃO")
print("=" * 50)

# Exemplo 1: split() - Dividir em lista
print("Exemplo 1: split() - Dividir em lista")
texto = "Python Java JavaScript"
resultado = texto.split()
print(f"Original: '{texto}'")
print(f"split(): {resultado}")
print()

# Exemplo 2: split() com separador específico
print("Exemplo 2: split() com separador específico")
texto = "João,Maria,Pedro,Ana"
resultado = texto.split(",")
print(f"Original: '{texto}'")
print(f"split(','): {resultado}")
print()

# Exemplo 3: split() com limite
print("Exemplo 3: split() com limite")
texto = "a-b-c-d-e"
resultado = texto.split("-", 2)
print(f"Original: '{texto}'")
print(f"split('-', 2): {resultado}")
print()

# Exemplo 4: splitlines() - Dividir por quebra de linha
print("Exemplo 4: splitlines() - Dividir por quebra de linha")
texto = "Linha 1\nLinha 2\nLinha 3"
resultado = texto.splitlines()
print(f"Original: '{texto}'")
print(f"splitlines(): {resultado}")
print()

# Exemplo 5: join() - Juntar lista em string
print("Exemplo 5: join() - Juntar lista em string")
lista = ["Python", "Java", "JavaScript"]
resultado = ", ".join(lista)
print(f"Lista: {lista}")
print(f"', '.join(lista): '{resultado}'")
print()

# Exemplo 6: join() com diferentes separadores
print("Exemplo 6: join() com diferentes separadores")
lista = ["A", "B", "C"]
print(f"Lista: {lista}")
print(f"' '.join(lista): '{' '.join(lista)}'")
print(f"'-'.join(lista): '{'-'.join(lista)}'")
print(f"''.join(lista): '{'' .join(lista)}'")
print()

# ==========================================
# 6. MÉTODOS DE VERIFICAÇÃO
# ==========================================
print("=" * 50)
print("6. MÉTODOS DE VERIFICAÇÃO")
print("=" * 50)

# Exemplo 1: isdigit() - Verifica se contém apenas dígitos
print("Exemplo 1: isdigit() - Verifica se contém apenas dígitos")
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'12a'.isdigit(): {'12a'.isdigit()}")
print(f"''.isdigit(): {''.isdigit()}")
print()

# Exemplo 2: isalpha() - Verifica se contém apenas letras
print("Exemplo 2: isalpha() - Verifica se contém apenas letras")
print(f"'Python'.isalpha(): {'Python'.isalpha()}")
print(f"'Python3'.isalpha(): {'Python3'.isalpha()}")
print(f"'Pythön'.isalpha(): {'Pythön'.isalpha()}")
print()

# Exemplo 3: isalnum() - Verifica se contém apenas letras e números
print("Exemplo 3: isalnum() - Verifica se contém apenas letras e números")
print(f"'Python3'.isalnum(): {'Python3'.isalnum()}")
print(f"'Python-3'.isalnum(): {'Python-3'.isalnum()}")
print()

# Exemplo 4: isspace() - Verifica se contém apenas espaços
print("Exemplo 4: isspace() - Verifica se contém apenas espaços")
print(f"'   '.isspace(): {'   '.isspace()}")
print(f"'Python'.isspace(): {'Python'.isspace()}")
print()

# Exemplo 5: islower() - Verifica se contém apenas minúsculas
print("Exemplo 5: islower() - Verifica se contém apenas minúsculas")
print(f"'python'.islower(): {'python'.islower()}")
print(f"'Python'.islower(): {'Python'.islower()}")
print()

# Exemplo 6: isupper() - Verifica se contém apenas maiúsculas
print("Exemplo 6: isupper() - Verifica se contém apenas maiúsculas")
print(f"'PYTHON'.isupper(): {'PYTHON'.isupper()}")
print(f"'Python'.isupper(): {'Python'.isupper()}")
print()

# Exemplo 7: istitle() - Verifica se está em formato título
print("Exemplo 7: istitle() - Verifica se está em formato título")
print(f"'Python Programming'.istitle(): {'Python Programming'.istitle()}")
print(f"'python programming'.istitle(): {'python programming'.istitle()}")
print()

# ==========================================
# 7. MÉTODOS DE FORMATAÇÃO
# ==========================================
print("=" * 50)
print("7. MÉTODOS DE FORMATAÇÃO")
print("=" * 50)

# Exemplo 1: format() - Formatação básica
print("Exemplo 1: format() - Formatação básica")
texto = "Olá, {}! Bem-vindo!"
resultado = texto.format("João")
print(f"Original: '{texto}'")
print(f"Resultado: '{resultado}'")
print()

# Exemplo 2: format() com múltiplos valores
print("Exemplo 2: format() com múltiplos valores")
texto = "{} tem {} anos e mora em {}."
resultado = texto.format("Maria", 25, "São Paulo")
print(f"Original: '{texto}'")
print(f"Resultado: '{resultado}'")
print()

# Exemplo 3: format() com índices
print("Exemplo 3: format() com índices")
texto = "{0} {1} {0}"
resultado = texto.format("Python", "Java")
print(f"Original: '{texto}'")
print(f"Resultado: '{resultado}'")
print()

# Exemplo 4: format() com chaves nomeadas
print("Exemplo 4: format() com chaves nomeadas")
texto = "{nome} tem {idade} anos"
resultado = texto.format(nome="Pedro", idade=30)
print(f"Original: '{texto}'")
print(f"Resultado: '{resultado}'")
print()

# Exemplo 5: f-strings (formatação moderna)
print("Exemplo 5: f-strings - Formatação moderna")
nome = "Ana"
idade = 28
texto = f"{nome} tem {idade} anos"
print(f"Resultado: '{texto}'")
print()

# Exemplo 6: f-strings com expressões
print("Exemplo 6: f-strings com expressões")
a = 10
b = 5
print(f"{a} + {b} = {a + b}")
print(f"{a} × {b} = {a * b}")
print()

# Exemplo 7: f-strings com formatação numérica
print("Exemplo 7: f-strings com formatação numérica")
pi = 3.14159
print(f"Pi com 2 casas: {pi:.2f}")
print(f"Pi com 4 casas: {pi:.4f}")
print()

# ==========================================
# 8. MÉTODOS DE ALINHAMENTO
# ==========================================
print("=" * 50)
print("8. MÉTODOS DE ALINHAMENTO")
print("=" * 50)

# Exemplo 1: center() - Centralizar
print("Exemplo 1: center() - Centralizar")
texto = "Python"
resultado = texto.center(20)
print(f"Original: '{texto}'")
print(f"center(20): '{resultado}'")
print(f"center(20, '-'): '{texto.center(20, '-')}'")
print()

# Exemplo 2: ljust() - Alinhar à esquerda
print("Exemplo 2: ljust() - Alinhar à esquerda")
texto = "Python"
resultado = texto.ljust(20)
print(f"Original: '{texto}'")
print(f"ljust(20): '{resultado}'")
print(f"ljust(20, '-'): '{texto.ljust(20, '-')}'")
print()

# Exemplo 3: rjust() - Alinhar à direita
print("Exemplo 3: rjust() - Alinhar à direita")
texto = "Python"
resultado = texto.rjust(20)
print(f"Original: '{texto}'")
print(f"rjust(20): '{resultado}'")
print(f"rjust(20, '-'): '{texto.rjust(20, '-')}'")
print()

# Exemplo 4: zfill() - Preencher com zeros
print("Exemplo 4: zfill() - Preencher com zeros")
texto = "123"
resultado = texto.zfill(5)
print(f"Original: '{texto}'")
print(f"zfill(5): '{resultado}'")
print(f"'-123'.zfill(5): '{'-123'.zfill(5)}'")
print()

# ==========================================
# 9. OUTROS MÉTODOS ÚTEIS
# ==========================================
print("=" * 50)
print("9. OUTROS MÉTODOS ÚTEIS")
print("=" * 50)

# Exemplo 1: len() - Comprimento
print("Exemplo 1: len() - Comprimento da string")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"len(texto): {len(texto)}")
print()

# Exemplo 2: Indexação - Acessar caractere
print("Exemplo 2: Indexação - Acessar caractere")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"texto[0]: '{texto[0]}'")
print(f"texto[5]: '{texto[5]}'")
print(f"texto[-1]: '{texto[-1]}'")
print()

# Exemplo 3: Slicing - Fatia de string
print("Exemplo 3: Slicing - Fatia de string")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"texto[0:3]: '{texto[0:3]}'")
print(f"texto[3:]: '{texto[3:]}'")
print(f"texto[:3]: '{texto[:3]}'")
print()

# ==========================================
# 10. EXEMPLOS PRÁTICOS COMPLETOS
# ==========================================
print("=" * 50)
print("10. EXEMPLOS PRÁTICOS COMPLETOS")
print("=" * 50)

# Exemplo 1: Validar email
print("\nExemplo 1: Validar email")
print("-" * 40)
def validar_email(email):
    return "@" in email and "." in email and email.count("@") == 1

emails = ["user@example.com", "user@", "user.example.com"]
for email in emails:
    valido = validar_email(email)
    print(f"{email}: {'✓ Válido' if valido else '✗ Inválido'}")

print()

# Exemplo 2: Extrair nome de arquivo
print("Exemplo 2: Extrair nome de arquivo")
print("-" * 40)
caminho = "/home/usuario/documentos/arquivo.txt"
nome_arquivo = caminho.split("/")[-1]
nome_sem_extensao = nome_arquivo.split(".")[0]
extensao = nome_arquivo.split(".")[-1]

print(f"Caminho: {caminho}")
print(f"Nome arquivo: {nome_arquivo}")
print(f"Sem extensão: {nome_sem_extensao}")
print(f"Extensão: {extensao}")

print()

# Exemplo 3: Processar lista CSV
print("Exemplo 3: Processar dados CSV")
print("-" * 40)
dados = "João,25,São Paulo\nMaria,30,Rio\nPedro,28,BH"
linhas = dados.split("\n")

print("Dados:")
for linha in linhas:
    partes = linha.split(",")
    nome, idade, cidade = partes
    print(f"  {nome.strip()}: {idade.strip()} anos de {cidade.strip()}")

print()

# Exemplo 4: Formatar tabela
print("Exemplo 4: Formatar tabela")
print("-" * 40)
dados = [
    ("Nome", "Idade", "Cidade"),
    ("João", "25", "SP"),
    ("Maria", "30", "RJ"),
    ("Pedro", "28", "BH")
]

for linha in dados:
    nome, idade, cidade = linha
    print(f"{nome.ljust(10)} {idade.rjust(5)} {cidade.rjust(10)}")

print()

# Exemplo 5: Converter case (camelCase para snake_case)
print("Exemplo 5: Converter camelCase para snake_case")
print("-" * 40)
def camel_to_snake(texto):
    resultado = ""
    for i, char in enumerate(texto):
        if char.isupper() and i > 0:
            resultado += "_" + char.lower()
        else:
            resultado += char
    return resultado

exemplos = ["meuNome", "usuarioId", "dataCriacao"]
for exemplo in exemplos:
    print(f"{exemplo} → {camel_to_snake(exemplo)}")

print()

# Exemplo 6: Contar palavras
print("Exemplo 6: Contar palavras em um texto")
print("-" * 40)
texto = "Python é incrível Python é poderoso"
palavras = texto.split()
print(f"Texto: '{texto}'")
print(f"Total de palavras: {len(palavras)}")
print(f"Palavras únicas: {len(set(palavras))}")

# Contar cada palavra
for palavra in set(palavras):
    count = texto.count(palavra)
    print(f"  '{palavra}': {count}x")

print()

# ==========================================
# 11. RESUMO DOS MÉTODOS MAIS ÚTEIS
# ==========================================
print("=" * 50)
print("11. RESUMO DOS MÉTODOS MAIS ÚTEIS")
print("=" * 50)
print("""
TRANSFORMAÇÃO:
- upper()          : Converter para MAIÚSCULA
- lower()          : Converter para minúscula
- title()          : Primeira Letra De Cada Palavra
- capitalize()     : Primeira letra maiúscula
- swapcase()       : Inverter maiúscula/minúscula

BUSCA:
- find(sub)        : Encontrar posição (retorna -1 se não encontrar)
- index(sub)       : Encontrar posição (erro se não encontrar)
- count(sub)       : Contar ocorrências
- startswith(pre)  : Verifica se começa com
- endswith(suf)    : Verifica se termina com

LIMPEZA:
- strip()          : Remove espaços das extremidades
- lstrip()         : Remove espaços da esquerda
- rstrip()         : Remove espaços da direita
- replace(old, new): Substituir texto

DIVISÃO/JUNÇÃO:
- split(sep)       : Dividir em lista
- splitlines()     : Dividir por quebra de linha
- join(lista)      : Juntar lista em string

VERIFICAÇÃO:
- isdigit()        : Contém apenas dígitos?
- isalpha()        : Contém apenas letras?
- isalnum()        : Contém apenas letras/números?
- islower()        : Contém apenas minúsculas?
- isupper()        : Contém apenas maiúsculas?

FORMATAÇÃO:
- format()         : Formatação com placeholders
- f-string         : Formatação moderna (Python 3.6+)

ALINHAMENTO:
- center(width)    : Centralizar
- ljust(width)     : Alinhar à esquerda
- rjust(width)     : Alinhar à direita
- zfill(width)     : Preencher com zeros

ACESSO:
- [indice]         : Acessar caractere por índice
- [inicio:fim]     : Fatia de string
- len()            : Comprimento da string
""")
