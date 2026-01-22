# ===== FUNÇÕES EM PYTHON: DIDÁTICAS E PROFISSIONAIS =====

print("=" * 80)
print("FUNÇÕES EM PYTHON: GUIA COMPLETO")
print("=" * 80)

# ===== 1. FUNÇÃO BÁSICA =====
print("\n1. FUNÇÃO BÁSICA")
print("-" * 80)
print("Sintaxe: def nome_funcao():\n    corpo\n")

def saudacao():
    """Função simples que imprime uma saudação"""
    print("Olá, bem-vindo!")

print("Chamando saudacao():")
saudacao()

# Docstring (documentação)
print(f"\nDocstring: {saudacao.__doc__}")


# ===== 2. FUNÇÃO COM PARÂMETROS =====
print("\n2. FUNÇÃO COM PARÂMETROS")
print("-" * 80)

def apresentar(nome, idade):
    """Função que recebe parâmetros"""
    print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

apresentar("João", 25)
apresentar("Maria", 30)

# Com palavras-chave
apresentar(idade=28, nome="Pedro")


# ===== 3. PARÂMETROS COM VALORES PADRÃO =====
print("\n3. PARÂMETROS COM VALORES PADRÃO")
print("-" * 80)

def criar_usuario(nome, email="não informado", ativo=True):
    """Função com parâmetros opcionais"""
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"Ativo: {ativo}")

print("Chamada 1:")
criar_usuario("Alice")

print("\nChamada 2:")
criar_usuario("Bob", "bob@email.com")

print("\nChamada 3:")
criar_usuario("Carol", "carol@email.com", False)


# ===== 4. FUNÇÃO COM RETORNO =====
print("\n4. FUNÇÃO COM RETORNO")
print("-" * 80)

def somar(a, b):
    """Função que retorna um valor"""
    resultado = a + b
    return resultado

resultado = somar(10, 20)
print(f"somar(10, 20) = {resultado}")

# Retorno múltiplo
def dividir_com_resto(a, b):
    """Retorna quociente e resto"""
    quociente = a // b
    resto = a % b
    return quociente, resto

q, r = dividir_com_resto(17, 5)
print(f"\ndividir_com_resto(17, 5): quociente={q}, resto={r}")


# ===== 5. *ARGS - NÚMERO VARIÁVEL DE ARGUMENTOS =====
print("\n5. *ARGS - NÚMERO VARIÁVEL DE ARGUMENTOS")
print("-" * 80)

def somar_varios(*numeros):
    """Função que aceita número variável de argumentos"""
    print(f"Argumentos recebidos: {numeros}")
    print(f"Tipo: {type(numeros)}")
    total = sum(numeros)
    return total

resultado = somar_varios(1, 2, 3)
print(f"somar_varios(1, 2, 3) = {resultado}")

resultado = somar_varios(10, 20, 30, 40, 50)
print(f"somar_varios(10, 20, 30, 40, 50) = {resultado}")

# Desempacotando lista
numeros = [5, 10, 15, 20]
resultado = somar_varios(*numeros)
print(f"somar_varios(*[5, 10, 15, 20]) = {resultado}")


# ===== 6. **KWARGS - ARGUMENTOS NOMEADOS VARIÁVEIS =====
print("\n6. **KWARGS - ARGUMENTOS NOMEADOS VARIÁVEIS")
print("-" * 80)

def criar_perfil(**dados):
    """Função que aceita argumentos nomeados variáveis"""
    print(f"Dados recebidos: {dados}")
    print(f"Tipo: {type(dados)}")
    for chave, valor in dados.items():
        print(f"  {chave}: {valor}")

print("Chamada com diferentes argumentos:")
criar_perfil(nome="João", idade=25, email="joao@email.com", cidade="São Paulo")

# Desempacotando dicionário
dados = {"nome": "Maria", "idade": 30, "profissao": "Engenheira"}
print("\nUsando dicionário com **:")
criar_perfil(**dados)


# ===== 7. *ARGS E **KWARGS JUNTOS =====
print("\n7. *ARGS E **KWARGS JUNTOS")
print("-" * 80)

