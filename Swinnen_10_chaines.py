# -*- coding: utf-8 -*-

#Il y a plusieurs sortes de SEQUENCES de données: chaînes, listes, tuples, dictionaries...
#CHAINES = séquence de caractères individuels
nom = 'Germaine'
print nom
print nom[1], nom[3]        # chaque caractère peut être LU par son index, (idem méthodes liste) mais pas CHANGE:
# nom[0] = 'J'              # erreur: on ne peut pas changer les caractères individuels, lecture seulement
print nom[1:3]              # 'er'  lit de 1 à 3 (3 n'est pas compris!) Notation indexes comparable avec les listes
print len(nom)              # attention, ne donne la longueur exacte qu'avec des chaines convertis en unicode (voir ci-dessous)

# caractères spéciaux et conversion en unicode
nom = 'Cédric'
print "afficher la chaine totale avec des caractère spéciaux, pas de souci ", nom
print "essai d'afficher 1 caractère spécial dans la chaine, problème ", nom[1]
# é s'affiche mal en Python: il faut convertir le BYTE string de python en string UNICODE  (utf-8)
# (le é sera alors encodé comme u'\xe9', mais en arrière-plan, pas visible)
# 2 possibilités pour cette conversion:
# nomUnicode = u'Cédric'             # ajouter u devant le 'string literal'
nomUnicode = nom.decode('utf-8')    # utiliser la fonction decode avec le string variable
print "après conversion en unicode c'est correct: ", nomUnicode[1]

# un problème supplémentaire se pose quand on veut lire et écrire vers un fichier texte
# (qui est automatiquement crée avec encodage Latin1, pas utf-8)
# pour ECRIRE un chaîne vers un fichier, il faut d'abord qu'il soit converti en unicode, puis encodé en Latin1
of = open("MonFichier.txt", "w")
nomUnicode = nom.decode('utf-8')        #premier pas, mais ne suffit pas
#of.write(nomUnicode)        #UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9'
nomLatin = nomUnicode.encode('Latin1')  #maintenant c'est bon
of.write(nomLatin)
of.close()

#pour LIRE une fichier en Python) opération inverse
of = open("MonFichier.txt", "r")
monTexte = of.read()
#ici on combine le encode-decode en une seule commande
monTexteUnicode = monTexte.decode('Latin1').encode('utf-8')
print "lecture du fichier, décodé du Latin1, encodé en utf-8: \n", monTexteUnicode
of.close()

#combiner des chaînes
n = 'abc' + 'def'       # concaténer des chaines
m = 'zut! ' * 4         # répétition

# traverser un chaine (ici pour afficher chaque caractère séparement)
for caract in n:            # caract est une variable, on lui donne le nom qu'on veut
    print caract + ' -',    # la virgule finale fait que les caractères s'affichent sur une seule ligne
print 'fin'

# rechercher un ou une sequence de caractères dans une chaine (mais on n'apprend pas sa position, voir find() et index() ci-dessous)
if "ef" in n:
    print "ef est trouvé"

# convertir un chaine en une liste de sous-chaines
c = "Votez pour moi"
aListe = c.split()                  # split appelé sans argument splitte la chaine sur les espaces (= defaut)
print "aListe créé par split sur espaces (= défaut)" , aListe            #['Votez', 'pour', 'moi']
c = "Cet exemple, parmi d'autres, peut encore servir"
aListe = c.split(",")                 # splitte sur les virgules,
                                    # ["Cet exemple", "parmi d'autres", "peut encore servir"]
print "aListe, crée par split sur virgules ", aListe

#rassemler les éléments d'une liste en 1 seule chaine, ici séparé par ;  (le delimitateur)
chaineTotale = ";".join(aListe)     # le délimitateur peut aussi être un espace " " ou tout autre caractère
print "La chaine après join ", chaineTotale                  # Cet exemple; parmi d'autres; peut encore servir

#rechercher la première occurance (index) d'une ou plusieurs caractères. Attention, unicode obligatoire, sinon faux !
chTotale = u"Cette leçon vaut bien un fromage, ou autre chose qu'un fromage"
aTrouver = u"fromage"
saPosition = chTotale.find(aTrouver)
print "saPosition ", saPosition                 #25  Il ne retrouve donc que l'index de la premiere occurance de "fromage"
                                                # solution: index() voir ci-dessous
# autre système, plus souple
saPosition = chTotale.index(aTrouver)
print "saPosition avec index ", saPosition
print "occurance suivante ", chTotale.index(aTrouver, saPosition+1)    # renouveler la recherche, mais à partir de l'index déjà trouvé

#autres fonctions utiles
print "nombreDeOccurances ", chTotale.count(aTrouver)      # 2  (le mot fromage apparait 2 fois
print chTotale.lower()
print chTotale.upper()                               # utiliser une chaîne unicode pour maj des caractères avec accents
print chTotale.title()                               # majuscule initiale à chaque mot
print chTotale.capitalize()                          # maj première lettre seulement
print chTotale.strip()                               # enlève ev. espaces superflus au début et à la fin de la chaine
print chTotale.replace(" ", "*")                     # remplacer un caractère par un autre, ici espace par *

#conversions
a = float("12.36")                              # chaine en nombre réel (float) attention ! point, pas virgule
b = int("184")                                  # chaine en int
c = str(17.46)                                  # float en str
d = unicode(15) + unicode([17.4, 'zut'])        # crée un chaine unicode à partir de chiffres, listes etc...


#FORMATAGE (combiner texte et variables en 1 string)
couleur = "verte"
temp = 1.34 + 15.9
print "La couleur est %s et la température vaut %s degrés Celsius " % (couleur, temp)
# les deux marqueurs %s sont inclus dans le string !
# ce sont des "placeholders" qui recevront resp. la première et deuxième variable (couleur, temp)
# s'il y a plusieurs variables ils sont séparés par des virgules

# le marqueur %s accepte n'importe quel type d'object, donc le plus facile
# pour plus de précision, par exemple:
# %d    convertit la variable en nombre entier (int)
# %f    convertit la variable en nombre réel (float)

# encore plus rigolo:
# %8.2f     prévoit 8 espaces en tout pour la variable float et affiche 2 chiffres après la virgule

# autre possibilité (sans doute qq millisecondes moins rapide)
print "La couleur est " +  str(couleur) + " et la température vaut " + str(temp) +  " degrés Celsius"
