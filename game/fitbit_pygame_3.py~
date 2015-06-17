# -*- coding: utf-8 -*-
import pygame
import sys
from pygame.locals import *

# fonction pas encore utilisé, mais utile
# charge une image chargé en mémoire et y ajoute son colorkey
# retourne l'image plus son Rect
def load_image(name, colorkey=None):
    # fullname=os.path.join("data", name)
    try:
        #image=pygame.image.load(fullname)
        image=pygame.image.load(name)
    except pygame.error, message:
        print "Impossible de charger l'image:",name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

# *******************************************
# TRANSFORMER CVS FITBIT: créer deux listes xListe et yListe,
# contenant resp. les coordonnées x et y de la courbe à dessiner
# *******************************************

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
def creerY(numCol):
    global nombreRecords, fibListe
    colListe = []
    derniereVraieValeur = 0

    for i in range(1, nombreRecords):
        if fibListe[i][numCol] != '' and fibListe[i][
            numCol] != '0':  # si le champ n'est pas vide et ne contient pas de 0,
            derniereVraieValeur = fibListe[i][numCol]  # c'est un valeur valide, on la mémorise
        else:  # si pas valide (le champ est vide ou contient 0)
            fibListe[i][numCol] = derniereVraieValeur  # on le remplace par la derniere valeur memorisé
        colListe.append(fibListe[i][
            numCol])  # on passe un string, mais pas de problème: il est automatiquement converti en int ou float
    return colListe

# *******************************************************************
# quelques fonctions pour la yListe et la création de niveaux
# ****************************************************************
# pas encore utilisé
# retourne le total cumulatif jusqu'a un certain moment du temps yliste[z]
def totalCumulatif(yListe, z):
    totalCumul = 0
    for i in range(0, z):
        totalCumul += int(yListe[i])
    return totalCumul


# def ecart_du_milieu(y, yListe, niveaux_liste):
def ecart_du_milieu(y, valeur_milieu, un_niveau):
    ecart = int(y) - valeur_milieu                    # = combien est y écarté de la valeur moyenne ?
    nombre_de_niveaux_ecart = ecart/un_niveau   # traduire ce chiffre en nombre de niveaus écarté de l'image moyenne
    return nombre_de_niveaux_ecart

def creer_liste_niveaux(yListe, un_niveau):
     # traduire y en 1 des 20 niveaus d'effort
    niveaux_liste = []
    for i in range(0, 21):
        niv_suivant = un_niveau * i
        niveaux_liste.append(niv_suivant)
    return niveaux_liste

def creer_liste_niveaux_cumulatif(yListe):
     # traduire y en 1 des 20 niveaus d'effort
    niveaux_liste_cumul = []
    totalCumul = int(totalCumulatif(yListe, len(yListe)))
    # print "totalCumul", totalCumul
    un_niveau_cumul = int(totalCumul/20)        # nombre de images d'animation
    # créer une liste avec les tous les niveaux (les seuils)
    for i in range(0, 20):
        niv_suivant = un_niveau_cumul * i
        niveaux_liste_cumul.append(niv_suivant)
    return niveaux_liste_cumul


def niveau_atteint(y, niveaux_liste, ecart):
    niveau_moyen = 10
    niv_atteint = niveau_moyen + ecart
    return niv_atteint

# ***********************************************
# Quelques fonctions pour les images
# ***********************************************
def choisirImageCumul(niveaux_liste, yCumul):
    imageIndex = 0
    for i in range(0, 20):
        if yCumul >= niveaux_liste[i] and yCumul < niveaux_liste[i+1]:
            imageIndex = i
            break
    return imageIndex
'''
def choisir_image(pos, niveaux_liste, valeur_milieu, un_niveau):
    # les x y non mis à l'echelle
    a, b  = pos
    ecart = ecart_du_milieu(b, valeur_milieu, un_niveau)
    # choisir l'index de l'image dans l'animation,
    # selon la valeur y de la courbe (dans item)
    imageInd = niveau_atteint(b, niveaux_liste, ecart)
    # pour eviter des "list index out of range" erreurs pas encore resolus (quand imageInd = 20)
    if imageInd >= 20:
        imageInd = 19
    elif imageInd < 0:
        imageInd = 0
    return imageInd
'''
# ******************************
    # alles hiertussen moet in een function komen
