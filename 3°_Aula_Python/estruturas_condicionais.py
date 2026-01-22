# ==========================================
# ESTRUTURAS CONDICIONAIS EM PYTHON
# ==========================================

# ==========================================
# 1. IF SIMPLES
# ==========================================
print("=" * 50)
print("1. IF SIMPLES")
print("=" * 50)

# Exemplo 1: Verificar maioridade
idade = 20

if idade >= 18:
    print(f"Idade: {idade}")
    print("Você é maior de idade!")

print()

# Exemplo 2: Verificar número positivo
numero = 10

if numero > 0:
    print(f"Número: {numero}")
    print("Número positivo!")

print()

# Exemplo 3: Verificar string vazia
texto = "Python"

if texto:
    print(f"Texto: '{texto}'")
    print("String não vazia!")

print()

# Exemplo 4: Verificar membro de lista
frutas = ["maçã", "banana", "laranja"]

if "banana" in frutas:
    print(f"Lista: {frutas}")
    print("Banana está na lista!")

print()

# ==========================================
# 2. IF/ELSE
# ==========================================
print("=" * 50)
print("2. IF/ELSE")
print("=" * 50)

# Exemplo 1: Verificar aprovação
nota = 6

if nota >= 7:
    print(f"Nota: {nota}")
    print("✓ Aprovado!")
else:
    print(f"Nota: {nota}")
    print("✗ Reprovado!")

print()

# Exemplo 2: Verificar número par ou ímpar
numero = 5

if numero % 2 == 0:
    print(f"Número: {numero}")
    print("É par!")
else:
    print(f"Número: {numero}")
    print("É ímpar!")

print()

# Exemplo 3: Verificar acesso
usuario = "Maria"
usuarios_autorizado = ["João", "Maria", "Pedro"]

if usuario in usuarios_autorizado:
    print(f"Usuário: {usuario}")
    print("✓ Acesso concedido!")
else:
    print(f"Usuário: {usuario}")
    print("✗ Acesso negado!")

print()

# Exemplo 4: Verificar idade para desconto
idade = 65

if idade >= 60:
    desconto = 0.20
    print(f"Idade: {idade}")
    print(f"Desconto: {desconto * 100}% (idoso)")
else:
    desconto = 0.05
    print(f"Idade: {idade}")
    print(f"Desconto: {desconto * 100}% (padrão)")

print()

# ==========================================
# 3. IF/ELIF/ELSE
# ==========================================
print("=" * 50)
print("3. IF/ELIF/ELSE")
print("=" * 50)

# Exemplo 1: Classificação de notas
print("Exemplo 1: Classificação de notas")
nota = 8

if nota >= 9:
    print(f"Nota: {nota}")
    print("Conceito: A - Excelente!")
elif nota >= 8:
    print(f"Nota: {nota}")
    print("Conceito: B - Bom!")
elif nota >= 7:
    print(f"Nota: {nota}")
    print("Conceito: C - Satisfatório")
elif nota >= 5:
    print(f"Nota: {nota}")
    print("Conceito: D - Insuficiente")
else:
    print(f"Nota: {nota}")
    print("Conceito: E - Reprovado!")

print()

# Exemplo 2: Classificação por idade
print("Exemplo 2: Classificação por idade")
idade = 15

if idade < 13:
    categoria = "Criança"
elif idade < 18:
    categoria = "Adolescente"
elif idade < 60:
    categoria = "Adulto"
else:
    categoria = "Idoso"

print(f"Idade: {idade}")
print(f"Categoria: {categoria}")

print()

# Exemplo 3: Escolher tamanho de camiseta
print("Exemplo 3: Escolher tamanho de camiseta")
altura = 1.75

if altura < 1.60:
    tamanho = "P (Pequeno)"
elif altura < 1.75:
    tamanho = "M (Médio)"
elif altura < 1.90:
    tamanho = "G (Grande)"
else:
    tamanho = "GG (Muito Grande)"

print(f"Altura: {altura}m")
print(f"Tamanho: {tamanho}")

print()

# Exemplo 4: Sistema de faixa etária para cinema
print("Exemplo 4: Sistema de faixa etária para cinema")
idade = 12

