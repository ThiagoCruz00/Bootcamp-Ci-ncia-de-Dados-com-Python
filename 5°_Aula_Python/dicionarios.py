# ===== DICIONÁRIOS EM PYTHON: CRIAÇÃO E ACESSO =====

print("=" * 70)
print("DICIONÁRIOS: CRIAÇÃO E ACESSO AOS DADOS")
print("=" * 70)

# ===== 1. O QUE SÃO DICIONÁRIOS? =====
print("\n1. O QUE SÃO DICIONÁRIOS?")
print("-" * 70)
print("Dicionários são coleções de pares CHAVE:VALOR")
print("Sintaxe: {chave1: valor1, chave2: valor2, ...}")
print("Características:")
print("  • Dados organizados por chave (não por índice)")
print("  • Chaves devem ser ÚNICAS")
print("  • Mutável (pode adicionar, remover, modificar)")
print("  • Ordenado (desde Python 3.7)")
print("  • Chaves devem ser imutáveis (int, str, tuple)")
print("  • Valores podem ser de qualquer tipo\n")


# ===== 2. CRIANDO DICIONÁRIOS =====
print("2. CRIANDO DICIONÁRIOS")
print("-" * 70)

# Dicionário vazio
dicionario_vazio = {}
print(f"Dicionário vazio: {dicionario_vazio}")
print(f"Tipo: {type(dicionario_vazio)}\n")

# Dicionário com números (chave: valor)
numeros = {1: "um", 2: "dois", 3: "três"}
print(f"Dicionário de números: {numeros}")

# Dicionário com strings
pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}
print(f"\nDicionário de pessoa: {pessoa}")

# Dicionário com valores de diferentes tipos
dados_mistos = {
    "nome": "Maria",
    "idade": 30,
    "altura": 1.70,
    "estudante": True,
    "notas": [8.5, 9.0, 7.5]
}
print(f"\nDicionário com tipos mistos: {dados_mistos}")

# Dicionário aninhado (dicionário dentro de dicionário)
alunos = {
    "aluno1": {
        "nome": "João",
        "idade": 20,
        "nota": 8.5
    },
    "aluno2": {
        "nome": "Maria",
        "idade": 21,
        "nota": 9.0
    }
}
print(f"\nDicionário aninhado (alunos): {alunos}")

# Usando função dict()
dicionario_com_funcao = dict(nome="Pedro", idade=25, cidade="Rio")
print(f"\nUsando dict(): {dicionario_com_funcao}")

# Usando dict() com lista de tuplas
dicionario_de_tuplas = dict([("chave1", "valor1"), ("chave2", "valor2")])
print(f"Dict de lista de tuplas: {dicionario_de_tuplas}")

# Usando dict.fromkeys() - todas as chaves com mesmo valor
dicionario_chaves = dict.fromkeys(["a", "b", "c"], 0)
print(f"\ndict.fromkeys(['a', 'b', 'c'], 0): {dicionario_chaves}")


# ===== 3. ACESSANDO VALORES PELA CHAVE =====
print("\n3. ACESSANDO VALORES PELA CHAVE")
print("-" * 70)

pessoa = {
    "nome": "João",
    "idade": 25,
    "profissao": "Engenheiro",
    "cidade": "São Paulo"
}
print(f"Dicionário: {pessoa}\n")

# Acessar com []
nome = pessoa["nome"]
print(f"pessoa['nome'] = {nome}")

idade = pessoa["idade"]
print(f"pessoa['idade'] = {idade}")

profissao = pessoa["profissao"]
print(f"pessoa['profissao'] = {profissao}")

# Acessar com get() - mais seguro
print(f"\nUsando get():")
print(f"pessoa.get('nome') = {pessoa.get('nome')}")
print(f"pessoa.get('idade') = {pessoa.get('idade')}")

# Diferença: [] gera erro, get() retorna None
print(f"\nTentando acessar chave que não existe:")
print(f"pessoa.get('telefone') = {pessoa.get('telefone')}")
print(f"pessoa.get('telefone', 'não informado') = {pessoa.get('telefone', 'não informado')}")

print("\nUsando []:")
try:
    print(pessoa["telefone"])
except KeyError:
    print("Erro: Chave 'telefone' não existe!")


