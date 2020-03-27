# Table de multiplication

import os

logiciel_on=True # sans info contraire on peut relancer une autre table

while logiciel_on:
	
	from package import multiplication
	
	quitter=input("Voulez-vous continuer ? (O/N) :")
	
	if quitter not in ("o","O"):
		logiciel_on=False

os.system=("pause")
input("Appuyez sur une touche pour quitter.")