if idade < 12:
    classificacao = "Livre"
    acesso = "✓"
elif idade < 14:
    classificacao = "12 anos"
    acesso = "✓"
elif idade < 16:
    classificacao = "14 anos"
    acesso = "✓"
elif idade < 18:
    classificacao = "16 anos"
    acesso = "✓"
else:
    classificacao = "18 anos"
    acesso = "✓"

print(f"Idade: {idade}")
print(f"Classificação: {classificacao}")
print(f"Pode assistir: {acesso}")

print()

# ==========================================
# 4. IF ANINHADO
# ==========================================
print("=" * 50)
print("4. IF ANINHADO")
print("=" * 50)

# Exemplo 1: Verificar acesso a conta bancária
print("Exemplo 1: Verificar acesso a conta bancária")
idade = 20
tem_documento = True
tem_renda = True

if idade >= 18:
    print(f"Idade: {idade} - ✓ Maior de idade")
    
    if tem_documento:
        print(f"Documento: ✓ Possui")
        
        if tem_renda:
            print(f"Renda: ✓ Sim")
            print("✓ Pode abrir conta bancária!")
        else:
            print(f"Renda: ✗ Não")
            print("✗ Precisa ter renda para abrir conta")
    else:
        print(f"Documento: ✗ Não possui")
        print("✗ Precisa de documento para abrir conta")
else:
    print(f"Idade: {idade} - ✗ Menor de idade")
    print("✗ Precisa ser maior de idade para abrir conta")

print()

# Exemplo 2: Compra online com validações
print("Exemplo 2: Compra online com validações")
preco = 150
tem_cupom = True
valor_minimo_cupom = 100
tem_credito = True

if preco > 0:
    print(f"Preço original: R${preco}")
    
    if tem_cupom and preco >= valor_minimo_cupom:
        desconto = preco * 0.10
        preco_final = preco - desconto
        print(f"Cupom aplicado! Desconto: R${desconto:.2f}")
    else:
        preco_final = preco
        if tem_cupom:
            print(f"Cupom não válido para este preço (mínimo: R${valor_minimo_cupom})")
    
    print(f"Preço final: R${preco_final:.2f}")
    
    if tem_credito:
        print("✓ Pagamento aprovado!")
    else:
        print("✗ Crédito insuficiente")
else:
    print("✗ Preço inválido")

print()

# Exemplo 3: Verificar permissão para filme
print("Exemplo 3: Verificar permissão para filme")
idade = 16
eh_acompanhado = True
classificacao_filme = 12

if idade >= classificacao_filme:
    print(f"Idade: {idade} - Classificação do filme: {classificacao_filme}")
    print("✓ Pode assistir sozinho")
elif eh_acompanhado:
    print(f"Idade: {idade} - Classificação do filme: {classificacao_filme}")
    print(f"✓ Pode assistir acompanhado")
else:
    print(f"Idade: {idade} - Classificação do filme: {classificacao_filme}")
    print("✗ Não pode assistir")

print()

# ==========================================
# 5. OPERADOR TERNÁRIO (ONE-LINER)
# ==========================================
print("=" * 50)
print("5. OPERADOR TERNÁRIO")
print("=" * 50)

# Exemplo 1: Verificação simples
print("Exemplo 1: Verificação simples")
idade = 18
status = "maior de idade" if idade >= 18 else "menor de idade"
print(f"Idade: {idade} - Status: {status}")

print()

# Exemplo 2: Determinar desconto
print("Exemplo 2: Determinar desconto")
cliente_vip = True
desconto = "20%" if cliente_vip else "5%"
print(f"Cliente VIP: {cliente_vip} - Desconto: {desconto}")

print()

# Exemplo 3: Ternário aninhado
print("Exemplo 3: Ternário aninhado")
nota = 8
resultado = "Excelente!" if nota >= 9 else ("Bom!" if nota >= 7 else "Insuficiente")
print(f"Nota: {nota} - {resultado}")

print()

# Exemplo 4: Palavra singular/plural
print("Exemplo 4: Palavra singular/plural")
quantidade = 3
palavra = "livro" if quantidade == 1 else "livros"
print(f"Você tem {quantidade} {palavra}")

