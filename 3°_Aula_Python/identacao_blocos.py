# ==========================================
# IDENTAÇÃO E BLOCOS EM PYTHON
# ==========================================
# Python usa identação (espaços/abas) para definir blocos de código
# Diferente de outras linguagens que usam chaves {}

# ==========================================
# 1. IDENTAÇÃO BÁSICA
# ==========================================
print("=" * 50)
print("1. IDENTAÇÃO BÁSICA")
print("=" * 50)
print()

# Exemplo 1: Sem identação (código no nível raiz)
print("Código sem identação (raiz):")
nome = "João"
idade = 25
print(f"Nome: {nome}, Idade: {idade}")

print()

# ==========================================
# 2. BLOCOS COM IF/ELIF/ELSE
# ==========================================
print("=" * 50)
print("2. BLOCOS COM IF/ELIF/ELSE")
print("=" * 50)
print()

# Exemplo 1: Bloco if simples
print("Exemplo 1: Bloco if simples")
idade = 18

if idade >= 18:
    print(f"Idade: {idade}")
    print("Você é maior de idade")
    print("Bem-vindo!")

print()

# Exemplo 2: Bloco if/else
print("Exemplo 2: Bloco if/else")
nota = 6

if nota >= 7:
    print(f"Nota: {nota}")
    print("Parabéns! Você foi aprovado")
    mensagem = "Sucesso"
    print(mensagem)
else:
    print(f"Nota: {nota}")
    print("Você foi reprovado")
    print("Tente novamente")

print()

# Exemplo 3: Bloco if/elif/else
print("Exemplo 3: Bloco if/elif/else")
conceito = "B"

if conceito == "A":
    print("Conceito A - Excelente!")
    pontos = 10
elif conceito == "B":
    print("Conceito B - Bom!")
    pontos = 8
elif conceito == "C":
    print("Conceito C - Satisfatório")
    pontos = 6
else:
    print("Conceito inválido")
    pontos = 0

print(f"Pontos obtidos: {pontos}")

print()

# ==========================================
# 3. BLOCOS ANINHADOS (IDENTAÇÃO MÚLTIPLA)
# ==========================================
print("=" * 50)
print("3. BLOCOS ANINHADOS")
print("=" * 50)
print()

# Exemplo: if dentro de if
idade = 20
tem_documento = True

print(f"idade = {idade}")
print(f"tem_documento = {tem_documento}")
print()

if idade >= 18:
    print("Você é maior de idade")
    
    if tem_documento:
        print("  Você tem documento")
        print("  Pode abrir conta")
        print("  Bem-vindo ao banco!")
    else:
        print("  Você não tem documento")
        print("  Não pode abrir conta agora")

print()

# Exemplo: Nível 3 de aninhamento
print("Exemplo com 3 níveis de aninhamento:")
pais = "Brasil"
estado = "São Paulo"
cidade = "São Paulo"

if pais == "Brasil":
    print(f"País: {pais}")
    
    if estado == "São Paulo":
        print(f"  Estado: {estado}")
        
        if cidade == "São Paulo":
            print(f"    Cidade: {cidade}")
            print("    Você está em SP capital")

print()

# ==========================================
# 4. BLOCOS COM FOR
# ==========================================
print("=" * 50)
print("4. BLOCOS COM FOR")
print("=" * 50)
print()

# Exemplo 1: For simples
print("Exemplo 1: For simples")
print("Números de 1 a 5:")

for numero in range(1, 6):
    print(numero)

print()

# Exemplo 2: For com código dentro do bloco
print("Exemplo 2: For com múltiplas linhas")
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(f"Fruta: {fruta}")
    print(f"Quantidade de letras: {len(fruta)}")
    print(f"Primeira letra: {fruta[0].upper()}")
    print()

print()

# Exemplo 3: For aninhado
print("Exemplo 3: For aninhado (tabuada)")

for i in range(1, 4):
    print(f"Tabuada do {i}:")
    for j in range(1, 6):
        resultado = i * j
        print(f"  {i} × {j} = {resultado}")
    print()

print()

# ==========================================
# 5. BLOCOS COM WHILE
# ==========================================
print("=" * 50)
print("5. BLOCOS COM WHILE")
print("=" * 50)
print()

# Exemplo 1: While simples
print("Exemplo 1: While simples")
contador = 1

while contador <= 3:
    print(f"Contador: {contador}")
    contador += 1

print()