# ===== 4. VERIFICAR CHAVES =====
print("\n4. VERIFICAR CHAVES")
print("-" * 70)

carro = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2020,
    "cor": "Azul"
}
print(f"Dicionário: {carro}\n")

# Verificar se chave existe com 'in'
print(f"'marca' in carro: {'marca' in carro}")
print(f"'velocidade' in carro: {'velocidade' in carro}")

print(f"\n'modelo' in carro: {'modelo' in carro}")
print(f"'motor' in carro: {'motor' in carro}")

# Verificar se chave NÃO existe com 'not in'
print(f"\n'velocidade' not in carro: {'velocidade' not in carro}")
print(f"'marca' not in carro: {'marca' not in carro}")


# ===== 5. ACESSAR CHAVES, VALORES E ITENS =====
print("\n5. ACESSAR CHAVES, VALORES E ITENS")
print("-" * 70)

empresa = {
    "nome": "TechCorp",
    "funcionarios": 150,
    "setor": "Tecnologia",
    "fundacao": 2010
}
print(f"Dicionário: {empresa}\n")

# Obter todas as chaves
chaves = empresa.keys()
print(f"Chaves (keys()): {chaves}")
print(f"Tipo: {type(chaves)}")

# Obter todos os valores
valores = empresa.values()
print(f"\nValores (values()): {valores}")
print(f"Tipo: {type(valores)}")

# Obter todos os itens (pares chave-valor)
itens = empresa.items()
print(f"\nItens (items()): {itens}")
print(f"Tipo: {type(itens)}")

# Converter para lista
print(f"\nConvertendo para listas:")
print(f"list(keys()): {list(empresa.keys())}")
print(f"list(values()): {list(empresa.values())}")
print(f"list(items()): {list(empresa.items())}")


# ===== 6. ITERANDO SOBRE DICIONÁRIOS =====
print("\n6. ITERANDO SOBRE DICIONÁRIOS")
print("-" * 70)

produto = {
    "nome": "Notebook",
    "preco": 3000,
    "marca": "Dell",
    "em_estoque": True
}
print(f"Dicionário: {produto}\n")

# Iterar sobre chaves
print("Iterando sobre CHAVES:")
for chave in produto:
    print(f"  {chave}")

# Iterar sobre keys()
print("\nIterando sobre keys():")
for chave in produto.keys():
    print(f"  {chave}")

# Iterar sobre valores
print("\nIterando sobre VALUES:")
for valor in produto.values():
    print(f"  {valor}")

# Iterar sobre itens (chave e valor)
print("\nIterando sobre ITEMS (chave: valor):")
for chave, valor in produto.items():
    print(f"  {chave}: {valor}")

# Iterar com índice
print("\nIterando com índice:")
for i, (chave, valor) in enumerate(produto.items()):
    print(f"  {i}: {chave} = {valor}")


# ===== 7. TAMANHO E ESTRUTURA =====
print("\n7. TAMANHO E ESTRUTURA")
print("-" * 70)

configuracao = {
    "idioma": "Português",
    "tema": "Escuro",
    "notificacoes": True,
    "volume": 80
}
print(f"Dicionário: {configuracao}")

# Tamanho (quantidade de pares chave-valor)
tamanho = len(configuracao)
print(f"\nTamanho (len): {tamanho}")

# Verificar se vazio
print(f"Vazio? {len(configuracao) == 0}")

dicionario_vazio = {}
print(f"\nDicionário vazio: {dicionario_vazio}")
print(f"Vazio? {len(dicionario_vazio) == 0}")


# ===== 8. ACESSAR DICIONÁRIOS ANINHADOS =====
print("\n8. ACESSAR DICIONÁRIOS ANINHADOS")
print("-" * 70)

empresa = {
    "nome": "TechCorp",
    "endereco": {
        "rua": "Avenida Principal",
        "numero": 123,
        "cidade": "São Paulo",
        "cep": "01234-567"
    },
    "contato": {
        "telefone": "(11) 99999-8888",
        "email": "contato@techcorp.com"
    }
}

print(f"Dicionário aninhado:\n{empresa}\n")

# Acessar nível 1
print(f"empresa['nome']: {empresa['nome']}")

