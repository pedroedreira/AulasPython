while True:
    nomeProduto = input("Insira o nome do produto: ")
    qtd = input("Insiria a quantidade: ")
    qtd = int(qtd)
    continuar = input("Deseja inserir mais um cadastro? Caso SIM digite [S], para NÃO digite [N]")
    if continuar == "N":
        break