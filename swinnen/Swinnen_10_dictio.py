# -*- coding: utf-8 -*-
# DICTIONNAIRE

# CREER
# au lieu d'un index, on utilise une clé, qui doit être unique
# on peut simplement ajouter des elements ainsi (il ne faut donc pas une fonction append(), comme pour les listes !
dico = {}
dico['computer'] = 'ordinateur'
dico['mouse'] = 'souris'
dico['keyboard'] = 'clavier'
print dico                           # {'computer' : 'ordinateur', 'mouse' : 'souris', 'keyboard' : 'clavier'}
                                    # n'apparaissent pas nécessairement dans l'ordre !

# ou bien créer avec une série des paires clé : valeur,
dico = {'computer' : 'ordinateur', 'mouse' : 'souris', 'keyboard' : 'clavier'}
inventaire = {'pommes': 430, 'bananes': 312, 'oranges': 274}
clients = {4317: 'Dupond', 256: 'Durand', 782 : "Schmidt"}

# un dictionnaire consiste donc de paires clé:valeur,
# où les clés et valeurs peuvent être de n'importe quel type

# LIRE
# au lieu d'un index, on utilise la clé, ici 'pommes'
nombreDePommes = inventaire['pommes']              # retourne 430

# ENLEVER
del dico['mouse']

print len(dico)

# méthodes des dictionaires
listeDeKeys =  inventaire.keys()            # renvoie une LISTE de toutes les CLES ['pommes', 'bananes', 'oranges']
listeDeValeurs = inventaire.values()        # renvoie une LISTE de toutes les VALEURS [430, 312, 274]
if inventaire.has_key('oranges') :          # rechercher la présence d'une clé
    print 'il y a des oranges'

if 'pommes' in inventaire:                  # alternative pour rechercher la présence d'une clé
    print 'il y a aussi des pommes'

listeDeTuples =  dico.items()       # retourne le contenu du dictionnaire en forme d'une liste de tuples (clé, valeur)
                                    # [('computer', 'ordinateur'), ('mouse', 'souris'), ('keyboard', 'clavier)]
                                    # ceci permet un triage alphabetique (voir plus bas)

# Faire une copie (alais ou vraie copy)
# alias (shallow copy) (en fait on crée seulement un autre nom, une autre référence vers le même objet en mémoire
# un changement dans un se reflète dans l'autre
dicoAlias = dico

# vraie copie (deep copy) (crée un nouvel objet indépendant)
dicoNouveau = dico.copy()

# PARCOURIR
# cec n'est pas optimal, à oublier:
for clef in inventaire:
    print clef, inventaire[clef]            #imprime la clé et sa valeur

# mieux: avec methode items(), qui renvoie une liste de tuples (clé, valeur)
for clef, valeur in inventaire.items():         # ou    .iteritems()
    print clef, valeur

# les clés ne doivent pas toujours être des chaines de caractères
# exemple avec des tuples, pour indiquer les coordonnées d'emplacement d'arbres sur un teerain (voir dessin p. 154
arbres = {}
arbres[(1,2)] = 'Peuplier'                  # remarque: les ( ) ne sont pas obligatoires
arbres[(3,4)] = 'Platane'
arbres[(6,5)] = 'Palmier'

print arbres[(6,5)]                 # palmier

# Pour éviter des erreurs de clés non-existantes: methode get()
# print inventaire['prunes']            # ERREUR, la clé n'existe pas, solution:
print inventaire.get('prunes', 0)   # get crée la clé prunes si elle n'existe pas et lui attribue la valeur 0 (valeur défaut)
                                    # il retourne la valeur 0, qui est imprimé

# autre exemple
#print arbres[(8,3)]                 # ERREUR: la clé n'existe pas, solution:
print arbres.get((8,3), 'clé existe pas')     # crée la clé (8,3) et lui attribue "clé existe pas' comme valeur défaut
                                            # cette valeur est imprimé

# les dictionnaires ne sont pas des séquences ordonnées,
# donc utiles pour des numérotations ou les chiffres ne se suivent pas (contrairement à un index)
client = {}
client[4317] = "Dupond"
client[256]= "Durand"
client[782] = "Schmidt"

# QUELQUES APPLICATION PRATIQUES
# HISTOGRAMMES (ou fréquences) (p.e. calculer le nombre de fois que chaque lettre est présente dans un texte)
texte = 'Les saucisses et saucissons secs sont dans le saloir'
lettres = {}
for car in texte:
    lettres[car] = lettres.get(car,0) + 1     # si pas rencontré: 0, si oui: augmenter la valeur de lettres[car] de 1

# maintenant on peut lire la fréquence d'un certain caractère:
print lettres['u']          # 2
print lettres['s']          # 14
                            # etc...
# ou bien:
print lettres               # pour afficher toutes les couples clés:valeur

# METTRE EN ORDRE ALPHABETIQUE
# un dictonnaire n'est pas une séquence ordonnée, donc on ne peut pas la trier avec .sort()
# solution convertir en liste (de tuples):
lettres_triees = lettres.items()        # d'abord convertir le dictionnaire en liste de tuples (voir plus haut)
lettres_triees.sort()                   # la liste peut être triée par alphabet
print lettres_triees

# GERER LE FLUX D'EXECUTION (alternative à une longue série de if - elif - else
def fonctionA():
    print 'fonction A executé'

def fonctionB():
    print 'fonction B executé'

def fonctionC():
    print 'fonction C executé'

dico = {'fer': fonctionA, 'bois': fonctionB, 'cuivre': fonctionC }
                                # attention, ne pas ajouter des () après les noms des fonctions,
                                # sinon exécution immédiatate à la création du dictionnaire

materiau = 'cuivre'             # la valeur est par exemple obtenu de l"utilisateur via input
dico[materiau]()                # dico[materieu] equivaut à dico['cuivre']
                                # et retourne comme valeur fonctionC
                                # en ajoutant () à la fin de fonctionC on obtient l'exécution de cette fonction