# Acessar nível 2
print(f"empresa['endereco']: {empresa['endereco']}")

print(f"\nempreza['endereco']['cidade']: {empresa['endereco']['cidade']}")
print(f"empresa['endereco']['rua']: {empresa['endereco']['rua']}")

print(f"\nempreza['contato']['email']: {empresa['contato']['email']}")
print(f"empresa['contato']['telefone']: {empresa['contato']['telefone']}")

# Com get() para mais segurança
print(f"\nCom get():")
print(f"empresa.get('endereco', {{}}).get('cidade'): {empresa.get('endereco', {}).get('cidade')}")


# ===== 9. MODIFICANDO DICIONÁRIOS =====
print("\n9. MODIFICANDO DICIONÁRIOS")
print("-" * 70)

pessoa = {
    "nome": "João",
    "idade": 25,
    "profissao": "Desenvolvedor"
}
print(f"Dicionário original: {pessoa}")

# Adicionar nova chave
pessoa["cidade"] = "São Paulo"
print(f"Após adicionar 'cidade': {pessoa}")

# Modificar valor existente
pessoa["idade"] = 26
print(f"Após mudar idade para 26: {pessoa}")

# Adicionar múltiplas chaves
pessoa.update({"salario": 5000, "empresa": "TechCorp"})
print(f"Após update com múltiplas chaves: {pessoa}")

# Remover chave com del
del pessoa["salario"]
print(f"Após remover 'salario': {pessoa}")

# Remover e obter valor com pop()
profissao = pessoa.pop("profissao")
print(f"pop('profissao') retornou: {profissao}")
print(f"Dicionário após pop: {pessoa}")

# pop() com valor padrão se chave não existe
valor = pessoa.pop("telefone", "não informado")
print(f"pop('telefone', 'não informado'): {valor}")

# Remover todas as chaves
pessoa_temp = {"a": 1, "b": 2}
print(f"\nAntes de clear(): {pessoa_temp}")
pessoa_temp.clear()
print(f"Após clear(): {pessoa_temp}")


# ===== 10. CÓPIA DE DICIONÁRIOS =====
print("\n10. CÓPIA DE DICIONÁRIOS")
print("-" * 70)

original = {
    "nome": "Maria",
    "idade": 30
}
print(f"Original: {original}")

# Cópia com copy()
copia = original.copy()
copia["idade"] = 31
print(f"\nApós copia['idade'] = 31:")
print(f"  Original: {original} (não modificada)")
print(f"  Cópia: {copia}")

# Referência (sem copy)
original = {"nome": "Pedro", "idade": 25}
referencia = original
referencia["idade"] = 26
print(f"\nReferência (sem copy):")
print(f"  Original: {original}")
print(f"  Referência: {referencia} (são iguais!)")

# Cópia profunda (deep copy)
import copy as modulo_copy

original_aninhado = {
    "pessoa": {
        "nome": "Ana",
        "idade": 28
    }
}
print(f"\nDicionário aninhado original: {original_aninhado}")

copia_rasa = original_aninhado.copy()
copia_rasa["pessoa"]["idade"] = 29
print(f"Após copia_rasa modificar idade para 29:")
print(f"  Original: {original_aninhado} (foi modificada!)")
print(f"  Cópia rasa: {copia_rasa}")

original_aninhado = {
    "pessoa": {
        "nome": "Bruno",
        "idade": 28
    }
}
copia_profunda = modulo_copy.deepcopy(original_aninhado)
copia_profunda["pessoa"]["idade"] = 29
print(f"\nCom deepcopy:")
print(f"  Original: {original_aninhado} (não foi modificada)")
print(f"  Cópia profunda: {copia_profunda}")


# ===== 11. VALORES PADRÃO COM setdefault() =====
print("\n11. VALORES PADRÃO COM setdefault()")
print("-" * 70)

produto = {
    "nome": "Teclado",
    "preco": 150
}
print(f"Dicionário: {produto}\n")

# setdefault() retorna valor se chave existe
valor = produto.setdefault("nome", "Sem nome")
print(f"setdefault('nome', 'Sem nome'): {valor}")
print(f"Dicionário (não mudou): {produto}")

