# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

produto = "FIAT TORO"
preco = 20000
desconto = 17

valor_final = preco - (preco * desconto / 100)

print("produto:", produto)
print("preço:", preco)
print("porcentagem de desconto:", desconto)
print("O produto com,str(desconto)+R$ , valor_final")
