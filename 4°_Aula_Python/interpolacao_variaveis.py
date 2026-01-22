# ==========================================
# INTERPOLAÇÃO DE VARIÁVEIS EM PYTHON
# ==========================================

# ==========================================
# 1. CONCATENAÇÃO COM +
# ==========================================
print("=" * 50)
print("1. CONCATENAÇÃO COM +")
print("=" * 50)

# Exemplo 1: Concatenação simples
print("Exemplo 1: Concatenação simples")
nome = "João"
mensagem = "Olá, " + nome
print(mensagem)
print()

# Exemplo 2: Concatenação múltipla
print("Exemplo 2: Concatenação múltipla")
primeiro_nome = "João"
ultimo_nome = "Silva"
idade = 25
mensagem = "Nome: " + primeiro_nome + " " + ultimo_nome + ", Idade: " + str(idade)
print(mensagem)
print()

# Exemplo 3: Concatenação com quebra de linha
print("Exemplo 3: Concatenação com quebra de linha")
linha1 = "Primeira linha"
linha2 = "Segunda linha"
texto = linha1 + "\n" + linha2
print(texto)
print()

# DESVANTAGEM: Deve converter números para string com str()
print("DESVANTAGEM: Precisa converter números com str()")
numero = 10
# mensagem = "O número é " + numero  # ERRO!
mensagem = "O número é " + str(numero)  # OK
print(mensagem)
print()

# ==========================================
# 2. MÉTODO format()
# ==========================================
print("=" * 50)
print("2. MÉTODO format()")
print("=" * 50)

# Exemplo 1: format() básico
print("Exemplo 1: format() básico com {}")
nome = "Maria"
mensagem = "Olá, {}!".format(nome)
print(mensagem)
print()

# Exemplo 2: format() com múltiplos valores
print("Exemplo 2: format() com múltiplos valores")
nome = "Pedro"
idade = 30
cidade = "São Paulo"
mensagem = "{} tem {} anos e mora em {}".format(nome, idade, cidade)
print(mensagem)
print()

# Exemplo 3: format() com índices explícitos
print("Exemplo 3: format() com índices explícitos")
mensagem = "Primeiro: {0}, Segundo: {1}, Primeiro novamente: {0}".format("A", "B")
print(mensagem)
print()

# Exemplo 4: format() com números
print("Exemplo 4: format() com números (conversão automática)")
numero = 42
decimal = 3.14159
mensagem = "Inteiro: {}, Decimal: {}".format(numero, decimal)
print(mensagem)
print()

# Exemplo 5: format() com chaves nomeadas
print("Exemplo 5: format() com chaves nomeadas")
mensagem = "{nome} tem {idade} anos".format(nome="Ana", idade=28)
print(mensagem)
print()

# Exemplo 6: format() com formatação de números
print("Exemplo 6: format() com formatação de números")
pi = 3.14159
preco = 19.90
mensagem = "Pi: {:.2f}, Preço: R${:.2f}".format(pi, preco)
print(mensagem)
print()

# Exemplo 7: format() com preenchimento
print("Exemplo 7: format() com preenchimento")
numero = 5
mensagem = "Número: {:05d}".format(numero)  # Preenche com zeros
print(mensagem)
print()

# ==========================================
# 3. F-STRINGS (FORMATAÇÃO MODERNA - Python 3.6+)
# ==========================================
print("=" * 50)
print("3. F-STRINGS (FORMATAÇÃO MODERNA)")
print("=" * 50)

# Exemplo 1: f-string básica
print("Exemplo 1: f-string básica")
nome = "João"
mensagem = f"Olá, {nome}!"
print(mensagem)
print()

# Exemplo 2: f-string com múltiplas variáveis
print("Exemplo 2: f-string com múltiplas variáveis")
nome = "Maria"
idade = 25
cidade = "Rio de Janeiro"
mensagem = f"{nome} tem {idade} anos e mora em {cidade}"
print(mensagem)
print()

# Exemplo 3: f-string com expressões
print("Exemplo 3: f-string com expressões")
a = 10
b = 5
mensagem = f"{a} + {b} = {a + b}"
print(mensagem)
print()

