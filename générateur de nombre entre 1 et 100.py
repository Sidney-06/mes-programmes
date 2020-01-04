from random import randint

print()
print("vous etes actuelment dans un générateur de nombre !!!")
print()
party = input("voulez vous générer un nombre entre 0 et 100 ? (écrire oui ou non) : ")
print()

if party == "oui":
    nb = randint(0,100)
    print("le nombre générer est : ", nb,"!!!")
    print()
    print("merci d'avoir utiliser ce générateur, on espere vous revoire bientot !!!")

else:
    print("tres bien vous ne souhaitez pas utiliser le gérateur alors on espere vous revoire tres bientot !!!")