def funcao_flexivel(a, b, *args, **kwargs):
    """Função com parâmetros fixos, variáveis e nomeados"""
    print(f"Parâmetro a: {a}")
    print(f"Parâmetro b: {b}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

print("Chamada:")
funcao_flexivel(1, 2, 3, 4, 5, nome="João", idade=25)

# Padrão em desenvolvimento profissional
def processar_requisicao(usuario_id, *filtros, **opcoes):
    """Simula processamento com opções flexíveis"""
    print(f"Processando usuário: {usuario_id}")
    if filtros:
        print(f"Filtros aplicados: {filtros}")
    if opcoes:
        print(f"Opções: {opcoes}")

print("\nExemplo profissional:")
processar_requisicao(123, "ativo", "premium", ordenar="data", limite=10)


# ===== 8. ESCOPO DE VARIÁVEIS =====
print("\n8. ESCOPO DE VARIÁVEIS")
print("-" * 80)

x = "Global"

def funcao_escopo():
    x = "Local"  # Variável local
    print(f"Dentro da função: {x}")

print(f"Fora da função: {x}")
funcao_escopo()
print(f"Depois da função: {x}")

# Modificar variável global com 'global'
contador = 0

def incrementar():
    global contador
    contador += 1
    return contador

print(f"\nContador inicial: {contador}")
print(f"Depois de incrementar: {incrementar()}")
print(f"Depois de incrementar: {incrementar()}")
print(f"Valor de contador: {contador}")


# ===== 9. FUNÇÃO ANINHADA (NESTED) =====
print("\n9. FUNÇÃO ANINHADA (NESTED)")
print("-" * 80)

def saudacao_completa(nome):
    """Função com função aninhada"""
    
    def apresentar():
        print(f"Meu nome é {nome}")
    
    def idade_em_ano(ano_nascimento):
        ano_atual = 2026
        return ano_atual - ano_nascimento
    
    apresentar()
    print(f"Nasci em: {idade_em_ano(2000)} anos atrás")

saudacao_completa("Alice")


# ===== 10. CLOSURE =====
print("\n10. CLOSURE")
print("-" * 80)

def criar_multiplicador(fator):
    """Função que retorna outra função (closure)"""
    def multiplicar(numero):
        return numero * fator
    return multiplicar

vezes_2 = criar_multiplicador(2)
vezes_3 = criar_multiplicador(3)

print(f"vezes_2(10) = {vezes_2(10)}")
print(f"vezes_3(10) = {vezes_3(10)}")

# Aplicação profissional: factory
def criar_validador(minimo, maximo):
    """Factory que cria validadores"""
    def validar(valor):
        return minimo <= valor <= maximo
    return validar

validador_idade = criar_validador(0, 150)
validador_nota = criar_validador(0, 10)

print(f"\nValidador de idade (0-150):")
print(f"  18: {validador_idade(18)}")
print(f"  200: {validador_idade(200)}")


# ===== 11. DECORADOR (DECORATOR) =====
print("\n11. DECORADOR (DECORATOR)")
print("-" * 80)

def meu_decorador(funcao):
    """Decorador que adiciona funcionalidade"""
    def wrapper(*args, **kwargs):
        print("--- Antes de executar a função ---")
        resultado = funcao(*args, **kwargs)
        print("--- Depois de executar a função ---")
        return resultado
    return wrapper

@meu_decorador
def saudar(nome):
    print(f"Olá, {nome}!")
    return f"Saudação para {nome}"

print("Função decorada:")
resultado = saudar("João")

# Decorador com temporizador
import time

def cronometro(funcao):
    """Decorador que mede tempo de execução"""
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

@cronometro
def tarefa_lenta():
    time.sleep(1)
    print("Tarefa concluída!")

print("\nDecorador com cronômetro:")
tarefa_lenta()

# Decorador com validação
def requer_positivo(funcao):
    """Decorador que valida argumentos positivos"""
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                print("Erro: Argumento deve ser positivo!")
                return None
        return funcao(*args, **kwargs)
    return wrapper

@requer_positivo
def calcular_raiz_quadrada(numero):
    return numero ** 0.5

print(f"\ncalcular_raiz_quadrada(16) = {calcular_raiz_quadrada(16)}")
print(f"calcular_raiz_quadrada(-4): {calcular_raiz_quadrada(-4)}")


# ===== 12. FUNÇÃO LAMBDA =====
print("\n12. FUNÇÃO LAMBDA")
print("-" * 80)

# Lambda simples
quadrado = lambda x: x ** 2
print(f"lambda x: x ** 2")
print(f"quadrado(5) = {quadrado(5)}")

# Lambda com múltiplos argumentos
somar = lambda x, y: x + y
print(f"\nlambda x, y: x + y")
print(f"somar(3, 7) = {somar(3, 7)}")

# Lambda com condição
maior = lambda x, y: x if x > y else y
print(f"\nlambda x, y: x if x > y else y")
print(f"maior(10, 20) = {maior(10, 20)}")


# ===== 13. MAP, FILTER, REDUCE =====
print("\n13. MAP, FILTER, REDUCE")
print("-" * 80)

numeros = [1, 2, 3, 4, 5]
print(f"Lista original: {numeros}")

# MAP - Aplica função a cada elemento
quadrados = list(map(lambda x: x ** 2, numeros))
print(f"\nmap(lambda x: x ** 2): {quadrados}")

# FILTER - Filtra elementos
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"filter(lambda x: x % 2 == 0): {pares}")

