#!/usr/bin/env python
# coding: utf-8

# # lista em Python
# 
# # estrutura:
# 
# Lista = [valor, vlor, valor, valor...]
# 
# 1- Lista é um dos objetos mais importantes de Python, por isso vamos trabalhar bastante nelas.
# 2- Quando importamos uma base de dados par ao Python, normalmente ela é lida como uma "lista" ou como alguma "variação de lista".
# 3- Listas em Python foram feitas para serem homogêneas, apesar de aceitarem valores hertogêneos.
# 4- exemplos de listas:
#     
# Listas de produtos de uma Loja:

# In[30]:


produtos = ["tv", "celular", "mouse", "teclado", "tablet"]

#ou ela pode ser escrita de outra forma:
Produtos = ["tv",
            "celular",
            "mouse", 
            "teclado",
            "tablet"]

#exibir lista:
print (produtos)


# # Lista de Unidades vendidas de cada produto da Loja:
# 

# In[31]:


vendas = [1000, 1500, 350, 270, 900]

#printar informação da lista vendas index 1
print(vendas[1])


# # Juntando informações das duas listas (produtos e  vendas)

# In[32]:


produtos = ["tv", "celular", "mouse", "teclado", "tablet"]
# indice      0        1          2       3          4  
vendas = [  1000,    1500,      350,    270,      900]


# In[33]:


#OBS: .format( variavel[index], variavel [index]  )
print ("Vendas do produto {} foram de {} Unidades".format(produtos[1], vendas[1]))


# # Modificando uma lista:
# 
# Sintaxe para realizar alteração:
# 
# lista[index] = valor_novo

# In[34]:


# vamos alterar a quantidade de vendas do teclado [index_3] para 300

vendas[3] = 300

print ("Vendas do produto {} foram de {} Unidades".format(produtos[3], vendas[3]))


# # Como dscobrir indice de um item de uma lista?
# 
# Sintaxe:
# 
# i = lista.index("item")

# In[37]:





# Nesse caso a lista é pequena para fins didáticos, mas essa lista poderia ter dezenas de milhares de produtos diferentes.
# E agora como faço para descobrir a quantidade em estoque do produto geladeira?

# In[41]:


produtos = ["tv", "celular", "mouse", "teclado", "tablet"]
vendas = [  1000,    1500,      350,    270,      900]


i = produtos.index("teclado")
print (i)

#note que basta digitar o nome da lista e o campo que deseja procurar.


# # Adicionar ou remover itens de uma lista:
# 
# Adicionar:
# lista.append(item)
# 
# 
# 
# Remover:
# item_removido = lista.pop(indice)
# 
# Remover:
# lista.remove(item)
# 
# 
# 
# Trocar item:
# lista[index] = "item_novo
# 
# 
# Digamos que estamos construindo o controle de produtos da Apple. E a Apple lançõu o IPhone 11 e irá tirar dos seus estoques o iphhone X

# In[47]:


produtos = ["apple tv", "mac", "iphone x", "ipad", "apple watch", "mac book", "airpods"]

#adicionar iphone 11 
produtos.append("iphone 11")
print (produtos)




#remover iphone x
produtos.remove("iphone x")
print (produtos)


# Como podemos ver foi acrescentado o item "iphone 11" e foi removido o "ipohone x".
