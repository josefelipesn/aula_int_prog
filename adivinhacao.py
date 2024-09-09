#Mago adivinhador

tipo_animal = input("Seu animal é mamífero ou réptil?: ")

if tipo_animal.lower() == "mamífero":
    print("Eu acho que seu animal favorito é um cachorro")

elif tipo_animal.lower() == "réptil":
    print("Eu acho que seu animal favorito é uma tartaruga!")

else:
    print("Não consegui adivinhar seu animal favorito.")