# ===== MÉTODOS DA CLASSE DICT EM PYTHON =====

print("=" * 70)
print("MÉTODOS DA CLASSE DICT")
print("=" * 70)

# ===== 1. MÉTODO keys() =====
print("\n1. MÉTODO keys()")
print("-" * 70)
print("Sintaxe: dicionario.keys()")
print("Função: Retorna uma visão de todas as chaves")
print("Retorna: dict_keys (semelhante a uma lista)\n")

pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
print(f"Dicionário: {pessoa}")

chaves = pessoa.keys()
print(f"\nkeys(): {chaves}")
print(f"Tipo: {type(chaves)}")

# Converter para lista
chaves_lista = list(pessoa.keys())
print(f"list(keys()): {chaves_lista}")

# Iterar sobre as chaves
print(f"\nIterando:")
for chave in pessoa.keys():
    print(f"  {chave}")

# Verificar se chave existe
print(f"\n'nome' in keys(): {'nome' in pessoa.keys()}")
print(f"'email' in keys(): {'email' in pessoa.keys()}")


# ===== 2. MÉTODO values() =====
print("\n2. MÉTODO values()")
print("-" * 70)
print("Sintaxe: dicionario.values()")
print("Função: Retorna uma visão de todos os valores")
print("Retorna: dict_values (semelhante a uma lista)\n")

produto = {"nome": "Notebook", "preco": 3000, "marca": "Dell"}
print(f"Dicionário: {produto}")

valores = produto.values()
print(f"\nvalues(): {valores}")
print(f"Tipo: {type(valores)}")

# Converter para lista
valores_lista = list(produto.values())
print(f"list(values()): {valores_lista}")

# Iterar sobre os valores
print(f"\nIterando:")
for valor in produto.values():
    print(f"  {valor}")

# Contar valores específicos
valores_totais = list(produto.values())
print(f"\nTotal de valores: {len(valores_totais)}")


# ===== 3. MÉTODO items() =====
print("\n3. MÉTODO items()")
print("-" * 70)
print("Sintaxe: dicionario.items()")
print("Função: Retorna uma visão de todos os pares (chave, valor)")
print("Retorna: dict_items (semelhante a lista de tuplas)\n")

carro = {"marca": "Toyota", "modelo": "Corolla", "ano": 2020}
print(f"Dicionário: {carro}")

itens = carro.items()
print(f"\nitems(): {itens}")
print(f"Tipo: {type(itens)}")

# Converter para lista
itens_lista = list(carro.items())
print(f"list(items()): {itens_lista}")

# Iterar sobre items
print(f"\nIterando sobre items:")
for chave, valor in carro.items():
    print(f"  {chave}: {valor}")

# Desempacotamento em loop
print(f"\nDesempacotando chave e valor:")
for k, v in carro.items():
    print(f"  Chave='{k}' → Valor='{v}'")


# ===== 4. MÉTODO get() =====
print("\n4. MÉTODO get()")
print("-" * 70)
print("Sintaxe: dicionario.get(chave, valor_padrao)")
print("Função: Obtém valor de uma chave com valor padrão se não existir")
print("Retorna: O valor ou None (ou valor_padrao)\n")

configuracao = {"tema": "escuro", "idioma": "português"}
print(f"Dicionário: {configuracao}")

# get com chave existente
valor = configuracao.get("tema")
print(f"\nget('tema'): {valor}")

valor = configuracao.get("idioma")
print(f"get('idioma'): {valor}")

# get com chave inexistente (retorna None)
valor = configuracao.get("volume")
print(f"get('volume'): {valor}")

# get com valor padrão
valor = configuracao.get("volume", 50)
print(f"get('volume', 50): {valor}")

valor = configuracao.get("notificacoes", True)
print(f"get('notificacoes', True): {valor}")

# Segurança: get() vs [] 
print(f"\nComparação de segurança:")
print(f"[] com chave inexistente:")
try:
    print(configuracao["email"])
except KeyError as e:
    print(f"  Erro: {e}")

print(f"get() com chave inexistente:")
print(f"  {configuracao.get('email')} (sem erro)")


# ===== 5. MÉTODO pop() =====
print("\n5. MÉTODO pop()")
print("-" * 70)
print("Sintaxe: dicionario.pop(chave, valor_padrao)")
print("Função: Remove e retorna o valor de uma chave")
print("Retorna: O valor removido\n")

dados = {"nome": "Maria", "idade": 30, "profissao": "Engenheira"}
print(f"Dicionário: {dados}")

# pop com chave existente
valor = dados.pop("profissao")
print(f"\npop('profissao'): {valor}")
print(f"Dicionário após pop: {dados}")

