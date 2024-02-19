# Criando um dicionário
pessoa = {"nome": "Davi", "idade": "16", "cidade": "Nilopolis RJ",}

# Exibindo o dicionário
print("Meu dicionario de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Criando uma chave e valor, depois de instanciado(criado) 
pessoa["sobrenome"] = "Alves"
print("Sobrenome:", pessoa["sobrenome"])
print("Meu dicionario de exemplo:", pessoa)

# Atualizando o dicionário
pessoa["idade"] = "17"
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor 
del pessoa["sobrenome"]

print("Meu dicionario de exemplo:", pessoa)

# Métodos: Keys(), values(), items()

# Métodos Keys
# chaves = pessoa.keys()
chaves = list (pessoa.keys()) 
print("Chaves do dicionario:", chaves)
print("Primeira chave:", chaves[0])

# Métodos values
# valores = pessoa.values()
valores = list (pessoa.values())
print("Valores do dicionario:", valores)
print("Primeiro valor do dicionario:", valores[0])

# Métodos items
# itens = pessoa.items()
itens = list (pessoa.items())
print("Pares chave-valor do dicionario:", itens)
print("Primeiro valor:", itens[0][1])
print("Primeiro valor:", itens[1][1])
print("Primeiro valor:", itens[2][1])
print("Primeiro chave-valor:%s = %s" % (itens[0][0], itens[0][1]))
print("Primeiro chave-valor:%s = %s" % (itens[1][0], itens[1][1]))
print("Primeiro chave-valor:%s = %s" % (itens[2][0], itens[2][1]))