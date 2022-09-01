""" Premier programme
Formation Python
Apprendre la programmation """

# redemander le nom tant que l'user n'a pas répondu à la question, testez juste si le nom est vide ou non
nom = ""
while nom == "":
    nom = input("Quel est votre nom ?")

age = 0

""""try veut dire essayer en anglais, 
le terme est utilisé en programmation pour gérer des erreurs possibles.
Si l'instruction sous try n'a pas fonctionné, il faut donc une exception qui s'enclenche.
Pour éviter la suite des instructions après avoir pris l'exception, il faut passer les instructions post-exception dans un bloc else:

while veut dire "tant que" """
while age == 0:
    age_str = input("Quel est votre age ?")
    try:
        age = int(age_str)
    except:
        print("ERREUR : vous devez rentrer un nombre pour l'age")

print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
# ceci est un commentaire en Python
print("L'an prochain vous aurez " + str(age+1) + " ans")