# Exemplo 2: While com múltiplas linhas
print("Exemplo 2: While com múltiplas linhas")
numero = 10

while numero > 0:
    print(f"Número: {numero}")
    valor_dobrado = numero * 2
    print(f"Dobrado: {valor_dobrado}")
    numero -= 2
    print()

print()

# ==========================================
# 6. BLOCOS COM FUNÇÕES
# ==========================================
print("=" * 50)
print("6. BLOCOS COM FUNÇÕES")
print("=" * 50)
print()

# Exemplo 1: Função simples
def saudacao():
    print("Olá!")
    print("Bem-vindo à função")

print("Chamando saudacao():")
saudacao()
print()

# Exemplo 2: Função com parâmetros
def apresentar(nome, idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    categoria = "adulto" if idade >= 18 else "jovem"
    print(f"Categoria: {categoria}")

print("Chamando apresentar():")
apresentar("Maria", 22)
print()

# Exemplo 3: Função com bloco if dentro
def classificar_nota(nota):
    if nota >= 9:
        resultado = "Excelente"
    elif nota >= 7:
        resultado = "Bom"
    elif nota >= 5:
        resultado = "Satisfatório"
    else:
        resultado = "Insuficiente"
    
    print(f"Nota: {nota}")
    print(f"Classificação: {resultado}")
    return resultado

print("Chamando classificar_nota():")
classificar_nota(8)
print()

# Exemplo 4: Função com loop dentro
def contar_ate(numero):
    print(f"Contando de 1 até {numero}:")
    for i in range(1, numero + 1):
        if i % 2 == 0:
            print(f"  {i} (par)")
        else:
            print(f"  {i} (ímpar)")

print("Chamando contar_ate():")
contar_ate(5)
print()

# ==========================================
# 7. BLOCOS COM CLASSES
# ==========================================
print("=" * 50)
print("7. BLOCOS COM CLASSES")
print("=" * 50)
print()

# Exemplo: Classe simples
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}")
        print(f"Tenho {self.idade} anos")
        
        if self.idade >= 18:
            print("Sou maior de idade")
        else:
            print("Sou menor de idade")
    
    def fazer_aniversario(self):
        self.idade += 1
        print(f"Fiz aniversário! Agora tenho {self.idade} anos")

print("Usando classe Pessoa:")
pessoa1 = Pessoa("João", 25)
pessoa1.apresentar()
print()

pessoa1.fazer_aniversario()
print()

# ==========================================
# 8. BLOCOS COM TRY/EXCEPT
# ==========================================
print("=" * 50)
print("8. BLOCOS COM TRY/EXCEPT")
print("=" * 50)
print()

# Exemplo 1: Try/except simples
print("Exemplo 1: Try/except simples")
try:
    numero = int("abc")
    print(f"Número: {numero}")
except ValueError:
    print("Erro: Digite um número válido")

print()

# Exemplo 2: Try/except/else
print("Exemplo 2: Try/except/else")
try:
    numero = int("42")
    print(f"Conversão bem-sucedida: {numero}")
except ValueError:
    print("Erro: Não é um número")
else:
    print(f"Dobrando o número: {numero * 2}")

print()

# Exemplo 3: Try/except/finally
print("Exemplo 3: Try/except/finally")
try:
    lista = [1, 2, 3]
    print(f"Acessando índice 5: {lista[5]}")
except IndexError:
    print("Erro: Índice fora do intervalo")
finally:
    print("Bloco finally sempre é executado")

print()

# ==========================================
# 9. BLOCOS COM COMPREENSÃO DE LISTAS
# ==========================================
print("=" * 50)
print("9. BLOCOS COM COMPREENSÃO DE LISTAS")
print("=" * 50)
print()

# Exemplo 1: Compreensão de lista simples
print("Exemplo 1: Compreensão de lista simples")
numeros = [1, 2, 3, 4, 5]
pares = [n for n in numeros if n % 2 == 0]
print(f"Números: {numeros}")
print(f"Pares: {pares}")

print()

# Exemplo 2: Compreensão com transformação
print("Exemplo 2: Compreensão com transformação")
numeros = [1, 2, 3, 4, 5]
dobrados = [n * 2 for n in numeros]
print(f"Números: {numeros}")
print(f"Dobrados: {dobrados}")

print()

# ==========================================
# 10. ERROS COMUNS DE IDENTAÇÃO
# ==========================================
print("=" * 50)
print("10. ERROS COMUNS DE IDENTAÇÃO")
print("=" * 50)
print()

