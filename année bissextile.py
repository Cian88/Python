# -*-coding:Latin-1-*

import os

continuer_test=True

while continuer_test:

	annee=input("Entrez une ann�e :")
	annee=int(annee)

	if annee%400==0 or (annee%4==0 and not annee%100==0):
		print("L'ann�e est bissextile.")
	else:
		print("L'ann�e n'est pas bissextile.")

os.system("pause")




