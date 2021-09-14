import random
# Création des variables
reponse = None
interval = None
a = None
b = None
reboot = True
reponse_reboot = None
print("Devinez le chiffre entre a et b!")
a = int(input("définisser la valeur de a : \n"))
b = int(input("définisser la valeur de b : \n"))
# définiton du nombre random à deviner
nombre_a_deviner = random.randint(a, b)
# code principal du jeu dans une boucle
while reponse != nombre_a_deviner or reboot:
	reponse = int(input("Quelle est votre réponse ?\n"))
	if reponse > nombre_a_deviner:
		print("Ce n'est pas ça. Le nombre est plus petit")
	elif reponse < nombre_a_deviner:
		print("Ce n'est pas ça. Le nombre est plus grand")
	else:
		print("Bonne réponse ")
		# choix de recommencer ou non le jeu, et donc réinitialiser la boucle principale
		reponse_reboot = input("Souhaitez vous recommencer ? Y ou N\n")
		if reponse_reboot == "Y":
			reboot = True
			interval = input("Souhaitez vous modifier l'inverval ? Y ou N\n")
			if interval == "Y":
				a = int(input("définisser la valeur de a : \n"))
				b = int(input("définisser la valeur de b : \n"))
			nombre_a_deviner = random.randint(a, b)
		else:
			#sortie du jeu
			reboot = False
print("Merci d'avoir joué")
