# ==========================================
# STRINGS COM MÚLTIPLAS LINHAS EM PYTHON
# ==========================================

# ==========================================
# 1. ASPAS TRIPLAS DUPLAS (""" """)
# ==========================================
print("=" * 50)
print("1. ASPAS TRIPLAS DUPLAS")
print("=" * 50)

# Exemplo 1: String com múltiplas linhas básica
print("Exemplo 1: String básica com múltiplas linhas")
texto = """Linha 1
Linha 2
Linha 3"""

print(texto)
print()

# Exemplo 2: Preservar indentação
print("Exemplo 2: Preservar indentação")
texto = """
    Nome: João
    Idade: 25
    Cidade: São Paulo
"""

print(texto)
print()

# Exemplo 3: String com quebras de linha vazias
print("Exemplo 3: Com linhas vazias")
texto = """Primeira linha

Segunda linha
Terceira linha"""

print(texto)
print()

# Exemplo 4: String com aspas simples dentro
print("Exemplo 4: String com aspas simples")
texto = """O programa disse: 'Olá mundo'
E continuou executando"""

print(texto)
print()

# Exemplo 5: String com aspas duplas dentro
print("Exemplo 5: String com aspas duplas")
texto = '''Ele disse "Python é incrível"
Eu concordei'''

print(texto)
print()

# ==========================================
# 2. ASPAS TRIPLAS SIMPLES (''' ''')
# ==========================================
print("=" * 50)
print("2. ASPAS TRIPLAS SIMPLES")
print("=" * 50)

# Exemplo 1: String com aspas triplas simples
print("Exemplo 1: Aspas triplas simples")
texto = '''Primeira linha
Segunda linha
Terceira linha'''

print(texto)
print()

# Exemplo 2: Aspas duplas dentro de aspas triplas simples
print("Exemplo 2: Aspas duplas dentro")
texto = '''
Título: "Aprendendo Python"
Autor: "João Silva"
'''

print(texto)
print()

# ==========================================
# 3. ESCAPE DE QUEBRA DE LINHA (\n)
# ==========================================
print("=" * 50)
print("3. ESCAPE DE QUEBRA DE LINHA (\\n)")
print("=" * 50)

# Exemplo 1: Usando \n em string simples
print("Exemplo 1: \\n em string simples")
texto = "Linha 1\nLinha 2\nLinha 3"
print(texto)
print()

# Exemplo 2: Comparar com aspas triplas
print("Exemplo 2: Equivalência")
texto1 = "Linha 1\nLinha 2\nLinha 3"
texto2 = """Linha 1
Linha 2
Linha 3"""

print("Com \\n:")
print(texto1)
print("\nCom aspas triplas:")
print(texto2)
print("\nSão iguais?", texto1 == texto2)
print()

# ==========================================
# 4. CONCATENAÇÃO DE MÚLTIPLAS LINHAS
# ==========================================
print("=" * 50)
print("4. CONCATENAÇÃO DE MÚLTIPLAS LINHAS")
print("=" * 50)

# Exemplo 1: Concatenar strings com +
print("Exemplo 1: Concatenar com +")
linha1 = "Primeira parte\n"
linha2 = "Segunda parte\n"
linha3 = "Terceira parte"
texto = linha1 + linha2 + linha3

print(texto)
print()

# Exemplo 2: Usar parênteses para quebrar linha no código
print("Exemplo 2: Quebra de linha no código com parênteses")
texto = ("Esta é uma string muito longa "
         "que foi dividida em múltiplas "
         "linhas do código para melhor "
         "legibilidade")

print(texto)
print()

# Exemplo 3: Usar \ para continuação de linha
print("Exemplo 3: Usar \\ para continuação de linha")
texto = "Esta é uma string muito longa \
que continua na próxima linha \
do código"

print(texto)
print()

# ==========================================
# 5. STRINGS BRUTAS (RAW STRINGS)
# ==========================================
print("=" * 50)
print("5. STRINGS BRUTAS (RAW STRINGS - r\"\")")
print("=" * 50)

# Exemplo 1: String bruta vs Normal
print("Exemplo 1: Comparar normal vs bruta")
caminho_normal = "C:\\Users\\Thiago\\Documents"
caminho_bruto = r"C:\Users\Thiago\Documents"

print("Normal:")
print(caminho_normal)
print("\nBruto:")
print(caminho_bruto)
print()

# Exemplo 2: Regex com string bruta
print("Exemplo 2: Padrão regex")
padrao_normal = "\\d{3}-\\d{4}"
padrao_bruto = r"\d{3}-\d{4}"

print("Normal:")
print(padrao_normal)
print("\nBruto:")
print(padrao_bruto)
print()

# Exemplo 3: String bruta com múltiplas linhas
print("Exemplo 3: String bruta com múltiplas linhas")
padrao = r"""
C:\Pasta1\Pasta2\Arquivo.txt
D:\Dados\backup\2024
"""

print(padrao)
print()