# Exemplo 4: f-string com operações matemáticas
print("Exemplo 4: f-string com operações matemáticas")
valor = 100
desconto = 0.1
preco_final = valor * (1 - desconto)
mensagem = f"Valor original: R${valor:.2f}, Desconto: {desconto*100}%, Preço final: R${preco_final:.2f}"
print(mensagem)
print()

# Exemplo 5: f-string com formatação numérica
print("Exemplo 5: f-string com formatação numérica")
pi = 3.14159
temperatura = 22.5
dinheiro = 1234.567
print(f"Pi com 2 casas: {pi:.2f}")
print(f"Temperatura: {temperatura:.1f}°C")
print(f"Dinheiro: R${dinheiro:.2f}")
print()

# Exemplo 6: f-string com alinhamento
print("Exemplo 6: f-string com alinhamento")
nome = "Python"
print(f"Esquerda: {nome:<15}")
print(f"Centro: {nome:^15}")
print(f"Direita: {nome:>15}")
print()

# Exemplo 7: f-string com preenchimento
print("Exemplo 7: f-string com preenchimento")
numero = 7
print(f"Número: {numero:05d}")
print(f"Número: {numero:05x}")  # Hexadecimal
print()

# Exemplo 8: f-string com chamada de função
print("Exemplo 8: f-string com chamada de função")
texto = "python"
mensagem = f"Maiúscula: {texto.upper()}, Comprimento: {len(texto)}"
print(mensagem)
print()

# Exemplo 9: f-string com condicional
print("Exemplo 9: f-string com condicional (Python 3.10+)")
idade = 20
mensagem = f"É maior de idade? {'Sim' if idade >= 18 else 'Não'}"
print(mensagem)
print()

# Exemplo 10: f-string com variáveis de formatação
print("Exemplo 10: f-string com variáveis de formatação")
precisao = 3
pi = 3.14159
mensagem = f"Pi: {pi:.{precisao}f}"
print(mensagem)
print()

# ==========================================
# 4. FORMATAÇÃO COM % (ANTIGA)
# ==========================================
print("=" * 50)
print("4. FORMATAÇÃO COM % (ANTIGA)")
print("=" * 50)

# Exemplo 1: Formatação básica com %s
print("Exemplo 1: Formatação com %s (string)")
nome = "João"
mensagem = "Olá, %s!" % nome
print(mensagem)
print()

# Exemplo 2: Formatação com múltiplos valores
print("Exemplo 2: Formatação com múltiplos valores")
nome = "Maria"
idade = 25
mensagem = "%s tem %d anos" % (nome, idade)
print(mensagem)
print()

# Exemplo 3: Formatação com %d (inteiro)
print("Exemplo 3: Formatação com %d (inteiro)")
numero = 42
mensagem = "O número é %d" % numero
print(mensagem)
print()

# Exemplo 4: Formatação com %f (float)
print("Exemplo 4: Formatação com %f (float)")
pi = 3.14159
mensagem = "Pi é aproximadamente %.2f" % pi
print(mensagem)
print()

# Exemplo 5: Formatação com %x (hexadecimal)
print("Exemplo 5: Formatação com %x (hexadecimal)")
numero = 255
mensagem = "Número em hex: %x" % numero
print(mensagem)
print()

# NOTA: Essa formatação é menos legível que format() ou f-strings
print("NOTA: Essa formatação é menos usada atualmente")
print()

# ==========================================
# 5. JOIN - JUNTAR STRINGS
# ==========================================
print("=" * 50)
print("5. JOIN - JUNTAR STRINGS")
print("=" * 50)

# Exemplo 1: join() com lista
print("Exemplo 1: join() com lista")
palavras = ["Python", "é", "incrível"]
mensagem = " ".join(palavras)
print(mensagem)
print()

# Exemplo 2: join() com diferentes separadores
print("Exemplo 2: join() com diferentes separadores")
elementos = ["A", "B", "C"]
print("Espaço: " + " ".join(elementos))
print("Hífen: " + "-".join(elementos))
print("Vírgula: " + ", ".join(elementos))
print()

# Exemplo 3: join() com números (precisa converter)
print("Exemplo 3: join() com números (precisa converter)")
numeros = [1, 2, 3, 4, 5]
mensagem = ", ".join(str(n) for n in numeros)
print(mensagem)
print()