# pop com chave inexistente e valor padrão
valor = dados.pop("email", "não informado")
print(f"\npop('email', 'não informado'): {valor}")
print(f"Dicionário (não mudou): {dados}")

# pop sem valor padrão (gera erro se não existe)
print(f"\nTentando fazer pop de chave inexistente sem valor padrão:")
try:
    dados.pop("telefone")
except KeyError as e:
    print(f"Erro: {e}")


# ===== 6. MÉTODO popitem() =====
print("\n6. MÉTODO popitem()")
print("-" * 70)
print("Sintaxe: dicionario.popitem()")
print("Função: Remove e retorna o último par (chave, valor)")
print("Retorna: Uma tupla (chave, valor) do último item\n")

cores = {"vermelho": "#FF0000", "verde": "#00FF00", "azul": "#0000FF"}
print(f"Dicionário: {cores}")

# popitem remove o último
chave, valor = cores.popitem()
print(f"\npopitem(): ({chave}, {valor})")
print(f"Dicionário após popitem: {cores}")

chave, valor = cores.popitem()
print(f"popitem(): ({chave}, {valor})")
print(f"Dicionário após popitem: {cores}")

# popitem em dicionário vazio gera erro
print(f"\nTentando popitem em dicionário vazio:")
try:
    {}.popitem()
except KeyError as e:
    print(f"Erro: {e}")


# ===== 7. MÉTODO clear() =====
print("\n7. MÉTODO clear()")
print("-" * 70)
print("Sintaxe: dicionario.clear()")
print("Função: Remove todos os itens do dicionário")
print("Retorna: None\n")

lista_compras = {"pão": 2, "leite": 1, "ovos": 12}
print(f"Dicionário: {lista_compras}")
print(f"Tamanho: {len(lista_compras)}")

lista_compras.clear()
print(f"\nApós clear(): {lista_compras}")
print(f"Tamanho: {len(lista_compras)}")


# ===== 8. MÉTODO update() =====
print("\n8. MÉTODO update()")
print("-" * 70)
print("Sintaxe: dicionario.update(outro_dict ou pares_chave_valor)")
print("Função: Adiciona/atualiza múltiplos pares chave-valor")
print("Retorna: None (modifica o dicionário original)\n")

preferencias = {"cor": "azul", "tamanho": "grande"}
print(f"Dicionário original: {preferencias}")

# update com outro dicionário
novas_preferencias = {"cor": "vermelho", "tema": "escuro"}
preferencias.update(novas_preferencias)
print(f"Após update({'cor': 'vermelho', 'tema': 'escuro'}): {preferencias}")

# update com pares chave-valor
preferencias = {"cor": "azul", "tamanho": "grande"}
preferencias.update(velocidade=100, brilho=80)
print(f"\nApós update(velocidade=100, brilho=80): {preferencias}")

# update com lista de tuplas
preferencias = {"cor": "azul"}
preferencias.update([("tamanho", "grande"), ("peso", 5)])
print(f"Após update([('tamanho', 'grande'), ('peso', 5)]): {preferencias}")


# ===== 9. MÉTODO copy() =====
print("\n9. MÉTODO copy()")
print("-" * 70)
print("Sintaxe: novo_dict = dicionario.copy()")
print("Função: Cria uma cópia rasa do dicionário")
print("Retorna: Um novo dicionário com os mesmos itens\n")

original = {"nome": "João", "idade": 25}
print(f"Original: {original}")

# Cópia
copia = original.copy()
copia["idade"] = 26
print(f"\nApós copia['idade'] = 26:")
print(f"  Original: {original} (não modificada)")
print(f"  Cópia: {copia}")

# Diferença entre = e copy()
print(f"\nDiferença entre = e copy():")
original = {"a": 1, "b": 2}
referencia = original
copia = original.copy()

print(f"Original: {original}")
print(f"Referência: {referencia}")
print(f"Cópia: {copia}")

original["a"] = 999
print(f"\nApós original['a'] = 999:")
print(f"  Original: {original}")
print(f"  Referência: {referencia} (também mudou!)")
print(f"  Cópia: {copia} (não mudou)")


# ===== 10. MÉTODO clear() com CÓPIA PROFUNDA =====
print("\n10. CÓPIA PROFUNDA (deepcopy)")
print("-" * 70)
print("Problema: copy() é rasa (shallow copy)")
print("Solução: Usar copy.deepcopy() para cópia profunda\n")

import copy

original = {
    "pessoa": {
        "nome": "Maria",
        "idade": 30
    },
    "notas": [8.5, 9.0, 7.5]
}
print(f"Dicionário aninhado: {original}")