# REDUCE - Reduz a uma único valor
from functools import reduce

produto = reduce(lambda x, y: x * y, numeros)
print(f"reduce(lambda x, y: x * y): {produto}")

soma = reduce(lambda x, y: x + y, numeros)
print(f"reduce(lambda x, y: x + y): {soma}")


# ===== 14. COMPREENSÃO DE LISTA (LIST COMPREHENSION) =====
print("\n14. COMPREENSÃO DE LISTA")
print("-" * 80)

numeros = [1, 2, 3, 4, 5]

# Equivalente ao map
quadrados = [x ** 2 for x in numeros]
print(f"[x ** 2 for x in numeros]: {quadrados}")

# Equivalente ao filter
pares = [x for x in numeros if x % 2 == 0]
print(f"[x for x in numeros if x % 2 == 0]: {pares}")

# Map + Filter
quadrados_pares = [x ** 2 for x in numeros if x % 2 == 0]
print(f"[x ** 2 for x in numeros if x % 2 == 0]: {quadrados_pares}")


# ===== 15. GENERATOR COM YIELD =====
print("\n15. GENERATOR COM YIELD")
print("-" * 80)

def contador(inicio, fim):
    """Generator que conta de inicio até fim"""
    numero = inicio
    while numero <= fim:
        print(f"  Gerando: {numero}")
        yield numero
        numero += 1

print("Usando generator:")
for num in contador(1, 3):
    print(f"  Recebido: {num}")