# ==========================================
# 6. DOCSTRINGS
# ==========================================
print("=" * 50)
print("6. DOCSTRINGS")
print("=" * 50)

# Exemplo 1: Docstring de função
def calcular_media(notas):
    """
    Calcula a média aritmética de uma lista de notas.
    
    Args:
        notas: Lista de números (int ou float)
    
    Returns:
        float: A média das notas
    
    Exemplo:
        >>> calcular_media([8, 9, 7])
        8.0
    """
    return sum(notas) / len(notas)

print("Exemplo 1: Docstring de função")
print(f"Docstring da função:\n{calcular_media.__doc__}")
print()

# Exemplo 2: Docstring de classe
class Pessoa:
    """
    Representa uma pessoa com nome e idade.
    
    Atributos:
        nome (str): Nome da pessoa
        idade (int): Idade da pessoa
    """
    
    def __init__(self, nome, idade):
        """Inicializa uma pessoa"""
        self.nome = nome
        self.idade = idade

print("Exemplo 2: Docstring de classe")
print(f"Docstring da classe:\n{Pessoa.__doc__}")
print()

# ==========================================
# 7. QUEBRA DE LINHA COM PARÊNTESES
# ==========================================
print("=" * 50)
print("7. QUEBRA DE LINHA COM PARÊNTESES")
print("=" * 50)

# Exemplo 1: String dividida por parênteses
print("Exemplo 1: Dividir string com parênteses")
mensagem = (
    "Esta é uma mensagem muito longa "
    "que foi dividida em múltiplas linhas "
    "para melhor legibilidade do código"
)

print(mensagem)
print()

# Exemplo 2: Lista de strings
print("Exemplo 2: Lista de strings concatenadas")
lista_linhas = (
    "Linha 1\n"
    "Linha 2\n"
    "Linha 3"
)

print(lista_linhas)
print()

# ==========================================
# 8. PRESERVAR ESPAÇOS E INDENTAÇÃO
# ==========================================
print("=" * 50)
print("8. PRESERVAR ESPAÇOS E INDENTAÇÃO")
print("=" * 50)

# Exemplo 1: Indentação preservada
print("Exemplo 1: Indentação preservada")
codigo = """
def hello():
    print("Olá")
    if True:
        print("Mundo")
"""

print(codigo)
print()

# Exemplo 2: Remover indentação desnecessária
print("Exemplo 2: Remover indentação com lstrip()")
codigo = """
    def hello():
        print("Olá")
        if True:
            print("Mundo")
""".lstrip()

print(codigo)
print()

# Exemplo 3: Remover espaços em branco
print("Exemplo 3: Strip de todas as linhas")
texto = """
    Linha com indentação
    Outra linha
    Mais uma linha
"""

linhas = [linha.strip() for linha in texto.strip().split('\n')]
print("Linhas sem espaços extras:")
for linha in linhas:
    print(f"  '{linha}'")
print()

# ==========================================
# 9. EXEMPLOS PRÁTICOS
# ==========================================
print("=" * 50)
print("9. EXEMPLOS PRÁTICOS")
print("=" * 50)

# Exemplo 1: Mensagem de boas-vindas
print("\nExemplo 1: Mensagem de boas-vindas")
print("-" * 40)
boas_vindas = """
╔════════════════════════════╗
║  BEM-VINDO AO PROGRAMA!   ║
╚════════════════════════════╝

Escolha uma opção:
1. Novo arquivo
2. Abrir arquivo
3. Salvar arquivo
4. Sair
"""

print(boas_vindas)

# Exemplo 2: Relatório formatado
print("\nExemplo 2: Relatório formatado")
print("-" * 40)
nome = "João Silva"
departamento = "TI"
salario = 5000.00

relatorio = f"""
RELATÓRIO DE FUNCIONÁRIO
========================

Nome: {nome}
Departamento: {departamento}
Salário: R$ {salario:.2f}
Data: 25/01/2024

Assinado pelo gerente
"""

print(relatorio)

# Exemplo 3: Email formatado
print("Exemplo 3: Email formatado")
print("-" * 40)
remetente = "sistema@empresa.com"
destinatario = "usuario@empresa.com"
assunto = "Confirmação de Cadastro"

email = f"""From: {remetente}
To: {destinatario}
Subject: {assunto}

Prezado usuário,

Seu cadastro foi realizado com sucesso!
Agora você pode acessar o sistema.

Atenciosamente,
Sistema Automatizado
"""

print(email)

# Exemplo 4: HTML/XML
print("Exemplo 4: Código HTML")
print("-" * 40)
html = """
<html>
    <head>
        <title>Meu Site</title>
    </head>
    <body>
        <h1>Bem-vindo!</h1>
        <p>Este é meu site.</p>
    </body>
</html>
"""

print(html)

# Exemplo 5: SQL Query
print("Exemplo 5: SQL Query")
print("-" * 40)
tabela = "usuarios"
email_busca = "usuario@example.com"

