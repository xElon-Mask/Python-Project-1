""" Premier programme
Formation Python
Apprendre la programmation """

nom = input("Quel est votre nom ?")
age = input("Quel âge avez-vous ?")

""""try veut dire essayer en anglais, 
le terme est utilisé en programmation pour gérer des erreurs possibles.
Si l'instruction sous try n'a pas fonctionné, il faut donc une exception qui s'enclenche.
Pour éviter la suite des instructions après avoir pris l'exception, il faut passer les instructions post-exception dans un bloc else:"""
try:
    age_prochain = int(age) + 1
except:
    print("ERREUR : vous devez rentrer un nombre pour l'age")
else:
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
# ceci est un commentaire en Python
    print("L'an prochain vous aurez " + str(age_prochain) + " ans")