def creer_animation(yListe, curve):
    # faire correspondre chaque x de la courbe à une image, selon la valeur y

    maxListe = max(yListe)              # une fonction de python, retourne la valeur maximale
    # diviser le y maximum par le nombre d'images d'animation disponibles,
    # ainsi on obtient 20 niveaux de y, où chaque niveau pourra correspondre à une image
    un_niveau = int(maxListe/20)

    '''
    # creer une liste avec les valeurs y par niveau (donc p.e 20 niveaux: [0, 47, 94,... 940]
    niveaux_liste = creer_liste_niveaux(yListe, un_niveau)
    print "niveaux_liste", niveaux_liste
    '''
    '''
    # pas encore utilisé
    niveaux_liste_cumul = creer_liste_niveaux_cumulatif(yListe)
    yCumul = 0
    '''
    '''
    # la valeur y qui correspond au milieu des niveau, p.e. 470
    # ce niveau servira de "norme" moyenne, auquel les autres images auront un "écart" de n niveaux (en + ou -)
    valeur_milieu = niveaux_liste[10]
    #print "valeur_milieu", valeur_milieu
    '''

    # indexes_animation est une liste précalculé qui contient seulement l'index des images à afficher (valeur 0 à 20)
    # comme ils se suivront dans l'animation, (donc selon les nodes parcourus)
    # dont p.e [0, 7, 4, 15, ... jusque les 60 jours de mesurations de fitbit)
    indexes_animation = []

    for i in range(0, len(curve)):
        # index_image = choisir_image(curve[i], niveaux_liste, valeur_milieu, un_niveau)
        # a,b sont les x,y non mis à l'echelle
        a, b  = curve[i]
        # transformer la valeur y en une valeur niveau, qui correspondra à l'index d'une image
        index_image = b/un_niveau
        # pour eviter des "list index out of range" erreurs pas encore resolus (quand index_image = 20)
        if index_image >= 20:
            index_image = 19
        elif index_image < 0:
            index_image = 0

        indexes_animation.append(index_image)
    #print "indexes_animation",indexes_animation
    return indexes_animation