sql = f"""
SELECT id, nome, email, criado_em
FROM {tabela}
WHERE email = '{email_busca}'
ORDER BY criado_em DESC
LIMIT 10
"""

print(sql)

# Exemplo 6: JSON
print("Exemplo 6: JSON formatado")
print("-" * 40)
json_texto = """
{
    "usuarios": [
        {
            "id": 1,
            "nome": "João",
            "email": "joao@example.com"
        },
        {
            "id": 2,
            "nome": "Maria",
            "email": "maria@example.com"
        }
    ]
}
"""

print(json_texto)

# ==========================================
# 10. TRABALHANDO COM QUEBRAS DE LINHA
# ==========================================
print("=" * 50)
print("10. TRABALHANDO COM QUEBRAS DE LINHA")
print("=" * 50)

# Exemplo 1: Contar quebras de linha
print("Exemplo 1: Contar quebras de linha")
texto = """Linha 1
Linha 2
Linha 3
Linha 4"""

quebras = texto.count('\n')
print(f"Texto:\n{texto}")
print(f"\nTotal de quebras de linha: {quebras}")
print()

# Exemplo 2: Dividir em linhas
print("Exemplo 2: Dividir em linhas com splitlines()")
texto = """Linha 1
Linha 2
Linha 3"""

linhas = texto.splitlines()
print(f"Texto original:\n{texto}")
print(f"\nLinhas como lista: {linhas}")
print(f"Total de linhas: {len(linhas)}")
print()

# Exemplo 3: Juntar linhas
print("Exemplo 3: Juntar linhas com join()")
linhas = ["Linha 1", "Linha 2", "Linha 3"]
texto = '\n'.join(linhas)
print(f"Lista: {linhas}")
print(f"\nTexto juntado:\n{texto}")
print()

# Exemplo 4: Processar arquivo (simulado)
print("Exemplo 4: Processar múltiplas linhas")
conteudo = """João Silva,25,São Paulo
Maria Santos,30,Rio de Janeiro
Pedro Oliveira,28,Belo Horizonte"""

linhas = conteudo.split('\n')
print("Registros:")
for linha in linhas:
    nome, idade, cidade = linha.split(',')
    print(f"  {nome}: {idade} anos, {cidade}")
print()

# ==========================================
# 11. CASOS ESPECIAIS E ARMADILHAS
# ==========================================
print("=" * 50)
print("11. CASOS ESPECIAIS E ARMADILHAS")
print("=" * 50)

# Exemplo 1: Diferença entre \r\n e \n
print("Exemplo 1: Diferentes fins de linha")
windows = "Linha 1\r\nLinha 2"  # Windows
unix = "Linha 1\nLinha 2"      # Unix/Linux/Mac

print(f"Windows (\\r\\n): {repr(windows)}")
print(f"Unix (\\n): {repr(unix)}")
print()

# Exemplo 2: Espaços em branco invisíveis
print("Exemplo 2: Espaços em branco")
texto_com_espacos = """
   Indentado
       Muito indentado
   Volta ao normal
"""

print("Com repr() para ver espaços:")
print(repr(texto_com_espacos))
print()

# Exemplo 3: Última linha vazia
print("Exemplo 3: Verificar última linha vazia")
texto1 = "Linha 1\nLinha 2"
texto2 = "Linha 1\nLinha 2\n"

print(f"Sem quebra final: {repr(texto1)}")
print(f"Com quebra final: {repr(texto2)}")
print(f"Terminam diferente? {texto1 != texto2}")
print()

# ==========================================
# 12. RESUMO DE TÉCNICAS
# ==========================================
print("=" * 50)
print("12. RESUMO DE TÉCNICAS")
print("=" * 50)
print("""
ASPAS TRIPLAS:
texto = \"\"\"
Linha 1
Linha 2
Linha 3
\"\"\"

ESCAPE DE QUEBRA:
texto = "Linha 1\\nLinha 2\\nLinha 3"

PARÊNTESES:
texto = (
    "Parte 1 "
    "Parte 2 "
    "Parte 3"
)

BARRA INVERTIDA:
texto = "Parte 1 \\
Parte 2 \\
Parte 3"

STRING BRUTA:
caminho = r"C:\\Users\\Docs"

OPERAÇÕES ÚTEIS:
- texto.split('\\n')          # Dividir por quebra
- texto.splitlines()          # Dividir mantendo apenas texto
- '\\n'.join(lista)           # Juntar com quebra
- texto.strip()               # Remover espaços
- texto.lstrip()              # Remover espaços à esquerda
- texto.rstrip()              # Remover espaços à direita
- repr(texto)                 # Ver caracteres invisíveis
- len(texto.split('\\n'))     # Contar linhas

DICAS:
1. Use aspas triplas para múltiplas linhas
2. Use \\n para quebras em strings simples
3. Use parênteses para quebrar código legível
4. Use raw strings (r"") para caminhos Windows
5. Use splitlines() para processar múltiplas linhas
6. Tenha cuidado com espaços em branco invisíveis
7. Considere usar strip() para remover espaços desnecessários
""")
