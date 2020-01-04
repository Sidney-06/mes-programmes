from random import randint

user = 0
compute = 0
party = "oui"

print()
print(" Pierre, Papier, Scisos !!!")
print()
print(" Dans ce jeux vous allez jouer contre l'ordinateur !!!")
print()
print(" INFORMATION :")
print(" La Pierre casse Les Scisos !!!")
print(" La Feuille recouvre La Pierre !!!")
print(" Les Scisos coupe La Feuille !!!")
print()
print(" La party se déroule en trois manche !!!")
print()
print(" Très bien maintenant jouons !!!")
print()
print("___________________________________________________________________________________________")
print()

while party == "oui":
    
    for i in range (3):
        print()
        print("  choisissez quelle objet vous allez utiliser avec les comandes ci desous :")
        print()

        player = input("             pierre = (pi), papier = (p), scisos = (s) : ")
        print()
        print()

        if player == "(pi)":
            print("                                  0", end =" ")

        if player == "(p)":
            print("                                  ___", end =" ")

        if player == "(s)":
            print("                                  >8", end =" ")

        print("vs", end =" ")

        chosen = randint(1,3)

        if chosen == 1:
            computer = "(pi)"
            print("0")

        if chosen == 2:
            computer = "(p)"
            print("___")

        if chosen == 3:
            computer = "(s)"
            print(">8")

        print()
        print()

        if player == computer:
            print("   EGALITER !")

        elif player == "(pi)" and computer == "(s)":
            print("   LE JOUEUR A GAGNER LA MANCHE !")          
            user = user + 1

        elif player == "(pi)" and computer == "(p)":
            print("   L'ORDINATEUR A GAGNER LA MANCHE !")
            compute = compute + 1

        elif player == "(p)" and computer == "(pi)":
            print("   LE JOUEUR A GAGNER LA MANCHE !")
            user = user + 1

        elif player == "(p)" and computer == "(s)":
            print("   L'ORDINATEUR A GAGNER LA MANCHE !")
            compute = compute + 1

        elif player == "(s)" and computer == "(p)":
            print("   LE JOUEUR A GAGNER LA MANCHE !")
            user = user + 1

        elif player == "(s)" and computer == "(pi)":
            print("   L'ORDINATEUR A GAGNER LA MANCHE !")
            compute = compute + 1

        else:
            print("   ERREURE !!!")

        print()
        print()
        print("   Point :")
        print()
        print("   Joueur = ", user, end ="   ") 
        print()
        print("   Ordinateur = ", compute, end ="   ")  
        print() 
        print()
        print("___________________________________________________________________________________________")   
        print()  

    print()
    print("Les 3 Manches Sont Terminées,")
    print()

    if user > compute:
        print("LE JOUEUR REMPORTE LA PARTIE AVEC UN SCORE DE :", user, "A", compute, "!!!")

    elif user < compute:
        print("L'ORDINATEUR REMPORTE LA PARTIE AVEC UN SCORE DE :", compute, "A", user, "!!!")

    elif user == compute:
        print("MATCHE NUL, LE JOUEUR ET L'ORDINATEUR SONT A EGALITER AVEC UN SCORE DE :", user, "A", compute, "!!!")

    print()
    print("___________________________________________________________________________________________")
    print()

    print()
    party = input("Voulez vous rejouer une Party ??? (répondez par oui ou non) : ")
    print()
    print()

    if party == "oui":
        print("Très bien vous souhaitez rejouer alors c'est partie !!!")
        print()
        print("___________________________________________________________________________________________")
        user = 0
        compute = 0

    else:
        print("Comme c'est domage vous ne souhaitez pas rejouer ! Tempi on espère vous revoire très bientôt alors !!!")
        print()
    
    print()