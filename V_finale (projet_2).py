from random import choice
from time import sleep

score = 0
l = 0

with open('Question','r') as q:
    tab1 = list(range(30))
    for i in range(20):
        a = choice(tab1)
        tab1.remove(a)
    for ligne in q:
        l = l + 1
        for t in tab1:
            if l == t:
                ligne = list(ligne.split(";;"))
                print(ligne[0],"\n")
                n = input("Votre réponse ? \n Réponse : ")
                rep = ligne[1]
                rep_finale = rep.replace("\n","")
                if n == rep_finale:
                    score = score + 1
                    print("Bonne réponse ! +1 \n")
                else:
                    print(f"Mauvaise réponse... \nC'était laréponse {rep_finale} \n")
                sleep(0.5)
    print(f"Bravo ! Vous avez un score de {score} / 10")
    if score > high_score:
        high_score = score
    print(f"Le records est à {high_score}")