# Generator com Fibonacci
def fibonacci(n):
    """Generator para sequência de Fibonacci"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("\nFibonacci (primeiros 8 números):")
print(list(fibonacci(8)))

# Vantagem: economia de memória
def numeros_pares_infinito():
    """Generator infinito de números pares"""
    numero = 0
    while True:
        yield numero
        numero += 2

print("\nPrimeiros 5 números pares (generator infinito):")
gerador = numeros_pares_infinito()
for _ in range(5):
    print(f"  {next(gerador)}")


# ===== 16. TYPE HINTS (ANOTAÇÕES DE TIPO) =====
print("\n16. TYPE HINTS (ANOTAÇÕES DE TIPO)")
print("-" * 80)

# Função com type hints
def somar_tipos(a: int, b: int) -> int:
    """Função com anotações de tipo
    
    Args:
        a: Primeiro número inteiro
        b: Segundo número inteiro
    
    Returns:
        A soma de a e b (inteiro)
    """
    return a + b

resultado = somar_tipos(5, 10)
print(f"somar_tipos(5, 10): {resultado}")

# Type hints com tipos complexos
from typing import List, Dict, Optional, Union

def processar_nomes(nomes: List[str]) -> Dict[str, int]:
    """Processa lista de nomes e retorna dicionário de contagem"""
    contagem = {}
    for nome in nomes:
        contagem[nome] = contagem.get(nome, 0) + 1
    return contagem

resultado = processar_nomes(["João", "Maria", "João", "Pedro"])
print(f"\nprocessar_nomes: {resultado}")

# Optional - pode retornar None
def encontrar_usuario(usuario_id: int) -> Optional[Dict[str, str]]:
    """Tenta encontrar usuário, retorna None se não existe"""
    usuarios = {1: {"nome": "João"}, 2: {"nome": "Maria"}}
    return usuarios.get(usuario_id)

print(f"encontrar_usuario(1): {encontrar_usuario(1)}")
print(f"encontrar_usuario(999): {encontrar_usuario(999)}")


# ===== 17. FUNÇÃO RECURSIVA =====
print("\n17. FUNÇÃO RECURSIVA")
print("-" * 80)

def fatorial(n: int) -> int:
    """Calcula fatorial de forma recursiva"""
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

print(f"fatorial(5) = {fatorial(5)}")
print(f"fatorial(10) = {fatorial(10)}")

# Recursiva com memoização (cache)
def fibonacci_recursivo(n: int, cache: Dict = {}) -> int:
    """Fibonacci recursivo com cache"""
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci_recursivo(n - 1, cache) + fibonacci_recursivo(n - 2, cache)
    return cache[n]

print(f"\nfibonacci_recursivo(10) = {fibonacci_recursivo(10)}")


# ===== 18. EXEMPLO PROFISSIONAL 1: VALIDADOR =====
print("\n18. EXEMPLO PROFISSIONAL 1: VALIDADOR")
print("-" * 80)

def validar_email(email: str) -> bool:
    """Valida se email tem formato correto"""
    return "@" in email and "." in email.split("@")[-1]

def validar_senha(senha: str) -> bool:
    """Valida força da senha"""
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_tamanho = len(senha) >= 8
    return tem_maiuscula and tem_minuscula and tem_numero and tem_tamanho

def registrar_usuario(nome: str, email: str, senha: str) -> Dict[str, Union[bool, str]]:
    """Registra usuário com validações"""
    erros = []
    
    if not nome or len(nome) < 3:
        erros.append("Nome deve ter pelo menos 3 caracteres")
    
    if not validar_email(email):
        erros.append("Email inválido")
    
    if not validar_senha(senha):
        erros.append("Senha deve ter maiúscula, minúscula, número e 8+ caracteres")
    
    return {
        "sucesso": len(erros) == 0,
        "erros": erros if erros else "Usuário registrado com sucesso!"
    }

print("Teste 1 - Dados válidos:")
resultado = registrar_usuario("João Silva", "joao@email.com", "Senha123")
print(f"  {resultado}")

print("\nTeste 2 - Email inválido:")
resultado = registrar_usuario("Maria", "maria.invalido", "Senha123")
print(f"  {resultado}")


# ===== 19. EXEMPLO PROFISSIONAL 2: DECORADOR DE RETRY =====
print("\n19. EXEMPLO PROFISSIONAL 2: DECORADOR DE RETRY")
print("-" * 80)

def retry(tentativas: int = 3, espera: float = 1):
    """Decorador que tenta executar função múltiplas vezes"""
    def decorador(funcao):
        def wrapper(*args, **kwargs):
            ultima_excecao = None
            for tentativa in range(1, tentativas + 1):
                try:
                    print(f"Tentativa {tentativa}...")
                    return funcao(*args, **kwargs)
                except Exception as e:
                    ultima_excecao = e
                    print(f"  Erro: {e}")
                    if tentativa < tentativas:
                        time.sleep(espera)
            raise ultima_excecao
        return wrapper
    return decorador

contador_chamadas = 0

@retry(tentativas=3, espera=0.5)
def funcao_instavel():
    """Função que falha aleatoriamente"""
    import random
    global contador_chamadas
    contador_chamadas += 1
    
    if contador_chamadas < 2:
        raise Exception("Falha simulada!")
    return "Sucesso na terceira tentativa!"

print("Testando decorador de retry:")
try:
    resultado = funcao_instavel()
    print(f"Resultado: {resultado}")
except Exception as e:
    print(f"Falha final: {e}")


# ===== 20. EXEMPLO PROFISSIONAL 3: PROCESSADOR DE DADOS =====
print("\n20. EXEMPLO PROFISSIONAL 3: PROCESSADOR DE DADOS")
print("-" * 80)

from typing import Callable, Any

def criar_pipeline(*funcoes: Callable) -> Callable:
    """Cria pipeline de funções"""
    def executar(valor: Any) -> Any:
        for funcao in funcoes:
            valor = funcao(valor)
        return valor
    return executar

# Funções de transformação
def remover_espacos(texto: str) -> str:
    return texto.strip()

def converter_maiuscula(texto: str) -> str:
    return texto.upper()

def remover_caracteres_especiais(texto: str) -> str:
    import string
    return "".join(c for c in texto if c.isalnum() or c.isspace())

def limitar_comprimento(texto: str, comprimento: int = 20) -> str:
    return texto[:comprimento]

# Criar pipeline
processar_nome = criar_pipeline(
    remover_espacos,
    converter_maiuscula,
    remover_caracteres_especiais
)

print("Pipeline de processamento:")
entrada = "  João Silva @@ "
print(f"Entrada: '{entrada}'")
print(f"Saída: '{processar_nome(entrada)}'")


# ===== 21. EXEMPLO PROFISSIONAL 4: CACHE COM DECORADOR =====
print("\n21. EXEMPLO PROFISSIONAL 4: CACHE COM DECORADOR")
print("-" * 80)

def cache_resultado(funcao: Callable) -> Callable:
    """Decorador que cacheia resultados de função"""
    cache = {}
    
    def wrapper(*args, **kwargs):
        # Criar chave do cache
        chave = (args, tuple(sorted(kwargs.items())))
        
        if chave in cache:
            print(f"  (Do cache)")
            return cache[chave]
        
        resultado = funcao(*args, **kwargs)
        cache[chave] = resultado
        return resultado
    
    wrapper.cache = cache
    return wrapper

@cache_resultado
def fibonacci_cacheado(n: int) -> int:
    """Fibonacci com cache automático"""
    if n <= 1:
        return n
    return fibonacci_cacheado(n - 1) + fibonacci_cacheado(n - 2)

print("Fibonacci com cache:")
print(f"fibonacci_cacheado(20) = {fibonacci_cacheado(20)}")
print(f"fibonacci_cacheado(25) = {fibonacci_cacheado(25)}")


# ===== 22. RESUMO E BOAS PRÁTICAS =====
print("\n22. RESUMO E BOAS PRÁTICAS")
print("-" * 80)

print("""
REGRAS DE OURO PARA FUNÇÕES:

