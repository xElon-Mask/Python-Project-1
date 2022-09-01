""" Premier programme
Formation Python
Apprendre la programmation """


def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input("Quel est votre age ?")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR : vous devez rentrer un nombre pour l'age")
    return age_int

# demander le nom
nom = ""
while nom == "":
    nom = input("Quel est votre nom ?")

# demander l'age
age = demander_age()


""""try veut dire essayer en anglais, 
le terme est utilisé en programmation pour gérer des erreurs possibles.
Si l'instruction sous try n'a pas fonctionné, il faut donc une exception qui s'enclenche.
Pour éviter la suite des instructions après avoir pris l'exception, il faut passer les instructions post-exception dans un bloc else:

while veut dire "tant que" """

# afficher les résultats
print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
# ceci est un commentaire en Python
print("L'an prochain vous aurez " + str(age+1) + " ans")

