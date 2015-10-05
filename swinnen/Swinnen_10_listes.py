# -*- coding: utf-8 -*-

from random import *                #pour les nombres aléatoires

# principales commandes:
# count, append, extend, insert, remove, pop, del, sort, reverse, index

#LISTES
#une liste peut contenir des éléments de type différent, même une autre liste, un tuple...
uneListe = ['lundi', 'mardi', 'mercredi', 1800, -1.5, ["est", "ouest"], 'janvier' ]

nombreElements = len(uneListe)		            # nombre d'éléments dans la liste (=7). [est, ouest] compte pour 1 element !
frequence = uneListe.count('mardi')             # combien de fois 'mardi' se retrouve dans la liste

# lire
print "toute la liste ", uneListe
premierElement = uneListe[0]			        # lire premier element: lundi. La numérotation des index commence à 0
dernierElement =  uneListe[-1]		            # c'est le raccourci pour uneListe[len(uneListe)-1]
avantDernierElement = uneListe[-2]
subListeMilieu =  uneListe[2:4]		            # SLICES ("tranches"): lire elements 2 et 3 (4 pas compris)
                                                # Pour connaitre le nombre d'éléments: 4 - 2 = 2
                                                # le résultat d'un slice est une LISTE
                                                # pour plus info slices voir plus bas
# lire une liste imbriquée
print uneListe[5]                               # ["est", "ouest"]          l'élement lu est de type liste
print uneListe[5][0]                            # est                       type: string

# assigner des valeurs aux elements de la liste
uneListe[3] = "jeudi"							# remplace l'element a index 3 (1800) par "jeudi"
uneListe[5][1] = "NordEst"                      # pour une liste imbriquée

# AJOUTER A LA FIN
uneListe.append("fevrier")			# ajouter à la fin
# on peut aussi créer une liste vide et puis la remplir  #resultat equivaut à: autreListe = ["nord", "sud"]
autreListe = []
autreListe.append ("nord")
autreListe.append("sud")

# COMBINER DES LISTES: 2 possibilités
# 1) ajouter les éléments individuels de la 2ieme liste:
listeAllongee = uneListe + autreListe   # remarque: uneListe et autreListe restent intacts
uneListe.extend(autreListe)             # même résultat, mais uneListe est changée
# uneListe = uneListe + autreListe      # même résultat que précédent
# 2) ajouter une liste en tant que liste (crée un liste imbriquee)
uneListe.append(autreListe) 		# cette fois autreListe est ajouté en tant que LISTE (comme 1 seul element)
                                    # uneListe est change

# INSERER
uneListe.insert(4, "vendredi")      # insérer "vendredi" à l'index 4

# ENLEVER
nombres = [4, 10, 8, 17, 10, 10, 16, 9, 2, 12, 4, 18, 8]
# enlever une certaine VALEUR
nombres.remove(10)  # attention ceci enlève l'élément avec la VALEUR 10, pas l'élément avec index 10
                    # attention: enlève seulement la premier occurence de la valeur 10 !

dernierElement = nombres.pop() 	    # enlève le dernier élément.
                                    # la valeur retourné peut être printé ou assignée à une variable
# enlever par INDEX de l'élément
troisiemeElement =  nombres.pop(3)		# ici on enlève le 4ième élement (17) (puisque l'index commence à 0)

# alternatif: si on n'a plus besoin de cet élément on utilise del (pas d'attribution à une variable)
del nombres[0]                      # enlève l'élément avec index 0
del nombres[7:9]                    # enleve une tranche (index 7 à 9 ( 9 pas compris)

#***************************************************************************

# PARCOURIR une liste, il y a deux façons
# parcourir chaque valeur la liste
for mot in uneListe:                            # dans la boucle la variable "mot" prend la VALEUR de chaque ELEMENT suivant
    print mot
# parcourir sur index avec range
for i in range(0, len(uneListe)):                   # dans la boucle, la variable i prend la valeur de 0, 1, 2 etc
    print uneListe[i]                               # et on lit la liste en utilisant i comme index
                                                    #utile pour préciser quelle série d'elements on veut lire)

# *****************************************************************
#tableau 2D:
unTableau = [["0a", "0b", "0c"], ["1a", "1b", "1c"]]       # tableau avec 2 lignes, 3 colonnes
#parcourir un tableau: même principe que précédent, mais on utilise 2 boucles for
# avec for
for ligne in unTableau:
    for colonne in ligne:
        print colonne
# avec range
for i in range(0, len(unTableau)):                         # l'index i parcourt les lignes
   for j in range(0, len(unTableau[i])):                  # l'index j parcourt les colonnes de la ligne i
        print unTableau[i][j]
