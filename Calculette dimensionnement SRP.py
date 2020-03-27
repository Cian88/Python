# Logiciel dimensionnement SRP by Valentin BOURA--DEFRANOUX

import os
from math import ceil

"""Restart logiciel"""

continuer = True
while continuer:

	"""Variables"""
	print("")
	print("")
	surface_plafond = input("Entrez la surface de votre plafond (m²) :")
	poids_structure = input("Entrez le poids de votre structure (kg/m²) :")
	espacement_poutre = input("Entrez l'espacement entre vos poutres (m) :")
	numero_filin = 0

	"""Validation variables comme nombres flottants"""

	surface_plafond = float(surface_plafond)
	poids_structure = float(poids_structure)
	espacement_poutre = float(espacement_poutre)

	"""Détermination du poids par SRP, numero du filin et nombre de srp"""

	nombre_fixation = surface_plafond / (1.2*espacement_poutre)
	nombre_fixation = ceil (nombre_fixation)
	poids_structure_total = poids_structure*surface_plafond
	poids_structure_total = round(poids_structure_total,1)
	poids_par_srp = poids_structure*1.2*espacement_poutre
	
	if poids_par_srp <= 45:
		numero_filin=2
	elif poids_par_srp<=90:
		numero_filin=3
	else:
		numero_filin=25

	"""Affichage résultat"""
	print ("")
	print ("")
	print ("Résultat :")
	print ("")
	if numero_filin == 25:
		print ("Veuillez nous consulter, votre projet est très spécifique et nécessite une étude approfondie")
		print("")
		print("")
	else:
		print ("Pour reprendre votre plafond ainsi que son ossature avec :\n\n#   un espacement entre poutres de", espacement_poutre,"m\n#   un poids total de la structure de", poids_structure,"kg/m²\n\nIl vous faudra", nombre_fixation, "SRP en n°",numero_filin,"(poids par SRP =", poids_par_srp,"kg.)")
		print("")
		print("")
	choix = input("Voulez-vous recommencer ? o/n :")
	if choix not in ("o","oui","O","ok","Ok","OK","OUI","0"):
		continuer=False
os.system("pause")
