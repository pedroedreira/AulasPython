produto = "Computador"
preco = 203.98
qtd = input("Digite a quantidade de produtos desejada:")
qtd = int(qtd)
resultado = qtd*preco
nomeCliente = input("Digite seu nome completo:")
doctoCliente = input("Insira seu ID:")

print("------RELATÓRIO------")
print("---INFORMAÇÕES DO COMPRADOR---")
print("NOME DE USUÁRIO:",nomeCliente)
print("ID DO USUÁRIO:",doctoCliente)
print("---INFORMAÇÕES DA COMPRA---")
print("PRODUTO ADQUIRIDO:",produto)
print("PREÇO UNITÁRIO: R$",preco)
print("QUANTIDADE ADQUIRIDA:",qtd)
print(f"TOTAL PARA PAGAMENTO: R${resultado:.2f}")