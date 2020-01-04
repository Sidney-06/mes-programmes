from random import randint

party = "oui"

print()
print("vous etes actuelment dans un générateur de nombre !!!")
print()

while party == "oui":

    print("choisisser 2 nombre :")
    print()

    nb1 = input("choisisser le premier nombre : ")
    print()
    nb2 = input("choisisser le deuxieme nombre : ")
    print()

    nb = randint(nb1,nb2)

    print()
    print("le nombre générer entre : ", nb1," et : ", nb2," est : ", nb," !!!")
    print()
    print()

    party = input("voulez vous regénérer un nombre ? (répondez par oui ou non) : ")

else:
    print("très bien vous ne souhaitez pas utiliser le générateur alors a bientot !!!")
