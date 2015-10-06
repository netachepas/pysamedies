# Programe du  Workshop


Lors de nos réunions hebdomadaires des Pysamedies (www.samedies.be) nous nous rencontrions à l'origine pour aborder ensemble l'apprentissage d'un langage de programmation: python. Nous avons choisi de nous baser sur les sets de données des capteurs personnels. Ces outils semblaient répondre à un intérêt commun, plusieures d'entre nous en utilisaient déjà un, d'autres envisageaient de le faire, certaines parce qu'elles devaient faire face à une maladie chronique, d'autres simplement par envie de suivre de plus près leur état de santé, d'autre par curiosité parce que elles s'intéressaient au question de santé, la leur et/ou celle des autres (comme dans de nombreux groupes de femmes).


## Breve présentation des pratiques du quantified self 

Qu'est ce qu'un set de données, à quoi est-ce que cela sert?
  
Nous utilisons des outils pour nous aider à nous tenir en forme physique notamment pour mesurer notre effort, des capteurs sont intégrés à ces outils, des données sont capturées par ces interfaces commerciales (fitbit, apple watch, jawbone etc...), et sont hébergées sur les serveurs des entreprises vous proposant leurs services, leurs plateforme sociale entre autres). Vous êtes vous jamais demandées à quoi ressemble ces set de données:

Voici plusieurs types de données que vouis pourrez télécharger et pour regarder à quoi ressemble ces information qui sont vos données de self tracking:

  - [Fitbit](https://github.com/netachepas/pysamedies/tree/master/workshop%20sophia/data/fitbit_export.csv)
  - [Jawbone](https://github.com/netachepas/pysamedies/tree/master/workshop%20sophia/data/jawbone.csv)
  - [Accéléromètre](https://github.com/netachepas/pysamedies/tree/master/workshop%20sophia/data/accelero)
  - [Autre chose](https://github.com/netachepas/pysamedies/tree/master/workshop%20sophia/data/autre_chose) 


Quelles informations sont reprises par nos systèmes de captation:
  - Poids
  - Verres d'eau bus
  - Nombre de pas faits
  - Minutes actives/sommeil

Mais les réseaux sociaux de chaque device proposent également des services pour organiser une communauté autour des questions associées au fitness:
  - Possibilité de faire un programme alimentaire personnalisé
  - Possibilité de mettre en place un réseau d'amis qui peuvent alors te soutenir.
  - Possibilité de synchrononiser son fitness tracker avec son smart phone qui capture toute sortes d'autres informations comme la géolocalistion (par le gps, mais pas uniquement)


Cependant il y a également un grand nombre de choses que les interfaces de fitness tracker ne permettent pas
  - Informations contextuelles (environementales (le temps qu'il fait), personnelles (pas le temps j'ai mon enfant qui est tombé malade), subjectives (je suis triste, déçue anxieuse).
  - tableau périodique qui permet de mieux connaitre son cycle.
  - état général de santé 
  - toutes sortes de particularités (je suis unijambiste, naine, sous traitement hormonal) ou tout simplement, je ne rentre pas de le profil. 

Comment alors concevoir une interface sociale qui intégrerait ces souhaits ces différences ces particularités qui font la vie de la plupart des personnes.

## La question des visuels

Les données sont omniprésentes, nous vivons à une époque où nous pouvons tout mesurer, chaque détail, archiver chaque action de notre vie, nous en avons les moyens. Mais alors il faut un peu se pencher sur l'environnement dans lequel nous allons vivre au milieu de toutes ces données.
Que voulons nous exactement retranscrire, voulons nous que notre vie ressemble à un immense tableau de bord?
Aussi cet atelier vous proposera une interface en ligne pour regarder à quoi ressemblent ces données et envisager de les représenter différemment. 
 
### atelier de données

Comment récupérer à partir des sites.

il est possible de récupérer ses données fitbit à partir de l'interface de leur site, pour cela il faut suivre quelques étapes:
  - tout d'abors allez sur votre profil
  - Puis sur la droite de l'écran allez dans settings/export de données.
  - Vous pourrez choisir les données que vous voulez télécharger (corps activité sommeil etc..) et la période au maximum un mois.
  - Puis devrez choisir le format du fichier, (xls ou csv) pour ce workshop cas nous utiliserons un fichier CSV.

Comment faire nos propres courbes 
  - rependre ces sets de données et les réinterpréter avec MPL
  - Leur associer de nouveaux visuels qui soient personnalisés et nous permettent de sortir du * Tableau de Bord *

Nous proposerons lors de cet atelier de réemployer ces outils développés lors des workshop de Pysamedies, (Vera en a fait beaucoup). 

#### Demarrer le serveur python

Démarrer un serveur local: en double-cliquant le fichier localCGIServer.py. 
Ceci ouvrira un fenêtre qui devra afficher: Localhost CGI started. 
Laisser cette fenêtre ouverte pendant toute la séance. Fermer la fenêtre pour arrêter le serveur.

Ouvrir un browser et rentrer l'adresse suivante pour charger le programme:
localhost:8080/fitbit_phaser/
(ou fitbit_phaser est le sous-répertoire qui contient le programme proprement dit. 

Dans la page qui s'affiche dans le browser, cliquer Start et naviguer vers le fichier fitbit_export.csv (ou une autre fichier csv qu'on a téléchargé chez fitbit)


#### Quelles Images


La présence intrusive des systèmes de visualisation de données en association avec les pratiques corporelles est envahissante nous avons déjà essayé de poser la question des visuels à plusieurs reprises notamment lors d'un atelier mené à [Relearn](http://water-wheel.net/media_items/view/5944) en aout dernier.

## La question de la vie privée: 

Le fitness tracker est un outil qui permet de retracer ses pratiques de fitness à des fins de bien être personnel, mais cette pratique peut éventuellement mener à des bénéfices insoupçonnés, ainsi dans de nombreux endroits (pas en Belgique) les compagnies d'assurance offrent à leur clients des capteurs de selftracking (fitbit le plus souvent) et proposent des réductions ou des cadeaux préférentiels aux clients qui leur transmettraient leurs données.


Votre fitness tracker peut révéler que vous avez une aventure pendant votre heure de repas.

De plus en plus de systèmes prennent en compte la localisation ce qui permet de corréler toutes sortes d'informations, recréer les mouvements de spersonnes même des dizaines d'années après leur occurence ce qui est quelque chose que nous n'avons jamais pu faire jusqu'à maintenant.

Certaines personnes ont entrepris de mentir à leur [fitbit](http://www.unfitbit.com)

## La question des données de la santé

Ces données de capteurs sont elles des données de santé?
Il manque un certain nombre de modes de fonstionnement qui sont habituellement employés dans les systèmes de santé, et qui caractérisent une relation dans le domaine médical.
Comment un réseau social comme celui de fitbit peut il remplacer.
  * De quelles caractéristiques devrait-il faire preuve? 
  * Comment l'organiser, sur quelles bases
  * De quoi un tel réseau devrait-il se préoccuper?

[fitbit est quoté en Bourse depuis le mois d'aout](http://www.marketwatch.com./investing/stock/fit/profile)




g
