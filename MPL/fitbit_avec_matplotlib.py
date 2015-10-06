# -*- coding: utf-8 -*-
#représenter des données enregistrées par fitbit dans un graphique 

#pour cet exemple il faut avoir installe les modules matplotlib et numpy (pylab est inclus dans matplotlib(?))
import numpy as numpy
import pylab as pl

#IMPORTANT: preparation du fichier csv:
#Ouvrir les donnees fitbit en feuille calcul LibreOffice
#Save as... choisir .csv comme extension et cocher "Edit filter" !
#dans le dialogue window qui s'ouvre: 
#si votre tableau contient des virgules dans les champs, changer le delimiteur en ;
#sinon les colonnes seront mal delimitees
#laisser le reste en défaut
#deplacer le csv dans le meme repertoire que ce .py

#IMPORTANT: il faut enlever la première ligne ( les titres de colonnes) 
#et ne garder que les données chiffres pour que ce code marche !

#ouvrir le csv et l'attribuer à un variable (= creer un objet fichier) 
fObj = open("jawbone2.csv")			

#on peut maintenant utiliser les methodes de cet objet fichier pour en lire le contenu
#readlines() importe le contenu en tant que liste, 		

fibListe = fObj.readlines()	
#chaque element de cette liste correspond a 1 ligne de texte (=1 record)
#fibListe se presente donc comme une LISTE DE STRINGS   		
#print ("Le premier record fibListe[0] est un string ", fibListe[0])		#  2;5;10;... 
																			#les colonnes dans ce string sont separes par des ;

#REMARQUES
#ne pas confondre readlines() avec readline(), qui ne lit chaque fois que 1 seule ligne
#read() lit le contenu complet, mais sous forme de texte
				

nombreRecords = len(fibListe)

fObj.close()					#on n'a plus besoin de cet objet fichier (épargner pour libérer la mémoire)


#transformer fibListe (une liste de strings) en un tableau 2D  
for i in range(0, nombreRecords-1):
	#fibListe[i] se présente sous la forme d'un string séparé par des ; 		"2;5;10;..."	
	#à droite: lire le contenu de fiblListe[i] (=un string) et le transformer en liste en splittant le string sur le delimitateur ;
	#puis attribuer ce resultat à fibListe[i]. On remplace donc le string original par une liste

	fibListe[i] = fibListe[i].split(";") 

#a partir de maintenant on peut lire chaque valeur dans ce tableau ainsi:
#print (fibListe[1][2])				#la valeur de record 1, colonne 2


#créer 1 courbe dans le graphique
#axe x = temps, axe y = valeurs 
#les valeurs pour l'axe y se trouvent p.e. dans la colonne 13 du tableau
# on peut creéer un liste avec les valeurs de 1 colonne de notre tableau 2D ainsi:

colonneTreizeListe = []									#definir une liste vide
for i in range(0, nombreRecords-1):						#parcourir tous les records 		
	colonneTreizeListe.append(int(fibListe[i][13]))		#lire la valeur de la colonne 13 et l'ajouter a la liste
													#en même temps changer le contenu de ce champ (type string) en int 
#print ("Colonne Treize liste ", colonneTreizeListe)

#les valeurs de l'axe x représentent le moment où chaque mesure y a été prise
#ici on va arbitrairement numéroter ces temps de 1 jusq'au nombre total de records) 
#x =  [1, 2, 3, 4, 5, 6, 7, 8...]	#les valeurs pourraient représenter p.e les jours ou les mois
#pour bien faire il faudrait extraire les dates exactes de la colonne 0 du tableau fitbit 

x = []										#pour remplir une liste avec les valeurs de 1 à nombreRecords
i= 1
for i in range(0, nombreRecords-1):
	x.append(int(i))
	x[i] = i
#print (x)

#à partir d'ici pylab fait tout le travail
pl.plot(x, colonneTreizeListe)
pl.show()
