# ==========================================
# FATIAMENTO DE STRING EM PYTHON
# ==========================================
# Slicing permite extrair partes de uma string usando índices

# ==========================================
# 1. INDEXAÇÃO BÁSICA
# ==========================================
print("=" * 50)
print("1. INDEXAÇÃO BÁSICA")
print("=" * 50)

# Exemplo 1: Acessar caractere por índice positivo
print("Exemplo 1: Índices positivos (esquerda para direita)")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"Índices: 0=P, 1=y, 2=t, 3=h, 4=o, 5=n")
print(f"texto[0] = '{texto[0]}'")
print(f"texto[1] = '{texto[1]}'")
print(f"texto[2] = '{texto[2]}'")
print(f"texto[5] = '{texto[5]}'")
print()

# Exemplo 2: Acessar caractere por índice negativo
print("Exemplo 2: Índices negativos (direita para esquerda)")
print(f"Texto: '{texto}'")
print(f"Índices negativos: -6=P, -5=y, -4=t, -3=h, -2=o, -1=n")
print(f"texto[-1] = '{texto[-1]}'  (último caractere)")
print(f"texto[-2] = '{texto[-2]}'")
print(f"texto[-3] = '{texto[-3]}'")
print(f"texto[-6] = '{texto[-6]}'  (primeiro caractere)")
print()

# Exemplo 3: Comprimento da string
print("Exemplo 3: Comprimento da string")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"len(texto) = {len(texto)}")
print(f"Último índice positivo: {len(texto) - 1}")
print()

# ==========================================
# 2. FATIAMENTO SIMPLES (SLICING)
# ==========================================
print("=" * 50)
print("2. FATIAMENTO SIMPLES")
print("=" * 50)

# Exemplo 1: Fatiamento básico [início:fim]
print("Exemplo 1: [início:fim]")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"texto[0:3] = '{texto[0:3]}'  (de 0 até 2, 3 excluído)")
print(f"texto[1:4] = '{texto[1:4]}'  (de 1 até 3)")
print(f"texto[2:5] = '{texto[2:5]}'  (de 2 até 4)")
print()

# Exemplo 2: Fatiamento do início
print("Exemplo 2: Do início [:fim]")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"texto[:3] = '{texto[:3]}'  (do início até índice 2)")
print(f"texto[:2] = '{texto[:2]}'")
print(f"texto[:1] = '{texto[:1]}'")
print()

# Exemplo 3: Fatiamento até o fim
print("Exemplo 3: Do início até o fim [início:]")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"texto[3:] = '{texto[3:]}'  (de índice 3 até o fim)")
print(f"texto[2:] = '{texto[2:]}'")
print(f"texto[1:] = '{texto[1:]}'")
print()

# Exemplo 4: String inteira
print("Exemplo 4: String inteira [:]")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"texto[:] = '{texto[:]}'  (cópia da string)")
print()

# Exemplo 5: Fatiamento com índices negativos
print("Exemplo 5: Fatiamento com índices negativos")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"texto[-3:] = '{texto[-3:]}'  (últimos 3 caracteres)")
print(f"texto[:-3] = '{texto[:-3]}'  (excluindo últimos 3)")
print(f"texto[-4:-1] = '{texto[-4:-1]}'  (do -4 até -2)")
print()

# ==========================================
# 3. FATIAMENTO COM PASSO
# ==========================================
print("=" * 50)
print("3. FATIAMENTO COM PASSO [início:fim:passo]")
print("=" * 50)

# Exemplo 1: Passo 2
print("Exemplo 1: Passo 2")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"texto[::2] = '{texto[::2]}'  (cada 2 caracteres)")
print(f"texto[0:6:2] = '{texto[0:6:2]}'  (explícito)")
print()

# Exemplo 2: Passo 3
print("Exemplo 2: Passo 3")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"texto[::3] = '{texto[::3]}'  (cada 3 caracteres)")
print()

# Exemplo 3: Começar em índice 1 com passo 2
print("Exemplo 3: Começar em 1, passo 2")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"texto[1::2] = '{texto[1::2]}'")
print()