# Cópia rasa
copia_rasa = original.copy()
copia_rasa["pessoa"]["idade"] = 31
copia_rasa["notas"][0] = 10.0
print(f"\nApós modificar cópia rasa (shallow copy):")
print(f"  Original: {original} (foi modificado!)")

# Cópia profunda
original = {
    "pessoa": {
        "nome": "Pedro",
        "idade": 25
    },
    "notas": [8.5, 9.0, 7.5]
}
copia_profunda = copy.deepcopy(original)
copia_profunda["pessoa"]["idade"] = 26
copia_profunda["notas"][0] = 10.0
print(f"\nApós modificar cópia profunda (deep copy):")
print(f"  Original: {original} (não foi modificado)")
print(f"  Cópia profunda: {copia_profunda}")


# ===== 11. MÉTODO setdefault() =====
print("\n11. MÉTODO setdefault()")
print("-" * 70)
print("Sintaxe: dicionario.setdefault(chave, valor_padrao)")
print("Função: Retorna valor se chave existe, senão adiciona com valor padrão")
print("Retorna: O valor existente ou o valor_padrao\n")

configuracoes = {"idioma": "português"}
print(f"Dicionário: {configuracoes}")

# setdefault com chave existente
valor = configuracoes.setdefault("idioma", "inglês")
print(f"\nsetdefault('idioma', 'inglês'): {valor}")
print(f"Dicionário (não mudou): {configuracoes}")

# setdefault com chave inexistente
valor = configuracoes.setdefault("tema", "claro")
print(f"setdefault('tema', 'claro'): {valor}")
print(f"Dicionário (adicionou 'tema'): {configuracoes}")

# setdefault com valor padrão None
valor = configuracoes.setdefault("notificacoes", None)
print(f"setdefault('notificacoes', None): {valor}")
print(f"Dicionário: {configuracoes}")


# ===== 12. MÉTODO fromkeys() =====
print("\n12. MÉTODO fromkeys()")
print("-" * 70)
print("Sintaxe: dict.fromkeys(chaves, valor_padrao)")
print("Função: Cria novo dicionário com as mesmas chaves e valor padrão")
print("Retorna: Um novo dicionário\n")

# fromkeys com valor padrão
chaves = ["nome", "idade", "cidade"]
novo_dict = dict.fromkeys(chaves, None)
print(f"dict.fromkeys(['nome', 'idade', 'cidade'], None):")
print(f"  {novo_dict}")

# fromkeys com valor padrão 0
numeros = dict.fromkeys(["a", "b", "c"], 0)
print(f"\ndict.fromkeys(['a', 'b', 'c'], 0):")
print(f"  {numeros}")

# fromkeys com string (converte caracteres em chaves)
letras = dict.fromkeys("ABC", 0)
print(f"\ndict.fromkeys('ABC', 0):")
print(f"  {letras}")

# fromkeys com valor padrão que é uma lista (CUIDADO!)
print(f"\nAtenção: Compartilhamento de referência:")
dicts = dict.fromkeys(["d1", "d2", "d3"], [])
dicts["d1"].append(1)
print(f"Após dicts['d1'].append(1):")
print(f"  {dicts} (todas as listas foram modificadas!)")


# ===== 13. MÉTODOS DE COMPARAÇÃO E VERIFICAÇÃO =====
print("\n13. MÉTODOS DE COMPARAÇÃO E VERIFICAÇÃO")
print("-" * 70)

d1 = {"a": 1, "b": 2}
d2 = {"a": 1, "b": 2}
d3 = {"a": 1, "b": 2, "c": 3}

print(f"d1: {d1}")
print(f"d2: {d2}")
print(f"d3: {d3}\n")

# Igualdade
print(f"d1 == d2: {d1 == d2}")
print(f"d1 == d3: {d1 == d3}")
print(f"d1 is d2: {d1 is d2} (referência diferente)")

# Desigualdade
print(f"\nd1 != d3: {d1 != d3}")

# Verificar chave
print(f"\n'a' in d1: {'a' in d1}")
print(f"'z' in d1: {'z' in d1}")

print(f"\n'a' not in d1: {'a' not in d1}")
print(f"'z' not in d1: {'z' not in d1}")

# bool
print(f"\nbool(d1): {bool(d1)}")
print(f"bool({{}}): {bool({})}")

# len
print(f"\nlen(d1): {len(d1)}")
print(f"len(d3): {len(d3)}")


# ===== 14. EXERCÍCIO PRÁTICO 1 =====
print("\n14. EXERCÍCIO PRÁTICO 1: GERENCIADOR DE CONTATOS")
print("-" * 70)

