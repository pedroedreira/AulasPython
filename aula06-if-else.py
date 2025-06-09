nomeCandidato = input("Insira seu nome:")
idadeCandidato = input("Insira sua idade:")
idadeCandidato = int(idadeCandidato)
renda = input("Insira sua renda mensal:")
renda = float(renda)

if renda >= 2000 and idadeCandidato >= 18:
    print("Ótimo! Você tem crédito aprovado para uso.")
else:
    print("Poxa! Infelizmente você não tem crédito aprovado")