1. NOMES DESCRITIVOS
   ✓ def calcular_media(notas)
   ✗ def calc(n)

2. UMA FUNÇÃO = UM OBJETIVO
   ✓ Fazer apenas uma coisa e fazer bem
   ✗ Misturar múltiplas responsabilidades

3. DOCUMENTAÇÃO
   ✓ Usar docstrings para explicar
   ✗ Deixar sem explicação

4. PARÂMETROS
   ✓ Máximo 3-4 parâmetros
   ✗ Mais de 10 parâmetros (use objeto)

5. RETORNO
   ✓ Sempre retornar algo significativo
   ✗ Retornar None sem motivo

6. TYPE HINTS
   ✓ Usar para melhor IDE support
   ✗ Deixar sem anotações

7. TRATAMENTO DE ERROS
   ✓ Capturar exceções esperadas
   ✗ Deixar código quebrar

8. TESTES
   ✓ Testar diferentes cenários
   ✗ Sem testes

QUANDO USAR O QUÊ:

• Função simples → def
• Transformação rápida → lambda
• Múltiplos valores → generator (yield)
• Adicionar comportamento → decorador
• Processamento em série → pipeline
• Cache automático → functools.lru_cache
• Validação → decorator
""")

print("\n" + "=" * 80)
print("FIM DO GUIA DE FUNÇÕES")
print("=" * 80)