print("""
ERROS COMUNS:

1. FALTA DE IDENTAÇÃO:
   if idade >= 18:
   print("Maior de idade")  # ❌ ERRO: Falta identação
   
   Correto:
   if idade >= 18:
       print("Maior de idade")  # ✓ OK

2. IDENTAÇÃO INCONSISTENTE:
   if numero > 0:
       print("Positivo")
      print("Continue")  # ❌ ERRO: Identação inconsistente
   
   Correto:
   if numero > 0:
       print("Positivo")
       print("Continue")  # ✓ OK

3. ESPAÇOS vs TABS (Misturar):
   if condicao:
       print("ok")      # 4 espaços
   	print("erro")   # tab (misturado) ❌
   
   Dica: Use sempre ESPAÇOS (4 espaços recomendado)

4. IDENTAÇÃO DESNECESSÁRIA:
   print("Início")
       print("Erro")  # ❌ ERRO: Identação no nível raiz
   print("Fim")
   
   Correto:
   print("Início")
   print("ok")  # ✓ OK
   print("Fim")
""")

print()

# ==========================================
# 11. BOAS PRÁTICAS DE IDENTAÇÃO
# ==========================================
print("=" * 50)
print("11. BOAS PRÁTICAS DE IDENTAÇÃO")
print("=" * 50)
print()

print("""
RECOMENDAÇÕES:

1. Use 4 ESPAÇOS para cada nível de identação
   (padrão PEP 8 - Guia de estilo Python)

2. Nunca misture ESPAÇOS e TABS

3. Mantenha a identação consistente em todo arquivo

4. Use um editor que mostre espaços/tabs (VS Code, PyCharm, etc.)

5. Limite a aninhamento a 3-4 níveis (refatore se necessário)

6. Use PASS para bloco vazio:
   if condicao:
       pass  # Implementar depois

7. Documente blocos complexos com comentários
""")

print()

# ==========================================
# 12. EXEMPLO PRÁTICO COMPLETO
# ==========================================
print("=" * 50)
print("12. EXEMPLO PRÁTICO COMPLETO")
print("=" * 50)
print()

def processar_alunos(alunos):
    """
    Processa lista de alunos e classifica suas notas.
    Exemplo de função com múltiplos níveis de identação.
    """
    print("Processando alunos...\n")
    
    for aluno in alunos:
        nome = aluno["nome"]
        nota = aluno["nota"]
        
        print(f"Aluno: {nome}")
        
        # Determinar conceito
        if nota >= 9:
            conceito = "A"
            status = "Excelente"
        elif nota >= 7:
            conceito = "B"
            status = "Bom"
        elif nota >= 5:
            conceito = "C"
            status = "Satisfatório"
        else:
            conceito = "D"
            status = "Insuficiente"
        
        # Determinar ação
        try:
            if nota >= 7:
                print(f"  Conceito: {conceito}")
                print(f"  Status: {status}")
                print(f"  ✓ Aprovado\n")
            else:
                print(f"  Conceito: {conceito}")
                print(f"  Status: {status}")
                print(f"  ✗ Reprovado\n")
        except Exception as e:
            print(f"  Erro ao processar: {e}\n")

# Usando a função
alunos_lista = [
    {"nome": "João", "nota": 8.5},
    {"nome": "Maria", "nota": 9.0},
    {"nome": "Pedro", "nota": 5.5}
]

processar_alunos(alunos_lista)

# ==========================================
# RESUMO SOBRE IDENTAÇÃO E BLOCOS
# ==========================================
print("=" * 50)
print("RESUMO SOBRE IDENTAÇÃO E BLOCOS")
print("=" * 50)
print("""
IDENTAÇÃO:
- Define blocos de código em Python
- Use 4 espaços por nível
- Não misture espaços e tabs
- Obrigatória após : (dois-pontos)

BLOCOS:
- if/elif/else
- for
- while
- def (função)
- class (classe)
- try/except/finally
- with (gerenciador de contexto)
- Compreensões (list, dict, set)

ESTRUTURA:
1. Declare a instrução (if, for, def, etc.)
2. Termine com : (dois-pontos)
3. Pressione Enter e aumente identação
4. Escreva o código do bloco
5. Diminua identação para voltar ao nível anterior

DICA IMPORTANTE:
Python FORÇA você a escrever código bem identado
Isso resulta em código mais legível e organizado!
""")
 