# **********************************************************************$
# TRIER / REVERSER
nombres = [17, 38, 10, "janvier", 25, 72]
nombres.sort()                      # trier la liste     [10, 17, 25, 38, 72, 'janvier']
nombres.reverse()                   # inverser l'ordre des éléments
print nombres                       # ['janvier', 72, 38, 25, 17, 10]

# RECHERCHE
mots = ['jambon', 'fromage', 'confiture', 'chocolat']
# rechercher la présence d'une valeur dans une liste (resultat est "true" ou "false")
if 'chocolat' in mots:
    print 'trouvé'

# rechercher l'implacement exact (index) d'une valeur
indexMot =  mots.index('chocolat')

# COPIER LISTE
# il y a des "vraies" et des "fausses" copies:
# 1)fausse copie (crée un alias)
aliasMots = mots                            # en fait on donne un autre nom (alias, référence) à la même liste
                                            # une seule liste dans la mémoire de l'ordinateur
                                            # si changement dans une des deux, l'autre reflétéra ce changement
# 2) vraie copie (deep copy) crée deux listes indépendentes. Pour cela, il faut copier chaque element
liste2 = []                                 # créer un nouvelle liste vide, à laquelle on ajoutera chaque element
for mot in mots:
    liste2.append(mot)
mots[0] = "autre valeur"                      # un changement en mots n'a pas d'influence sur liste2,
print mots
print liste2

# ****************************************************************************
#SLICES
# lire une "slice" de la liste, le resultat est à son tour une liste (même s'il ne contient qu'un seul élement)
# le résultat peut être printé ou attribué à une variable, la liste originale n'est pas altérée
subListeDebut = uneListe[0:2]		            # lit 2 éléments: 0 et 1  (2 n'est pas compris)!
subListeDebut1 = uneListe[:2]		            # même chose que précédent: 0 est supposé par défaut
listeTotale = uneListe[0:]		            # zero jusque fin (la fin est supposé par défaut (= print uneListe)
subListeMilieu =  uneListe[2:4]		            # Elements 2 à 3 / Nombre d'éléments: 4 - 2 = 2
listeAvecUnElement = uneListe[2:3]		    # comme uneListe[2], mais ici le résultat est de type liste, pas de type int ou string
listeToutSaufDernier =  uneListe[:-1]       # une liste avec tous les elements SAUF le dernier)
                                            #attention, ne pas confondre avec dernierElement (voir plus haut),
                                            # qui retourne une seule valeur !
# SLICING AVANCE
# Ajouter des éléments à l'intéreur de la liste
mots = ['jambon', 'fromage', 'confiture', 'chocolat']
mots[2:2] = ['miel']                                    # ajoute miel après fromage (à l'index 2)
mots[5:5] = ['saucisson', 'ketchup']                    # ajoute saucisson et ketchup après chocolat (à l'index 5)
# remplacer une tranche
mots[1:3] = ['salade']                                  # elements 1 à 3 (3 non compris) sont remplacés pas 'salade'
mots[0:2] = []                                          # elements 0 à 2 (2 non compris) sont enlevés (remplaces par liste vide)
 # attention: un élément seul, comme 'salade' doit aussi être présentés comme liste, donc entre [] !
print mots

#********************************************************************************

# CREATION DE QQS LISTES SPECIALES
# créer une liste par répétition
sept_zeros = [0]*7                  # crée une liste de sept zeros
autantDeZeros = [0]*len(autreListe)             # une liste de zeros de la même longueur que autreListe

# Range crée une liste avec une séquence ordonnée de nombres
listeNombres = range(10)                                  # un liste de 10 nombres, allant de 0 à 9!
listeNombres = range(5, 13)                               # 5 à 12!   (nombre d'éléments: 13 - 5 = 8
listeNombres = range(3, 16, 3)                            # dernier argument: step       3, 6, 9, 12, 15

# liste de nombres aléatoires
nombresAleatoiresListe = []
for i in range(10):                   # créer une liste de dix elements
    #r = random()                     # un chiffre entre 0 et 1
    #r = randrange(6)                 # un chiffre entre 0 et 5  (6 possibilités)
    r = randrange(6) + 1             # idem, mais décalé de 1: un chiffre entre 1 et 6  (6 possibilités)
    nombresAleatoiresListe.append(r)
print nombresAleatoiresListe

# ***********************************************************$
# TUPLE
# peut être lu cfr liste, mais pas modifié
unTuple = ("un", "deux", "trois")           # parentheses pas obligatoire
autreTuple = ("chose",)                       # si 1 element, la virgule de la fin provoque la tranformation en tuple