quantidade = 1
palavra = "livro" if quantidade == 1 else "livros"
print(f"Você tem {quantidade} {palavra}")

print()

# ==========================================
# 6. ESTRUTURAS CONDICIONAIS COM AND/OR/NOT
# ==========================================
print("=" * 50)
print("6. CONDICIONAIS COM AND/OR/NOT")
print("=" * 50)

# Exemplo 1: Usando AND
print("Exemplo 1: Usando AND (ambas devem ser verdadeiras)")
idade = 25
tem_habilitacao = True

if idade >= 18 and tem_habilitacao:
    print(f"Idade: {idade}, Habilitação: {tem_habilitacao}")
    print("✓ Pode dirigir")
else:
    print(f"Idade: {idade}, Habilitação: {tem_habilitacao}")
    print("✗ Não pode dirigir")

print()

# Exemplo 2: Usando OR
print("Exemplo 2: Usando OR (uma deve ser verdadeira)")
eh_fim_de_semana = False
eh_feriado = True

if eh_fim_de_semana or eh_feriado:
    print(f"Fim de semana: {eh_fim_de_semana}, Feriado: {eh_feriado}")
    print("✓ Não trabalha")
else:
    print(f"Fim de semana: {eh_fim_de_semana}, Feriado: {eh_feriado}")
    print("✗ Trabalha normalmente")

print()

# Exemplo 3: Usando NOT
print("Exemplo 3: Usando NOT (negar)")
estava_chovendo = False

if not estava_chovendo:
    print(f"Estava chovendo: {estava_chovendo}")
    print("✓ Pode sair para passear")
else:
    print(f"Estava chovendo: {estava_chovendo}")
    print("✗ Não pode sair")

print()

# Exemplo 4: Combinando AND, OR, NOT
print("Exemplo 4: Combinando AND, OR, NOT")
tem_dinheiro = True
tem_vontade = True
esta_chovendo = False

if (tem_dinheiro and tem_vontade) and not esta_chovendo:
    print(f"Dinheiro: {tem_dinheiro}, Vontade: {tem_vontade}, Chovendo: {esta_chovendo}")
    print("✓ Pode ir ao cinema")
else:
    print(f"Dinheiro: {tem_dinheiro}, Vontade: {tem_vontade}, Chovendo: {esta_chovendo}")
    print("✗ Não pode ir ao cinema")

print()

# ==========================================
# 7. EXEMPLOS PRÁTICOS COMPLETOS
# ==========================================
print("=" * 50)
print("7. EXEMPLOS PRÁTICOS COMPLETOS")
print("=" * 50)

# Exemplo 1: Sistema de notas com feedback detalhado
print("\nExemplo 1: Sistema de notas")
print("-" * 40)
nota = 7.5
presenca = 0.85

if nota >= 7 and presenca >= 0.75:
    print(f"Nota: {nota}")
    print(f"Presença: {presenca * 100}%")
    
    if nota >= 9:
        print("✓ APROVADO com louvor!")
    elif nota >= 8:
        print("✓ APROVADO com excelência!")
    else:
        print("✓ APROVADO!")
elif nota >= 5 and presenca >= 0.75:
    print(f"Nota: {nota}")
    print(f"Presença: {presenca * 100}%")
    print("⚠ Em recuperação")
else:
    print(f"Nota: {nota}")
    print(f"Presença: {presenca * 100}%")
    print("✗ REPROVADO")

print()

# Exemplo 2: Calcular valor de entrada com categorias
print("Exemplo 2: Calcular entrada para parque")
print("-" * 40)
idade = 8
eh_residente = True

preco_base = 50

if idade < 5:
    preco = 0
    categoria = "Gratuito (menor de 5 anos)"
elif idade < 12:
    preco = preco_base * 0.5
    categoria = "Meia entrada (criança)"
elif idade < 60:
    preco = preco_base
    categoria = "Inteira (adulto)"
else:
    preco = preco_base * 0.5
    categoria = "Meia entrada (idoso)"

if eh_residente and preco > 0:
    preco = preco * 0.8
    residente_texto = " (com desconto de residente)"