# ==========================================
# 6. COMPARAÇÃO DE MÉTODOS
# ==========================================
print("=" * 50)
print("6. COMPARAÇÃO DE MÉTODOS")
print("=" * 50)

nome = "João"
idade = 25

print("Mesmo resultado, diferentes métodos:\n")

# Método 1: Concatenação
resultado1 = "Nome: " + nome + ", Idade: " + str(idade)
print(f"1. Concatenação: {resultado1}")

# Método 2: format()
resultado2 = "Nome: {}, Idade: {}".format(nome, idade)
print(f"2. format(): {resultado2}")

# Método 3: f-string
resultado3 = f"Nome: {nome}, Idade: {idade}"
print(f"3. f-string: {resultado3}")

# Método 4: % formatting
resultado4 = "Nome: %s, Idade: %d" % (nome, idade)
print(f"4. %% formatting: {resultado4}")

print()

# ==========================================
# 7. FORMATAÇÃO AVANÇADA
# ==========================================
print("=" * 50)
print("7. FORMATAÇÃO AVANÇADA")
print("=" * 50)

# Exemplo 1: Espaçamento e alinhamento
print("Exemplo 1: Espaçamento e alinhamento")
print(f"{'Nome':<15} {'Idade':>5} {'Cidade':^20}")
print(f"{'João':<15} {'25':>5} {'São Paulo':^20}")
print(f"{'Maria':<15} {'30':>5} {'Rio de Janeiro':^20}")
print()

# Exemplo 2: Números com separador de milhares
print("Exemplo 2: Números com separador de milhares")
valor = 1234567.89
print(f"Sem separador: {valor:.2f}")
print(f"Com separador: {valor:,.2f}")
print()

# Exemplo 3: Números binários, octais, hexadecimais
print("Exemplo 3: Números binários, octais, hexadecimais")
numero = 255
print(f"Decimal: {numero}")
print(f"Binário: {numero:b}")
print(f"Octal: {numero:o}")
print(f"Hexadecimal: {numero:x}")
print()

# Exemplo 4: Porcentagem
print("Exemplo 4: Porcentagem")
taxa = 0.85
print(f"Taxa: {taxa:.0%}")
print(f"Taxa: {taxa:.1%}")
print()

# ==========================================
# 8. EXEMPLOS PRÁTICOS COMPLETOS
# ==========================================
print("=" * 50)
print("8. EXEMPLOS PRÁTICOS COMPLETOS")
print("=" * 50)

# Exemplo 1: Recibo de compra
print("\nExemplo 1: Recibo de compra")
print("-" * 40)
item = "Notebook"
quantidade = 2
preco_unitario = 2500.00
desconto_percentual = 0.10

subtotal = quantidade * preco_unitario
desconto = subtotal * desconto_percentual
total = subtotal - desconto

print(f"{'Item':<20} {'Qtd':>5} {'Preço':>12} {'Total':>12}")
print(f"{item:<20} {quantidade:>5} R${preco_unitario:>10.2f} R${subtotal:>10.2f}")
print(f"\nSubtotal: R${subtotal:.2f}")
print(f"Desconto (10%): R${desconto:.2f}")
print(f"Total: R${total:.2f}")

print()

# Exemplo 2: Informações de aluno
print("Exemplo 2: Informações de aluno")
print("-" * 40)
nome_aluno = "Pedro Silva"
matricula = 2024001
notas = [8.5, 9.0, 7.5]
media = sum(notas) / len(notas)

print(f"Aluno: {nome_aluno}")
print(f"Matrícula: {matricula:07d}")
print(f"Notas: {', '.join(f'{n:.1f}' for n in notas)}")
print(f"Média: {media:.2f}")
print(f"Conceito: {'A' if media >= 9 else 'B' if media >= 7 else 'C' if media >= 5 else 'D'}")

print()

# Exemplo 3: Relatório de vendas
print("Exemplo 3: Relatório de vendas")
print("-" * 40)
vendedor = "Carlos"
meta = 10000
vendido = 12500
percentual = (vendido / meta) * 100

