import json
import os.path
import os
# Salvar os dados do estoque
arquivo_estoque = 'estoque.json'

# Carregar os dados do estoque
def carregar_estoque():
    # Verificar se o arquivo existe
    if not os.path.exists(arquivo_estoque):
        return []

    try:
        with open(arquivo_estoque, 'r') as file:
            estoque = json.load(file)
            if not isinstance(estoque, list):
                raise ValueError('Formato inválido no arquivo de estoque')
            return estoque
    except (json.JSONDecodeError, ValueError):
        return []

# Função para salvar os dodos do estoque
def salvar_estoque(estoque):
    with open(arquivo_estoque, 'w') as file:
        json.dump(estoque, file, indent=4)

# Adicionar os produtos
def adicionar_produto(nome, quantidade, preco):
    estoque = carregar_estoque()
    estoque.append({'nome': nome, 'quantidade': quantidade, 'preco': preco})
    salvar_estoque(estoque)
