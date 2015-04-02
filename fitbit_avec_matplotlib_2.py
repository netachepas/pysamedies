# -*- coding: utf-8 -*-
# import numpy as numpy					#apparement inutile avec les fonctions utilisées
#import pylab as pl
from pylab import plot, xlabel, show	# nécessite 'matplotlib' (contenant pylab)


#ouvrir le csv et l'attribuer à un variable (= creer un objet fichier) 
fObj = open("jawbone.csv")			

fibListe = fObj.readlines()					

nombreRecords = len(fibListe)

fObj.close()					#on n'a plus besoin de cet objet fichier



for i in range(1, nombreRecords-1):
	#   WAS 'range(0, nombreRecords-1)' ==> Maintenant on défini la plage allant de
	#   la deuxième ligne à la dernière (donc sans celle des titres, la 0!).

	#à droite: lire le contenu d'element i (=un string) et le transformer en liste en splittant le string sur le delimitateur ;
	#et remplacer le contenu original (le string est donc remplace par une liste)
	fibListe[i] = fibListe[i].split(";") 


def creerListeColonne(numCol):
	colXListe = []
	for i in range(1, nombreRecords-1):		#   WAS 'range(0, nombreRecords-1, voir plus haut)'			
		colXListe.append(int(fibListe[i][numCol]))
	return colXListe



colonneTreizeListe = creerListeColonne(13)
#colonneZeroListe = creerListeColonne(0)
print (len(colonneTreizeListe))



#pour l'axe x, on cree une liste avec les chiffres de 0 à nombreRecords, censees representer des jours consecutives 
#TO DO: remplacer ces chiffres arbitraires avec les valeurs reelles des temps ou ces valeurs on ete mesurees
x = []											#WAS x =  [1, 2, 3, 4, 5, 6, 7, 8]	#représentent mois 1 à 8
for i in range(1, nombreRecords-1):				#WAS rang(0,...)
	x.append(int(i))


plot(x, colonneTreizeListe)				# WAS pl.plot, quand on faisait import pylab as pl
xlabel("Jours de mesure")				# WAS xlabel(colonneTreizeListe) 		#titre du graphe (ici les données de la colonne 13)
show()									# WAS pl.show
