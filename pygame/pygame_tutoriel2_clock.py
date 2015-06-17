# -*- coding: utf-8 -*-
import sys, pygame

pygame.init()                                   # même chose pour tous les pygames
pygame.display.set_caption('Basic Pygame program')       # titre dans la barre du window

clock = pygame.time.Clock()                     # pas strictement nécessaire pour l'animation, 
                                                #mais garantit une vitesse constante et déterminée par FPS

dimension = largeur, hauteur = 320, 240         # dimensions pour la fenêtre (screen)
screen = pygame.display.set_mode(dimension)     # crée une SURFACE (fenêtre graphique) sur laquelle on peut dessiner
speed = [3, 2]                                  # déplacement (en pixels) par tour, pour les directions x et y
black = 0, 0, 0                                 # definir une couleur. tuple de rouge, vert, bleu  (valeurs entre 0 et 250)
ball = pygame.image.load("girl.png")            # load retourne une autre surface, contenant l'image girl.png
ball = ball.convert_alpha()                     # convert() ou convert_alpha() convertissent le format pixel de l'image à celui du screen
                                                # nécessaire pour accélerer le blit
                                                # _alpha pour garder les zones transparantes du png
ballrect = ball.get_rect()                      # crée un objet rect (=zone rectangulaire)
                                                # avec la même position (x,y) et la même dimension (hauteur, largeur) que ball
                                                

while 1:                                        # crée une boucle infinie (1 est la même chose que True)
                                                # c'est une "condition" qui est toujours vraie
    # capter tous les événements qui se produisent
    # event.get() retourne une liste de tous les evenements qui se produisent (keys, mouse...)
    # la boucle for parcourt continuellement cette liste
    for event in pygame.event.get():      # tant que la boucle tourne, le programme est à l'écoute d'événements
        if event.type == pygame.QUIT:     # si le event est click sur la petite croix de fermeture,
            sys.exit()                    # on quitte le système, la boucle s'arrête donc

    # deplacer le rectangle, qui va déterminer la nouvelle zone à couvrir par de blit de l'image  
    ballrect = ballrect.move(speed)             # à chaque tour de boucle on appelle la méthode move() des rectangles
                                                # qui change les valeurs x et y de ce rectangle 
                                                # en leur ajoutant les deux valeurs de speed    

    # si le rectangle dépasse les limites de l'écran on inverse sa direction
    # on peut utiliser les proprietés .left .right .top .bottom des rectangles pour déterminer les dépassements
    if ballrect.left < 0 or ballrect.right > largeur:
        speed[0] = -speed[0]                            # direction x (premier élément de la liste speed, donc speed[0]
    if ballrect.top < 0 or ballrect.bottom > hauteur:
        speed[1] = -speed[1]                            # direction y (deuxième élément de la liste speed, donc speed[1]

    # peindre tout en noir (pour effacer l'ancienne position)
    screen.fill(black)
    # blit = copier les pixels d'une surface sur une autre 
    screen.blit(ball, ballrect)         # blit de la surface "ball" (source) sur la surface "screen" 
                                                # où ballrect décrit la zone de destination
    # seulement quand cette copie est complète, le résultat est affiché à l'écran:
    #pygame.display.flip()              # correspond à un nouveau frame dans un film
    pygame.display.update()             # remplace la ligne précédente
    clock.tick(30)                      # limiter la vitesse à max 30 frames per seconde (FPS)
    