# Exemplo 4: Passo negativo (reverter)
print("Exemplo 4: Passo negativo (reverter string)")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"texto[::-1] = '{texto[::-1]}'  (string reversa)")
print()

# Exemplo 5: Passo -2 (reverter pulando 1)
print("Exemplo 5: Passo -2 (reverter pulando 1)")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"texto[::-2] = '{texto[::-2]}'")
print()

# Exemplo 6: Passo -3 (reverter pulando 2)
print("Exemplo 6: Passo -3")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"texto[::-3] = '{texto[::-3]}'")
print()

# ==========================================
# 4. EXEMPLOS COM PALAVRAS E FRASES
# ==========================================
print("=" * 50)
print("4. EXEMPLOS COM PALAVRAS E FRASES")
print("=" * 50)

# Exemplo 1: Primeira e última letra
print("Exemplo 1: Primeira e última letra")
palavra = "Hello"
print(f"Palavra: '{palavra}'")
print(f"Primeira letra: {palavra[0]}")
print(f"Última letra: {palavra[-1]}")
print()

# Exemplo 2: Primeiras e últimas letras
print("Exemplo 2: Primeiras e últimas letras")
palavra = "Hello"
print(f"Palavra: '{palavra}'")
print(f"Primeiras 2: {palavra[:2]}")
print(f"Últimas 2: {palavra[-2:]}")
print(f"Primeiras 3 e últimas 3: {palavra[:3]} ... {palavra[-3:]}")
print()

# Exemplo 3: Meio da palavra
print("Exemplo 3: Meio da palavra")
palavra = "Python"
meio = len(palavra) // 2
print(f"Palavra: '{palavra}'")
print(f"Primeira metade: {palavra[:meio]}")
print(f"Segunda metade: {palavra[meio:]}")
print()

# Exemplo 4: Extrair domínio de email
print("Exemplo 4: Extrair domínio de email")
email = "usuario@example.com"
print(f"Email: {email}")
arroba = email.index("@")
dominio = email[arroba+1:]
print(f"Domínio: {dominio}")
print()

# Exemplo 5: Extrair nome de arquivo
print("Exemplo 5: Extrair nome de arquivo")
caminho = "/home/usuario/documento.txt"
barra = caminho.rfind("/")
nome_arquivo = caminho[barra+1:]
print(f"Caminho: {caminho}")
print(f"Nome do arquivo: {nome_arquivo}")
print()

# ==========================================
# 5. EXEMPLOS COM DATA E HORA
# ==========================================
print("=" * 50)
print("5. EXEMPLOS COM DATA E HORA")
print("=" * 50)

# Exemplo 1: Extrair partes de data (formato: DD/MM/YYYY)
print("Exemplo 1: Extrair partes de data")
data = "25/12/2024"
print(f"Data: {data}")
dia = data[0:2]
mes = data[3:5]
ano = data[6:10]
print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")
print()

# Exemplo 2: Extrair partes de hora (formato: HH:MM:SS)
print("Exemplo 2: Extrair partes de hora")
hora = "14:30:45"
print(f"Hora: {hora}")
horas = hora[0:2]
minutos = hora[3:5]
segundos = hora[6:8]
print(f"Horas: {horas}, Minutos: {minutos}, Segundos: {segundos}")
print()

# Exemplo 3: Extrair ano de uma data completa
print("Exemplo 3: Extrair ano")
data_completa = "São Paulo, 25 de Dezembro de 2024"
ano = data_completa[-4:]
print(f"Data completa: {data_completa}")
print(f"Ano: {ano}")
print()

# ==========================================
# 6. EXEMPLOS COM NÚMEROS DE TELEFONE
# ==========================================
print("=" * 50)
print("6. EXEMPLOS COM NÚMEROS DE TELEFONE")
print("=" * 50)

# Exemplo 1: Formatar telefone
print("Exemplo 1: Formatar telefone")
telefone = "11987654321"
print(f"Telefone sem formato: {telefone}")
formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
print(f"Telefone formatado: {formatado}")
print()

# Exemplo 2: Extrair DDD
print("Exemplo 2: Extrair DDD (Discagem Direta à Distância)")
telefone = "11987654321"
ddd = telefone[:2]
numero = telefone[2:]
print(f"Telefone: {telefone}")
print(f"DDD: {ddd}")
print(f"Número: {numero}")
print()