else:
    residente_texto = ""

print(f"Idade: {idade}")
print(f"Categoria: {categoria}{residente_texto}")
print(f"Preço: R${preco:.2f}")

print()

# Exemplo 3: Validação de senha
print("Exemplo 3: Validação de senha")
print("-" * 40)
senha = "Senha123@"
tem_maiuscula = any(c.isupper() for c in senha)
tem_minuscula = any(c.islower() for c in senha)
tem_numero = any(c.isdigit() for c in senha)
tem_caractere_especial = any(c in "@#$%&*" for c in senha)
tem_comprimento_minimo = len(senha) >= 8

print(f"Senha: {senha}")
print(f"Comprimento (≥8): {'✓' if tem_comprimento_minimo else '✗'}")
print(f"Maiúscula: {'✓' if tem_maiuscula else '✗'}")
print(f"Minúscula: {'✓' if tem_minuscula else '✗'}")
print(f"Número: {'✓' if tem_numero else '✗'}")
print(f"Caractere especial: {'✓' if tem_caractere_especial else '✗'}")

if (tem_maiuscula and tem_minuscula and tem_numero and 
    tem_caractere_especial and tem_comprimento_minimo):
    print("✓ Senha forte!")
elif (tem_maiuscula and tem_minuscula and tem_numero and tem_comprimento_minimo):
    print("⚠ Senha média")
else:
    print("✗ Senha fraca")

print()

# Exemplo 4: Recomendação de roupa baseada em temperatura
print("Exemplo 4: Recomendação de roupa")
print("-" * 40)
temperatura = 22
chovendo = False

if temperatura < 10:
    roupa = "Casaco pesado"
elif temperatura < 15:
    roupa = "Casaco leve"
elif temperatura < 20:
    roupa = "Blusa/Camiseta de mangas"
elif temperatura < 25:
    roupa = "Camiseta"
else:
    roupa = "Camiseta regata/bermuda"

if chovendo:
    roupa += " + Capa de chuva"

print(f"Temperatura: {temperatura}°C")
print(f"Chovendo: {'Sim' if chovendo else 'Não'}")
print(f"Recomendação: {roupa}")

print()

# ==========================================
# 8. BOAS PRÁTICAS
# ==========================================
print("=" * 50)
print("8. BOAS PRÁTICAS")
print("=" * 50)
print("""
RECOMENDAÇÕES:

1. EVITE aninhamentos muito profundos
   - Use 'return' em funções para sair cedo
   - Refatore em funções menores

2. Use nomes descritivos para variáveis booleanas
   - ✓ eh_maior_idade = True
   - ✗ x = True

3. Coloque condições simples primeiro
   - if not valor: return
   - # código principal

4. Use operador ternário apenas para casos simples
   - ✓ status = "ativo" if ativo else "inativo"
   - ✗ valor = "a" if x > 5 else "b" if x > 3 else "c"...

5. Combine operadores AND/OR de forma clara
   - Use parênteses para deixar clara a intenção
   - if (condicao1 and condicao2) or condicao3:

6. Evite comparar com True/False
   - ✓ if ativo:
   - ✗ if ativo == True:

7. Prefira 'in' para verificar pertencimento
   - ✓ if item in lista:
   - ✗ if lista.count(item) > 0:
""")

print()

# ==========================================
# RESUMO
# ==========================================
print("=" * 50)
print("RESUMO DE ESTRUTURAS CONDICIONAIS")
print("=" * 50)
print("""
IF SIMPLES:
if condicao:
    # código

IF/ELSE:
if condicao:
    # código se verdadeiro
else:
    # código se falso

IF/ELIF/ELSE:
if condicao1:
    # código 1
elif condicao2:
    # código 2
else:
    # código padrão

OPERADOR TERNÁRIO:
variavel = valor1 if condicao else valor2

OPERADORES LÓGICOS:
- and: ambas verdadeiras
- or: pelo menos uma verdadeira
- not: inverte o valor

DICAS:
- Use identação de 4 espaços
- Mantenha condições legíveis
- Combine operadores com cuidado
- Prefira múltiplas linhas a condições muito longas
""")
