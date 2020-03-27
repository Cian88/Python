nb=input("Entrez un chiffre/nombre :")
maxi=input("Entrez l'échelle de la table :")
i=0
	
try:
	nb=int(nb)
	maxi=int(maxi)
			
except ValueError:
	print("Entrez un chiffre/nombre :")

while i<maxi:
	print(nb,"*",i+1,"=", nb*(i+1))
	i+=1