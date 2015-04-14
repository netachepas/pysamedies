# -*- coding: utf-8 -*-
#import numpy as np					# pas necessaire pour le moment
# import pylab as pl 					# remplacé par la ligne suivante
#from pylab import plot, xlabel, show	# nécessite 'matplotlib' (contenant pylab)
import matplotlib.pyplot as plt


# fonction qui extrait les valeurs d'une colonne dans une liste et retourne cette liste 
def creerListeColonne(numCol):
	colXListe = []
	# on parcourt d'abord la colonne une première fois, pour remplir tous les champs vides par une valeur 0 
	for i in range(1, nombreRecords):		#   WAS 'range(0, nombreRecords-1)'  	
		if fibListe[i][numCol] == '':		#les valeurs sont de type string
			fibListe[i][numCol] = 0
		
		
	for i in range(1, nombreRecords):
		valeurCol = int(fibListe[i][numCol])	#les valeurs sont de type string, donc d'abord convertir en int 
		
		#pour les champs à valeur 0, on remplace le 0 par la moyenne de la precedente et suivante
		if valeurCol == 0:
			if (i > 1) and (i < nombreRecords-1):		#faire la moyenne est seulement possible si le champ a un champ precedent et suivant
														#donc pas possible pour i = 1 en i = nombreRecords-1, une valeur 0 restera 0
				precedent = int(fibListe[i-1][numCol])	#lire le champ dans la ligne precedente	
				suivant = int(fibListe[i+1][numCol])	#idem ligne suivante
				valeurCol= int(precedent+suivant)/2		#remplacer la valeur 0 par la moyenne
			
		colXListe.append(valeurCol)						#ajouter la valeur à la liste
	#print colXListe
	return colXListe									#retourner à la commande qui appelle la fonction


#PROGRAMME PRINCIPAL COMMENCE ICI
#ouvrir le csv et l'attribuer à un variable (= creer un objet fichier) 
fObj = open("jawbone.csv")			
fibListe = fObj.readlines()		#cree une liste ou chaque element = une ligne de texte (= 1 record string)				
nombreRecords = len(fibListe)
fObj.close()					


for i in range(1, nombreRecords):
	#   WAS 'range(0, nombreRecords-1)' ==> Maintenant on défini la plage allant de
	#   la deuxième ligne à la dernière (donc sans celle des titres, la 0!).

	#à droite: lire le contenu d'element i (=un string) et le transformer en liste en splittant le string sur le delimitateur ;
	#et remplacer le contenu original (le string est donc remplace par une liste)
	fibListe[i] = fibListe[i].split(";") 


#pour l'axe x, on cree une liste avec les chiffres de 0 à nombreRecords, censees representer des jours consecutives 
#TO DO: remplacer ces chiffres arbitraires avec les valeurs reelles des temps ou ces valeurs on ete mesurees

xListe = []											#WAS x =  [1, 2, 3, 4, 5, 6, 7, 8]	#représentent p.e. les jours 1 à 8
for i in range(1, nombreRecords):				#WAS rang(0,...)
	xListe.append(int(i))

# le code precedent peut etre remplace par une fonction de numpy
# xListe = np.arange(1,nombreRecords) 			#troisième argument optionel: step

# demander les colonnes à afficher à l'utilisateur
# convertir la sequence des valeurs entrees en list
quellesColonnes = list(input("Entrez plusieurs colonnes, separes par des virgules "))

# ou pour tester rapidement:
#quellesColonnes = [9,10, 13,14,15]

nombreColonnesAMontrer = len(quellesColonnes)
for i in range (0, nombreColonnesAMontrer):
	yListe = creerListeColonne(quellesColonnes[i])
	plt.plot(xListe, yListe)				# WAS pl.plot, quand on faisait import pylab as pl	
	
	
plt.xlabel("Jours de mesure")				#titre du graphe (ici les données de la colonne 13)
plt.ylabel("Resultats")
plt.title = ("Lecture de %i colonnes de fitbit" % nombreColonnesAMontrer)
plt.show()									