contatos = {}

# Adicionar contatos
contatos.setdefault("João", {})
contatos["João"]["email"] = "joao@email.com"
contatos["João"]["telefone"] = "9999-1111"

contatos.update({
    "Maria": {
        "email": "maria@email.com",
        "telefone": "9999-2222"
    },
    "Pedro": {
        "email": "pedro@email.com",
        "telefone": "9999-3333"
    }
})

print(f"Contatos: {contatos}\n")

# Listar todos
print("Todos os contatos:")
for nome, dados in contatos.items():
    print(f"  {nome}:")
    for chave, valor in dados.items():
        print(f"    {chave}: {valor}")

# Obter contato
print(f"\nTelefone de Maria: {contatos['Maria']['telefone']}")

# Remover contato
removido = contatos.pop("Pedro", None)
print(f"\nRemovido: {removido}")
print(f"Contatos restantes: {list(contatos.keys())}")


# ===== 15. EXERCÍCIO PRÁTICO 2 =====
print("\n15. EXERCÍCIO PRÁTICO 2: SISTEMA DE PONTUAÇÃO")
print("-" * 70)

jogadores = {
    "Alice": 100,
    "Bob": 85,
    "Carol": 92,
    "David": 78
}

print(f"Pontuações: {jogadores}\n")

# Adicionar novo jogador
jogadores.setdefault("Eve", 0)
print(f"Após adicionar Eve: {jogadores}")

# Atualizar pontuações
pontos_atualizados = {"Alice": 110, "Bob": 90}
jogadores.update(pontos_atualizados)
print(f"\nApós atualizar pontos: {jogadores}")

# Encontrar maior pontuação
maior_jogador = max(jogadores, key=jogadores.get)
print(f"\nMaior pontuação: {maior_jogador} com {jogadores[maior_jogador]} pontos")

# Encontrar menor pontuação
menor_jogador = min(jogadores, key=jogadores.get)
print(f"Menor pontuação: {menor_jogador} com {jogadores[menor_jogador]} pontos")

# Média de pontos
media = sum(jogadores.values()) / len(jogadores)
print(f"Média de pontos: {media:.2f}")

# Ranking
print(f"\nRanking:")
for i, (jogador, pontos) in enumerate(sorted(jogadores.items(), key=lambda x: x[1], reverse=True), 1):
    print(f"  {i}. {jogador}: {pontos}")


# ===== 16. EXERCÍCIO PRÁTICO 3 =====
print("\n16. EXERCÍCIO PRÁTICO 3: CONTAGEM DE PALAVRAS")
print("-" * 70)

texto = "python python java python java java javascript"
palavras = texto.split()

print(f"Texto: {texto}\n")

# Contar palavras usando dicionário
contagem = {}
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

print(f"Contagem de palavras:")
for palavra, count in sorted(contagem.items(), key=lambda x: x[1], reverse=True):
    print(f"  {palavra}: {count}")

# Palavra mais frequente
mais_frequente = max(contagem, key=contagem.get)
print(f"\nPalavra mais frequente: '{mais_frequente}' (aparece {contagem[mais_frequente]} vezes)")


# ===== 17. RESUMO DOS MÉTODOS =====
print("\n17. RESUMO DOS MÉTODOS")
print("-" * 70)

print("\nMétodos de ACESSO:\n")
acesso = {
    "keys()": "Retorna todas as chaves",
    "values()": "Retorna todos os valores",
    "items()": "Retorna pares (chave, valor)",
    "get(chave)": "Obtém valor com segurança",
}
for metodo, desc in acesso.items():
    print(f"  {metodo:20} → {desc}")

print("\nMétodos de MODIFICAÇÃO:\n")
modificacao = {
    "update()": "Adiciona/atualiza múltiplos itens",
    "pop()": "Remove e retorna valor",
    "popitem()": "Remove último item",
    "clear()": "Remove todos os itens",
    "setdefault()": "Define valor padrão",
}
for metodo, desc in modificacao.items():
    print(f"  {metodo:20} → {desc}")

print("\nMétodos de CÓPIA:\n")
copia_metodos = {
    "copy()": "Cria cópia rasa",
    "deepcopy()": "Cria cópia profunda (módulo copy)",
}
for metodo, desc in copia_metodos.items():
    print(f"  {metodo:20} → {desc}")

print("\nMétodos de CRIAÇÃO:\n")
criacao = {
    "fromkeys()": "Cria dict com mesmas chaves",
}
for metodo, desc in criacao.items():
    print(f"  {metodo:20} → {desc}")

print("\n" + "=" * 70)