# ==========================================
# 7. EXEMPLOS COM CÓDIGO
# ==========================================
print("=" * 50)
print("7. EXEMPLOS COM CÓDIGO")
print("=" * 50)

# Exemplo 1: Extrair prefixo de função
print("Exemplo 1: Extrair prefixo de função")
funcao = "get_user_name"
print(f"Função: {funcao}")
prefixo = funcao[:3]
sufixo = funcao[4:]
print(f"Prefixo: {prefixo}")
print(f"Sufixo (sem underscore): {sufixo}")
print()

# Exemplo 2: Converter camelCase (simulado com slicing)
print("Exemplo 2: Analisar estrutura")
variavel = "myVariableName"
print(f"Variável: {variavel}")
print(f"Primeira letra: {variavel[0]}")
print(f"Resto: {variavel[1:]}")
print()

# ==========================================
# 8. EXEMPLOS COM STRINGS ESPECIAIS
# ==========================================
print("=" * 50)
print("8. EXEMPLOS COM STRINGS ESPECIAIS")
print("=" * 50)

# Exemplo 1: Remover caracteres especiais no início/fim
print("Exemplo 1: Remover caracteres especiais")
texto = "***Python***"
print(f"Original: '{texto}'")
print(f"Sem asteriscos: '{texto[3:-3]}'")
print()

# Exemplo 2: Extrair entre delimitadores
print("Exemplo 2: Extrair entre delimitadores")
texto = "<tag>Conteúdo</tag>"
inicio = texto.index(">") + 1
fim = texto.index("</")
conteudo = texto[inicio:fim]
print(f"Original: '{texto}'")
print(f"Conteúdo: '{conteudo}'")
print()

# Exemplo 3: Inverter linha de texto
print("Exemplo 3: Inverter linha de texto")
texto = "Python é incrível"
invertido = texto[::-1]
print(f"Original: '{texto}'")
print(f"Invertido: '{invertido}'")
print()

# ==========================================
# 9. COMPARAÇÃO: SLICING vs MÉTODOS
# ==========================================
print("=" * 50)
print("9. COMPARAÇÃO: SLICING vs MÉTODOS")
print("=" * 50)

texto = "  Python  "

print(f"Texto original: '{texto}'")
print()

# Remover espaços
print("Remover espaços:")
print(f"Com slicing: '{texto.strip()}'")
print(f"Alternativa: '{texto[2:-2]}'")
print()

# Extrair primeiros 3 caracteres
print("Primeiros 3 caracteres (após strip):")
print(f"Com slicing: '{texto.strip()[:3]}'")
print()

# Contar caracteres
print("Verificar comprimento:")
texto_limpo = "Python"
print(f"len('{texto_limpo}') = {len(texto_limpo)}")
print()

# ==========================================
# 10. EXEMPLOS PRÁTICOS COMPLETOS
# ==========================================
print("=" * 50)
print("10. EXEMPLOS PRÁTICOS COMPLETOS")
print("=" * 50)

# Exemplo 1: Validar formato de CPF
print("\nExemplo 1: Analisar CPF (formato XXX.XXX.XXX-XX)")
print("-" * 40)
cpf = "123.456.789-00"
print(f"CPF: {cpf}")
partes = cpf.split(".")
ultimos = partes[2][3:]
print(f"Primeiros 3 dígitos: {cpf[:3]}")
print(f"Dígitos verificadores: {cpf[-2:]}")
print()

# Exemplo 2: Processar código de barra
print("Exemplo 2: Processar código de barra")
print("-" * 40)
codigo = "5901234123457"
print(f"Código: {codigo}")
print(f"País: {codigo[:2]}")
print(f"Fabricante: {codigo[2:7]}")
print(f"Produto: {codigo[7:12]}")
print(f"Verificação: {codigo[12]}")
print()

