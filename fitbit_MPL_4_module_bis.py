# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


def creerFibTableau(csvFile):
    global nombreRecords, fibListe  # declarer comme "global" tous les variables qui doivent être partagés à travers le programme
    # sinon ils seront seulement "connus" à l'intérieur de cette fonction
    fObj = open(csvFile)
    fibListe = fObj.readlines()  # cree une liste ou chaque element = une ligne de texte (= 1 record string)
    nombreRecords = len(fibListe)
    fObj.close()

    for i in range(0, nombreRecords):  # WAS 1: on doit aussi splitter la ligne avec les headers, donc la 0
        # pour lire les données on commencera à 1 (voir plus bas)
        fibListe[i] = fibListe[i].split(";")
    return fibListe


def lireNombreRecords(fibListe):
    return len(fibListe)


# creer la liste des jours pour l'axe X
def creerX():
    # pour l'axe x, on cree une liste avec les chiffres de 0 à nombreRecords, censees representer des jours consecutives
    #TO DO: remplacer ces chiffres arbitraires avec les valeurs reelles des temps ou ces valeurs on ete mesurees
    global nombreRecords
    xListe = []  # x =  [1, 2, 3, 4, 5, 6, 7, 8]	#représentent p.e. les jours 1 à 8
    for i in range(1, nombreRecords):  #WAS rang(0,...)
        xListe.append(int(i))
    return xListe


# le code precedent peut etre remplace par une fonction de numpy
# xListe = np.arange(1,nombreRecords) 			#troisième argument optionel: step

# creër la liste avec les valeurs d'une colonne pour l'axe Y
def creerY(numCol):  # WAS creerListeColonne
    global nombreRecords, fibListe
    colListe = []  # WAS: colXListe      # initialiser une liste vide
    derniereVraieValeur = 0  # initialiser avec une valeur quelquonque

    for i in range(1,
                   nombreRecords):  # WAS: 2 boucles, maintenant 1 / plus utiliser moyenne, mais valeur précédente si valable
        if fibListe[i][numCol] != '' and fibListe[i][
            numCol] != '0':  # si le champ n'est pas vide et ne contient pas de 0,
            derniereVraieValeur = fibListe[i][numCol]  # c'est un valeur valide, on la mémorise
        else:  # si pas valide (le champ est vide ou contient 0)
            fibListe[i][numCol] = derniereVraieValeur  # on le remplace par la derniere valeur memorisé
        colListe.append(fibListe[i][
            numCol])  # on passe un string, mais pas de problème: il est automatiquement converti en int ou float
    return colListe


# PROGRAMME PRINCIPAL
if __name__ == '__main__':
    # la façon officielle pour délimiter le programme principal
    # permet aussi bien l'utilisation comme programme indépendant
    # que import de ce fichier comme module dans un autre .py
    creerFibTableau("jawbone.csv")
    xListe = creerX()
    # demander les colonnes à afficher à l'utilisateur
    # et convertir la sequence des valeurs entrees en list
    # quellesColonnes = list(input("Entrez plusieurs colonnes, separes par des virgules "))
    quellesColonnes = [13, 37]  # print fibListe[0][13]           # m_distance
    #print fibListe[0][37]           # s_duration

    nombreColonnesAMontrer = len(quellesColonnes)
    for i in range(0, nombreColonnesAMontrer):
        yListe = creerY(quellesColonnes[i])
        plt.plot(xListe, yListe, '-*')  # faire un plot pour chaque yListe
        # le troisième argument précise le style de la courbe
        # WAS: b"*" pour étoiles bleus (si on enlève le b, les courbes sont de couleur différente
        #      "-*" si on veut combiner ligne et étoiles (encore une autre alternative)

    # inscriptions du plot
    plt.xlabel("Jours de mesure")  #titre du graphe (ici les données de la colonne 13)
    plt.ylabel("Resultats")
    plt.title = "Lecture fitbit"  # WAS plt.title("Lecture colonne %i " % nCol)

    # affichage du plot
    plt.show()