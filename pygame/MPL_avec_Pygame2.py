# -*- coding: utf-8 -*-
# exemple inspiré de https://www.pygame.org/wiki/MatplotlibPygame?parent=CookBook

import matplotlib
import sys
import pygame
from pygame.locals import *     # contient des constantes, comme DOUBLEBUF

# pour integrer MPL vec Pygame, nous devons utiliser un non-interactive backend ("Agg"),
# pour éviter que mpl utilise son propre GUI:
matplotlib.use("Agg")                               # le backend (?) qu'on veut utiliser
                                                    # p.e. pour Tkinter c'est TkAgg
# attention: la commande .use doit être utilisé avant l'import de matplotlib.backends, pylab, matplotlib.pyplot
# sinon, le backend est déjà déterminé
import matplotlib.backends.backend_agg as agg       # donner alias pour appeler ce backend
import matplotlib.pyplot as plt
import pylab                                        # pylab combines pyplot with numpy into a single namespace
import fitbit_MPL_4_module_bis as fb

pygame.init()

# pas strictement nécessaire pour l'animation, mais garantit une vitesse constante et déterminée par FPS
clock = pygame.time.Clock()

size = (600, 400)
window = pygame.display.set_mode(size, DOUBLEBUF)
screen = pygame.display.get_surface()

# explication de: http://www.labri.fr/perso/nrougier/teaching/matplotlib/
# When we call plot, matplotlib calls gca() to get the current axes
# and gca in turn calls gcf() # to get the current figure.
# If there is none it calls figure() to make one,
# strictly speaking, to make a subplot(111)

# ici on va faire tout ça explicitement: créer d'bord une figure, puis des axes à partir de cette figure

# creer un figure qui contiendra des axes et un canvas, sur lequel on peut dessiner un (non-interactive) plot
fig = pylab.figure(figsize=[4, 4],  # Inches
                   dpi=100,  # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )

# préciser le système d'axes dans la figure
# cette étappe est optionelle, on peut aussi utiliser "plt" à la place de "ax" dans le code ci-dessous
# seulement utile si on veut changer les axes (p.e. partant du milieu, au lieu du coin inférieur gauche etc
# ax = fig.gca()

# ceci était l'exemple donné, on va remplacer ces listes X et Y par nos propres données fitbit
#ax.plot([1, 2, 3], [4, 5, 6])

#  créer les listes pour les courbes
fb.creerFibTableau("jawbone.csv")

xListe = fb.creerX()
col = [13, 37]
for i in range(0, len(col)):
    yListe = fb.creerY(col[i])
    # ax.plot(xListe, yListe)           # xListe est optionel !
    plt.plot(xListe, yListe)        # ceci marche aussi, automatiquement la figure existante est utilisé

# optionnel, si on veut changer le look de la courbe
#line, = plt.plot(yListe)
#plt.setp(line, color='r', linewidth=2.0)

# transformer la figure (contenant le plot) en un canvas (surface dessinable), grâce à agg
canvas = agg.FigureCanvasAgg(fig)
canvas.draw()                                   # dessine le canvas, mais celui-ci n"est pas visible ??

# a partir  du canvas, créer une "surface", qu'on pourra blitter sur le screen
# d'abord créer un renderer pour lire le contenu du canvas, (cad le contenu de fig)
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()              # attribuer le contenu "rendu" à une variable (de type string)

size = canvas.get_width_height()                # lire la dimension de canvas, donc de fig

# créer une pygame "surface"
# qui contient les raw_data (un string transformation du canvas, sur lequel on a déjà dessiné fig (avec draw)
surf = pygame.image.fromstring(raw_data, size, "RGB")
screen.blit(surf, (0, 0))               # le code jusqu'ici suffirait si on ne veut pas ajouter une animation


# AJOUTER UN PERSONNAGE ANIMEE
# preparer le personnage
img = pygame.image.load('girl.png')
yPos = 0

# blit "surf" et "img" en boucle
while True:
    # attendre que l'utilisatuer clique la petite croix pour fermer
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # effacer l'écran en le remplissant de blanc (effacer la position précédente de l'image)
    screen.fill((255, 255, 255))

    # calculer la nouvelle position du personnage
    yPos += 5
    if yPos > 400:
        yPos = 0
    pos = (200, yPos)  # un tuple

    # blitter la courbe et le personnage sur le screen
    screen.blit(surf, (0, 0))           # comme l'écran a été effacé, il faut aussi blitter la courbe
    screen.blit(img, pos)               # attention à l'ordre des commandes blit:
                                        # le dernier d'affiche au-dessus du précédent

    # redessiner tout
    pygame.display.update()
    clock.tick(30)  # max 30 frames per seconde (FPS)