# *********************************************************
def main():
    # Event constant.
    TIMEREVENT = pygame.USEREVENT

    # The FPS the game runs at.
    FPS = 30

    # Color constants.
    RED = (255, 0, 0, 255)          #RED = "#FF0000"
    GREEN = (0, 255, 0, 255)        #GREEN = "#00FF00"
    BLACK = (0,0,0,255)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

    pygame.init()

    # Set the screen size.
    largeur = 800
    hauteur = 600
    screen = pygame.display.set_mode((largeur, hauteur))

    # la surface transparante pour dessiner la courbe (= les nodes et les lignes)
    marge_y_inf = 100
    drawing_surface = pygame.Surface((largeur,hauteur-marge_y_inf))
    drawing_surface.set_colorkey(BLACK)
    drawing_surface = drawing_surface.convert_alpha()        # faster blitting, convert_alpha() because transparency

    # créer le slider
    # 1) d'abord créer un surface qui contient l'image de la main
    hand = pygame.image.load("Hand_black.png")
    hand_rect = hand.get_rect()
    hand_rect.x = 0
    hand_rect.y = 500

    # 2) surface "parent" sur laquelle on blitte la surface "hand" et on dessine un ligne verticale
    slider = pygame.Surface((40, 600)).convert()
    slider_rect = slider.get_rect()
    slider_rect.x = 20
    slider_rect.y = 0
    pygame.draw.line(slider, RED, (20,0), (20,500), 1)
    slider.blit(hand, hand_rect)
    slider.set_colorkey(BLACK)                      # rendre le rectangle de la surface slider transparante
    slider = slider.convert_alpha()

    # surface transparante contenant 1 node jaune
    highlight = pygame.Surface((16,16))
    highlight_rect = highlight.get_rect()
    highlight.set_colorkey(BLACK)
    highlight.convert_alpha()           # rendre tout ce qui est déterminé par la colorkey (noir) transparant
    pygame.draw.circle(highlight, YELLOW, (8, 8), 8, 0)         # radius de 8, diametre 16

    # Use a timer to control FPS.
    pygame.time.set_timer(TIMEREVENT, int(1000 / FPS))

    # doit être wav ou ogg, pas mp3 !
    # son = pygame.mixer.Sound("snd/arabicperc1-10.wav")

    # ***************************************************************
    # à partir du csv, creation des axes x et y, sous la forme de deux listes (xListe et yListe)
    #name=raw_input("please enter the name of the csv file you want to illustrate")
    #creerFibTableau(name)    
    creerFibTableau("jawbone.csv")
    xListe = creerX()
    #quellesColonnes = [13, 37]
    quellesColonnes = [13]     # quellesColonnes doit être sous format de liste, même s'il n'y a qu'un element

    # pourrait être simplifié puisqu'on n'affiche qu'une seule colonne (courbe)
    nombreColonnesAMontrer = len(quellesColonnes)
    # attention, on n'affiche plus tout de suite la courbe avec matplotlib,
    # avec for, une deuxième yListe_strings effacerait donc le premeir
    # pour le moment ça marche parce qu'on n'a qu'une seule yListe à sauvegarder
    # remarque: appelé "yListe_strings" parce que cvs donne les valeurs en tant que chaines,
    # dans un deuxième temps on crée la vraie yListe, en transformant chaque valeur en int
    # sans doute les 2 boucles "for" pourraient être combinés, mais ça rend le code trop confus
    yListe_strings = []
    for i in range(0, nombreColonnesAMontrer):
        yListe_strings = creerY(quellesColonnes[i])

    yListe = []
    for j in range(0, len(yListe_strings)):
        yListe.append(int(yListe_strings[j]))

    # pas encore utilisé
    totalCumulatifListe = totalCumulatif(yListe, len(yListe))

    # scale yListe: on rend toutes les valeurs y plus petites, pour qu'elles rentrent dans notre drawing_surface(800, 600)
    for i in range(0,len(yListe)):
        y = yListe[i] / 40.0       # 40 au pif.  La division demande un float et produit un float
        yListe[i] = int(y)         # après on reconvertit en int et on remplacce l'ancienne valuer par la nouvelle

    # ***********************************************$
    # à partir de xListe et yListe, précalculer une liste "curve"
    # qui contiendra une suite des couples (x, y) de la courbe à dessiner
    curve = []
    for x, y in zip(xListe, yListe):        # la fonction zip() de python lit les valeurs de deux listes en même temps
        x = x * 15      # 15 au pif: pour espacer plus les valeurs sur axe x (étirer la courbe)
                        # les valeurs y ont déjà été mis à l'échelle plus haut
        curve.append((x,y))

    # ******************************************
    # nodes_list est la même chose que curve, mais "amélioré":
    # il contient des rects (=cliquables) au lieu de seulement les valeurs de coordonnees (x,y)
    # ansi le coordonées xy peuvent devenir "cliquables" pour la souris (détection collision souris-rect)
    nodes_list = []
    for i in range(0, len(curve)):
        coordx, coordy = curve[i]
        r = pygame.Rect(coordx, coordy, 15,15)          # transformer les coordonnées en rect
        nodes_list.append(r)


    # créer une liste qui stocke en mémoire vive les 20 images morphés, dans l'ordre (numerotées de 0 à 20)
    images_librairie = []
    for i in range(0,20):
        fileImage = "animation" + str(i) + ".jpg"
        image = pygame.image.load(fileImage)
        # si nécessaire, redimensionner l'image
        taille = image.get_size()         # retourne une liste, avec taille[0] = largeur et taille[1] = hauteur
        # create a 2x bigger image than self.image
        bigger_img = pygame.transform.scale(image, (int(taille[0]*2), int(taille[1]*2)))
        images_librairie.append(bigger_img)
    # afficher déjà la premiere image à l'écran
    screen.blit(images_librairie[0], (0, 0))

    # précalculer une liste qui indque la suite des images à afficher, en avancant sur l'axe x
    # chaque image sera choisi selon la valeur y à cet endroit
    # p.e. indexes_animation = [3, 5, 10, 6.... ]
    # à la position x = 2, on va donc chercher dans images_librairie[2] l'image animation10.jpg
    # cette liste contient donc autant d'élément que de points sur la courbe = nombre de x)
    indexes_animation = creer_animation(yListe, curve)

    # initialiser qqs variables pour le while loop (game loop)
    dessin_fini = False
    drag = False
    h_rect = (0,0,0,0)                  # pour positionner les highlights sur la courbe
    counter_x = 0                       # utilisé dans le dessin de la courbe

    while True:
        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Draw the screen based on the timer.
            if ev.type == TIMEREVENT:

                # dessiner lentement la courbe en parcourant les valeurs x,y de la liste "curve"
                # tout le loop ci-dessous bloque le programme jusqu'à ce que la courbe soit complètement dessiné
                # mais ça ne pose pas vraiment un problème
                while counter_x < len(curve)-1:
                    # lire dans curve les valeurs (x,y) à cet endroit x de la courbe
                    item = curve[counter_x]
                    # ainsi que le (x,y) du item suivant pour pouvoir dessiner la ligne
                    item_suivant = curve[counter_x + 1]

                    pygame.draw.circle(drawing_surface, GREEN, item, 5, 5)
                    pygame.draw.line(drawing_surface, GREEN, item, item_suivant,1)

                    # lire dans images_serie le numero de l'image qui correspond a cette position x
                    index_image = indexes_animation[counter_x]
                    # ce numero sert d'index pour retrouver cet image dans la "librairie"
                    img = images_librairie[index_image]                  # blitter à 0,0 (coin sup gauche)
                    screen.blit(img, (0, 0))                    # blitter dans le coir sup gauche
                    screen.blit(drawing_surface, (0,0))         # blitter la courbe au-dessus l'image
                    pygame.display.flip()
                    # pour ralentir l'animation
                    #pygame.time.delay(50)

                    counter_x += 1                                  # avancer sur l'axe x