print(f"Vendedor: {vendedor}")
print(f"Meta: R${meta:,.2f}")
print(f"Vendido: R${vendido:,.2f}")
print(f"Resultado: {'+' if vendido >= meta else ''}{((vendido - meta) / meta * 100):+.1f}%")
print(f"Status: {'✓ Atingiu meta' if percentual >= 100 else '✗ Não atingiu meta'}")

print()

# Exemplo 4: Formatação de data e hora (simulado)
print("Exemplo 4: Formatação de data e hora (simulado)")
print("-" * 40)
dia = 25
mes = 12
ano = 2024
hora = 14
minuto = 30

print(f"Data: {dia:02d}/{mes:02d}/{ano}")
print(f"Hora: {hora:02d}:{minuto:02d}")
print(f"Data e hora: {dia:02d}/{mes:02d}/{ano} às {hora:02d}:{minuto:02d}")

print()

# Exemplo 5: Tabela de usuários
print("Exemplo 5: Tabela de usuários")
print("-" * 40)
usuarios = [
    ("João Silva", "joao@email.com", "Ativo"),
    ("Maria Santos", "maria@email.com", "Ativo"),
    ("Pedro Oliveira", "pedro@email.com", "Inativo")
]

print(f"{'Nome':<20} {'Email':<20} {'Status':<10}")
print("-" * 50)
for nome, email, status in usuarios:
    print(f"{nome:<20} {email:<20} {status:<10}")

print()

# ==========================================
# 9. DICAS DE BOA PRÁTICA
# ==========================================
print("=" * 50)
print("9. DICAS DE BOA PRÁTICA")
print("=" * 50)
print("""
RECOMENDAÇÕES:

1. PREFIRA F-STRINGS (Python 3.6+)
   - Mais legível
   - Mais rápido
   - Suporta expressões
   ✓ f"{nome} tem {idade} anos"
   ✗ "{}  tem {} anos".format(nome, idade)

2. USE format() SE PRECISAR DE COMPATIBILIDADE
   - Python 3.0+
   ✓ "{} tem {} anos".format(nome, idade)
   ✗ "% s tem %d anos" % (nome, idade)

3. EVITE CONCATENAÇÃO COM + PARA MUITOS VALORES
   ✗ "Nome: " + nome + ", Idade: " + str(idade)
   ✓ f"Nome: {nome}, Idade: {idade}"

4. USE join() PARA LISTAS
   ✓ ", ".join(lista)
   ✗ lista[0] + ", " + lista[1] + ", " + lista[2]

5. CUIDADO COM CONVERSÕES
   - str() para string
   - int() para inteiro
   - float() para decimal
   ✗ numero = "42" + 8  # ERRO!
   ✓ numero = int("42") + 8  # OK

6. FORMATAÇÃO DE NÚMEROS
   - :.2f = 2 casas decimais
   - :05d = preenche com zeros
   - :, = separador de milhares
   - :% = porcentagem

7. LEGIBILIDADE ACIMA DE TUDO
   - Divida strings muito longas em múltiplas linhas
   - Use nomes descritivos
   - Comente código complexo
""")

print()

# ==========================================
# 10. RESUMO DOS MÉTODOS
# ==========================================
print("=" * 50)
print("10. RESUMO DOS MÉTODOS")
print("=" * 50)
print("""
MÉTODO                  | USO                          | EXEMPLO
------------------------|-----------------------------|--------------------
Concatenação com +      | Simples e direto             | "Olá, " + nome
format()                | Compatibilidade Python 3.0+ | "{}, {}".format(a, b)
f-string                | Moderno (Python 3.6+)       | f"{a}, {b}"
% formatting            | Antiga, evitar               | "%s, %d" % (a, b)
join()                  | Juntar listas                | " ".join(lista)

ESPECIFICADORES F-STRING:
{variavel}              : Valor simples
{variavel:.2f}          : Float com 2 casas
{variavel:05d}          : Inteiro com zeros
{variavel:<10}          : Alinhado à esquerda
{variavel:>10}          : Alinhado à direita
{variavel:^10}          : Centralizado
{variavel:,}            : Com separador de milhares
{variavel:%}            : Porcentagem
{variavel:b}            : Binário
{variavel:x}            : Hexadecimal
""")