# setdefault() adiciona se chave NÃO existe
valor = produto.setdefault("marca", "Desconhecida")
print(f"\nsetdefault('marca', 'Desconhecida'): {valor}")
print(f"Dicionário (adicionou 'marca'): {produto}")

# setdefault() com valor padrão
valor = produto.setdefault("cor", "Preto")
print(f"setdefault('cor', 'Preto'): {valor}")
print(f"Dicionário: {produto}")


# ===== 12. EXEMPLOS PRÁTICOS =====
print("\n12. EXEMPLOS PRÁTICOS")
print("-" * 70)

print("\n--- Exemplo 1: Dados de um Aluno ---")
aluno = {
    "matricula": 12345,
    "nome": "João Silva",
    "email": "joao@university.com",
    "notas": {
        "português": 8.5,
        "matemática": 9.0,
        "inglês": 7.5
    },
    "ativo": True
}

print(f"Aluno: {aluno['nome']}")
print(f"Matrícula: {aluno['matricula']}")
print(f"Email: {aluno['email']}")
print(f"Ativo: {'Sim' if aluno['ativo'] else 'Não'}")

print(f"\nNotas:")
for disciplina, nota in aluno['notas'].items():
    print(f"  {disciplina}: {nota}")

media = sum(aluno['notas'].values()) / len(aluno['notas'])
print(f"Média: {media:.2f}")

print("\n--- Exemplo 2: Configurações de Aplicação ---")
config = {
    "app": {
        "nome": "MeuApp",
        "versao": "1.0.0",
        "debug": False
    },
    "database": {
        "host": "localhost",
        "porta": 5432,
        "usuario": "admin"
    },
    "features": {
        "login": True,
        "compartilhamento": False,
        "notificacoes": True
    }
}

print(f"Aplicação: {config['app']['nome']} v{config['app']['versao']}")
print(f"Banco de dados: {config['database']['host']}:{config['database']['porta']}")
print(f"\nFeatures ativas:")
for feature, ativa in config['features'].items():
    status = "✓" if ativa else "✗"
    print(f"  {status} {feature}")

print("\n--- Exemplo 3: Contagem de Ocorrências ---")
frutas = ["maçã", "banana", "maçã", "laranja", "banana", "maçã", "uva"]
print(f"Frutas: {frutas}")

contagem = {}
for fruta in frutas:
    if fruta in contagem:
        contagem[fruta] += 1
    else:
        contagem[fruta] = 1

print(f"Contagem:")
for fruta, quantidade in contagem.items():
    print(f"  {fruta}: {quantidade}")


# ===== 13. RESUMO DE MÉTODOS =====
print("\n13. RESUMO DE MÉTODOS DE DICIONÁRIO")
print("-" * 70)

print("\nMétodos principais:\n")
metodos = {
    "keys()": "Retorna todas as chaves",
    "values()": "Retorna todos os valores",
    "items()": "Retorna pares (chave, valor)",
    "get(chave)": "Obtém valor com valor padrão None",
    "pop(chave)": "Remove e retorna valor",
    "popitem()": "Remove e retorna último item",
    "clear()": "Remove todos os itens",
    "update(outro)": "Adiciona/atualiza com outro dicionário",
    "copy()": "Cria cópia rasa",
    "setdefault()": "Obtém ou define valor padrão",
    "fromkeys()": "Cria dicionário com mesmos valores"
}

for metodo, descricao in metodos.items():
    print(f"  {metodo:25} → {descricao}")


# ===== 14. QUANDO USAR DICIONÁRIOS =====
print("\n14. QUANDO USAR DICIONÁRIOS")
print("-" * 70)

print("\nUse DICIONÁRIO quando:")
print("  ✓ Dados são organizados por chave (não por índice)")
print("  ✓ Quer acesso rápido pelos dados (por chave)")
print("  ✓ Dados são pares chave-valor")
print("  ✓ Ordem não é importante (ou é preservada)")
print("  ✓ Quer estrutura semelhante a JSON")

print("\nNÃO use DICIONÁRIO quando:")
print("  ✗ Precisa de ordem específica (use lista ordenada)")
print("  ✗ Elementos devem ser únicos (use conjunto)")
print("  ✗ Dados são sequenciais (use lista ou tupla)")

print("\n" + "=" * 70)