# moet die indent 1 naar links ??
                dessin_fini = True

            elif ev.type == pygame.MOUSEBUTTONDOWN:
                if dessin_fini:                     # on peut seulement bouger le slider après la finition du dessin
                    pos = pygame.mouse.get_pos()
                    mousex, mousey = pos            # le tuple "pos" contient deux valeurs qui sont "déballés"

                    # si la souris se trouve au-dessus du slider: mettre le 'flag' qui permet le drag
                    if slider_rect.collidepoint(pos):
                        drag = True

                    # parcourir toute la liste des nodes pour vérifier
                    # si la position de la souris correspond à celle d'un node:
                    # ce node est cliqué: changer l'image

                    # d'abord créer une zone de détection plus large autour du click
                    # ??? is dit nog nodig ??? nu de nodes zelf een grotere rect hebben?
                    zone_rect = pygame.Rect(mousex, mousey, 20, 20)
                    for i in range(0, len(nodes_list)):

                        # detecter collision entre souris et node
                        if nodes_list[i].collidepoint((zone_rect.centerx, zone_rect.centery)):
                            # canal_son = geluid.play()

                            # lire de quel image il s'agit et le sauvegarder dans une variable
                            # imageInd = montrer_image(i, curve, yListe, niveaux_liste, valeur_milieu, un_niveau)
                            index_image = indexes_animation[i]

                            # dessiner un highlight sur la courbe, à l'endroit cliqué
                            # la position est déterminé par nodes_list[i],
                            # mais on a besoin de corriger un peu cette position, d'où les 3 lignes suivantes:
                            #pygame.draw.rect(drawing_surface, RED, nodes_list[i])
                            h_rect = nodes_list[i].copy()                     # copie, pour ne pas altérer l'original
                            h_rect.centerx = nodes_list[i].centerx - 8      # - 8 au pif
                            h_rect.centery = nodes_list[i].centery - 8
                            drawing_surface.blit(highlight, h_rect)

            elif ev.type == pygame.MOUSEBUTTONUP:
                # mettre le 'flag' qui empêche le drag
                drag = False

            # si la souris bouge tandis que le drag est permis: déplacer le slider et montrer l'image approprié
            elif ev.type == MOUSEMOTION:
                mousex, mousey = ev.pos
                if drag == True:
                    slider_rect.centerx = mousex    # update de la position slider pour pouvoir le blitter

                    # le code suivant pour le drag correspond au code pour le mouse click plus haut
                    #
                    i = mousex/15              # refaire l'espacement de l'axe x à l'envers
                    index_image = indexes_animation[i]
                    h_rect = nodes_list[i].copy()
                    h_rect.centerx = nodes_list[i].centerx - 8   # -8 est un correction pour que ça tombe juste
                    h_rect.centery = nodes_list[i].centery - 8


        screen.fill(BLACK)
        # afficher l'image morphé en fond d'écran
        screen.blit(images_librairie[index_image], (0, 0))
        # afficher la courbe au-dessus
        screen.blit(drawing_surface, (0,0))
        # quand l'animation est finie, on montre aussi le slider et le dernier highlight
        if dessin_fini == True:
            pygame.draw.line(screen, WHITE, (0,520), (800,520), 3)  # simuler un "rail" pour le slider
            screen.blit(slider,slider_rect)
            screen.blit(highlight, h_rect)      # blitter un highlight à la position déterminé plus haut
        pygame.display.flip()

        # ????
        pygame.time.delay(200)


if __name__ == "__main__":
    main()


