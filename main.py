""" Premier programme
Formation Python
Apprendre la programmation """

#afficher_informations_personne
# Paramètres : nom, age

def afficher_informations_personne(nom, age):
    print()
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age+1) + " ans")

# rajouter condition si age > 60 : Vous êtes sénior
# age < 10 : Vous êtes enfant
    if age == 17:
        print("Vous êtes presque majeur")
    elif age == 18:
        print("Tout juste majeur: Félicitiations !")
    elif age > 60:
        print("Vous êtes sénior")   
    elif age >= 18:
        print("Vous êtes majeur")
    elif age < 10:
        print("Vous êtes enfant")
    else:
        print("Vous êtes mineur")




def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ?")
    return reponse_nom

def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre age ?")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR : vous devez rentrer un nombre pour l'age")
    return age_int

# demander le nom
nom1 = demander_nom()
nom2 = demander_nom()


# demander l'age
age1 = demander_age(nom1)
age2 = demander_age(nom2)


""""try veut dire essayer en anglais, 
le terme est utilisé en programmation pour gérer des erreurs possibles.
Si l'instruction sous try n'a pas fonctionné, il faut donc une exception qui s'enclenche.
Pour éviter la suite des instructions après avoir pris l'exception, il faut passer les instructions post-exception dans un bloc else:

while veut dire "tant que" """

# afficher les résultats
"""
print("Vous vous appelez " + nom1 + ", vous avez " + str(age1) + " ans")
# ceci est un commentaire en Python
print("L'an prochain vous aurez " + str(age1+1) + " ans")

print("Vous vous appelez " + nom2 + ", vous avez " + str(age2) + " ans")
print("L'an prochain vous aurez " + str(age2+1) + " ans")"""

afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)
