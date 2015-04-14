# -*- coding: utf-8 -*-
# par rapport au tutoriel 1: ajouté le clock (ligne 8) et FPS (fin)
import sys, pygame

pygame.init()           # même chose pour tous les pygames

# pas strictement nécessaire pour l'animation, mais garantit une vitesse constante et déterminée par FPS
clock = pygame.time.Clock()

size = width, height = 320, 240                 # dimensions pour la fenêtre (screen)
screen = pygame.display.set_mode(size)          # crée une SURFACE (fenêtre graphique) sur laquelle on peut dessiner
speed = [1, 1]                                  # déplacement (en pixels) par tour, pour les directions x et y
black = 0, 0, 0                                 # definir une couleur. tuple de rouge, vert, bleu  (valeurs entre 0 et 250)
ball = pygame.image.load("girl.png")            # load retourne une autre surface, contenant l'image ball.bmp
ballrect = ball.get_rect()                      # crée un objet rect (=zone rectangulaire)
                                                # de la même dimension que ball
                                                # il est encore vide

while 1:                                        # crée une boucle infinie (1 est la même chose que True)
                                                # c'est une "condition" qui est toujours vraie
    # capter tous les événements qui se produisent
    # event.get() retourne une liste de tous les evenements qui se produisent (keys, mouse...)
    # la boucle for parcourt continuellement cette liste
    for event in pygame.event.get():      # tant que la boucle tourne, le programme est à l'écoute d'événements
        if event.type == pygame.QUIT:     # si le event est click sur la petite croix de fermeture,
            sys.exit()                    # on quitte le système, la boucle s'arrête donc

    # deplacer le rectangle, qui va contenir l'image de la balle (on ne peut pas déplacer l'image même)
    ballrect = ballrect.move(speed)             # à chaque tour de boucle on appelle la méthode move des rectangles

    # si le rectangle dépasse les limites de l'écran on inverse sa direction
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]                            # direction x
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]                            # direction y

    # peindre tout en noir (pour effacer l'ancienne position)
    screen.fill(black)
    # blit = copier les pixels d'une surface sur une autre (ceci se passe en arrière-plan, dans la mémoire)
    screen.blit(ball, ballrect)         # blit de l'image ball (source) dans ballrect (destination)
    # seulement quand cette copie est complète, le résultat est affiché à l'écran:
    #pygame.display.flip()               # correspond à un nouveau frame dans un film
    pygame.display.update()             # remplace la ligne précédente
    clock.tick(30)  # max 30 frames per seconde (FPS)