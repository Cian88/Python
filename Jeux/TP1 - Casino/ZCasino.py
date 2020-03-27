# Jeu ZCasino
#-*-coding_Latin-1*

"""Variables & Modules"""

import os

nombre_mise=input("Choisissez un nombre entre 0 et 50 :")
mise=input("Choisissez votre mise entre 1 et 10 000 000$ :")
roulette=randrange(50)

roulette=int(roulette)
nombre_mise=int(nombre_mise)
mise=int(mise)

from random import randrange
from math import ceil

"""Programme roulette"""

if randrange(50)==nombre_mise:
        print("Vous avez gagne :",ceil(mise*3),"$ en trouvant le bon numero.")
elif ((randrange(50)%2==0)and(nombre_mise%2==0)) or ((randrange(50)%2!=0) and (nombre_mise%2!=0)):
        print("Vous avez gagne :",ceil (mise*1.5,"$ en tombant sur la bonne couleur.")
else:
        print("Vous avez perdu :", mise)

os.system("pause")
