#Verificar se há ferro suficiente na liga da armadura.

ferro = float(input("digite a quantidade de ferro: "))
ouro = float(input("Digite a quantidade de ouro:"))

total = ferro + ouro
porcentagemferro = (ferro / total) *100

if porcentagemferro >= 70:
    print("quantidade de ferro é suficiente")

else:
    print("quantidade de ferro não é suficiente")
