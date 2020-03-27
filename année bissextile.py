# -*-coding:Latin-1-*

import os

continuer_test=True

while continuer_test:

	annee=input("Entrez une année :")
	annee=int(annee)

	if annee%400==0 or (annee%4==0 and not annee%100==0):
		print("L'année est bissextile.")
	else:
		print("L'année n'est pas bissextile.")

os.system("pause")