# Exemplo 3: Analisar URL
print("Exemplo 3: Analisar URL")
print("-" * 40)
url = "https://www.example.com/path/to/page"
protocolo_fim = url.index("://")
protocolo = url[:protocolo_fim]
resto = url[protocolo_fim+3:]
barra = resto.index("/")
dominio = resto[:barra]
caminho = resto[barra:]
print(f"URL: {url}")
print(f"Protocolo: {protocolo}")
print(f"Domínio: {dominio}")
print(f"Caminho: {caminho}")
print()

# Exemplo 4: Extrair informações de arquivo
print("Exemplo 4: Informações de arquivo")
print("-" * 40)
arquivo = "documento_importante_v2.pdf"
print(f"Arquivo: {arquivo}")
ponto = arquivo.rfind(".")
nome = arquivo[:ponto]
extensao = arquivo[ponto+1:]
print(f"Nome: {nome}")
print(f"Extensão: {extensao}")
print()

# Exemplo 5: Processar código de produto
print("Exemplo 5: Processar código de produto")
print("-" * 40)
codigo_produto = "ELETRO2024NOTEBOOKDELL001"
print(f"Código: {codigo_produto}")
print(f"Categoria: {codigo_produto[:6]}")
print(f"Ano: {codigo_produto[6:10]}")
print(f"Tipo: {codigo_produto[10:18]}")
print(f"Marca: {codigo_produto[18:22]}")
print(f"Sequencial: {codigo_produto[22:]}")
print()

# ==========================================
# 11. CASOS ESPECIAIS E ARMADILHAS
# ==========================================
print("=" * 50)
print("11. CASOS ESPECIAIS E ARMADILHAS")
print("=" * 50)

# Exemplo 1: Índice fora do intervalo com slicing
print("Exemplo 1: Índice fora do intervalo")
texto = "Python"
print(f"Texto: '{texto}'")
print(f"texto[0:100] = '{texto[0:100]}'  (não gera erro!)")
print(f"texto[10:20] = '{texto[10:20]}'  (vazio, não gera erro!)")
print()

# Exemplo 2: Diferença entre slicing e indexação
print("Exemplo 2: Diferença entre [] e [:]")
texto = "Python"
print(f"Texto: '{texto}'")
try:
    print(f"texto[10] = gera erro!")
except IndexError:
    print("  IndexError: string index out of range")
print(f"texto[10:20] = '{texto[10:20]}'  (sem erro, resultado vazio)")
print()

# Exemplo 3: Modificação de strings
print("Exemplo 3: Strings são imutáveis!")
texto = "Python"
print(f"Texto original: '{texto}'")
# texto[0] = 'J'  # ERRO! Strings não podem ser modificadas
novo_texto = 'J' + texto[1:]
print(f"Novo texto: '{novo_texto}'")
print()

# ==========================================
# 12. RESUMO E DICAS
# ==========================================
print("=" * 50)
print("12. RESUMO E DICAS")
print("=" * 50)
print("""
SINTAXE BÁSICA:
string[início:fim:passo]

PARTES OPCIONAIS:
- início: índice inicial (padrão: 0)
- fim: índice final (excluído)
- passo: incremento entre índices (padrão: 1)

INDEXAÇÃO:
- Positiva: 0, 1, 2, 3, ...
- Negativa: -1, -2, -3, ...
- -1 é o último caractere

EXEMPLOS COMUNS:
string[0]           - Primeiro caractere
string[-1]          - Último caractere
string[:3]          - Primeiros 3 caracteres
string[-3:]         - Últimos 3 caracteres
string[1:-1]        - Excluindo primeiro e último
string[::-1]        - String invertida
string[::2]         - Cada 2 caracteres
string[1::2]        - Começando em 1, cada 2

DICAS:
1. Slicing não gera erro com índices fora do intervalo
2. Strings são IMUTÁVEIS - não pode modificar diretamente
3. Slicing retorna uma nova string
4. O índice final é EXCLUÍDO do resultado
5. Use índices negativos para contar do fim
6. Combine slicing com outros métodos de string

COMPARAÇÃO COM MÉTODOS:
string.upper()      - Converter para maiúscula
string.split()      - Dividir em lista
string.replace()    - Substituir texto
string.strip()      - Remover espaços
string.find()       - Encontrar posição

PERFORMANCE:
- Slicing é rápido
- Use slicing para extrair partes
- Use métodos de string para transformações
""")
